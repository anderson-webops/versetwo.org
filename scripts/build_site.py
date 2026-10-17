"""Build an allowlisted, reproducible static artifact for the protected web host."""

import argparse
import gzip
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import tarfile

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_FILES = (
    "index.html", "stories.html", "practice.html", "week.html",
    "next-step.html", "sources.html", "guide.html", "print.html",
    "style.css", "favicon.svg", "music-practice-packet.pdf",
    "facilitator-outline.pdf",
)
ARCHIVE_NAME = "versetwo.org-static.tar.gz"


def json_bytes(value):
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode()


def build(source, contract_path, destination, commit, ref):
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise ValueError("A full lowercase source commit SHA is required")
    if not re.fullmatch(r"[A-Za-z0-9._/+@-]{1,160}", ref):
        raise ValueError("Invalid source ref")
    if contract_path.is_symlink():
        raise ValueError("The deployment contract must be a regular file")
    contract = json.loads(contract_path.read_text())
    if (contract.get("schema_version"), contract.get("application"), contract.get("kind")) != (1, "versetwo.org", "static"):
        raise ValueError("Unsupported deployment contract")
    payload = {}
    for name in PUBLIC_FILES:
        path = source / name
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"Missing or non-regular public file: {name}")
        payload[f"public/{name}"] = path.read_bytes()
    payload["public/deployment.json"] = json_bytes({
        "commit": commit, "ok": True, "ref": ref,
        "runtime": "static", "service": "front-end",
    })
    payload["deployment-contract.json"] = json_bytes(contract)
    manifest = {
        "schema_version": 1, "application": "versetwo.org",
        "source": {"commit": commit, "ref": ref, "repository": contract["source_repository"]},
        "files": {
            name: {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}
            for name, data in sorted(payload.items())
        },
    }
    payload["manifest.json"] = json_bytes(manifest)
    destination.mkdir(parents=True, exist_ok=True)
    archive = destination / ARCHIVE_NAME
    with archive.open("wb") as output:
        with gzip.GzipFile(filename="", fileobj=output, mode="wb", mtime=0) as compressed:
            with tarfile.open(fileobj=compressed, mode="w") as tar:
                for name, data in sorted(payload.items()):
                    entry = tarfile.TarInfo(name)
                    entry.size = len(data)
                    entry.mode = 0o644
                    entry.mtime = 0
                    tar.addfile(entry, io.BytesIO(data))
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    (destination / f"{ARCHIVE_NAME}.sha256").write_text(f"{digest}  {ARCHIVE_NAME}\n")
    (destination / "manifest.json").write_bytes(payload["manifest.json"])
    (destination / "deployment-contract.json").write_bytes(payload["deployment-contract.json"])
    return archive


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--ref", default="main")
    parser.add_argument("--output", type=Path, default=ROOT / "build")
    args = parser.parse_args()
    actual_commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    if actual_commit != args.commit:
        raise ValueError("Requested source commit does not match this checkout")
    subprocess.run(["git", "diff", "--exit-code", "HEAD", "--", "prototype", "deployment-contract.json", "scripts/build_site.py", "scripts/verify_site.py"], cwd=ROOT, check=True)
    archive = build(ROOT / "prototype", ROOT / "deployment-contract.json", args.output, args.commit, args.ref)
    print(f"Built {archive}")


if __name__ == "__main__":
    main()
