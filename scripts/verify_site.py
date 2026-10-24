"""Accept an exact static archive without extracting or accessing its source tree."""

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import tarfile

# Kept independent of the builder so an accidental publication-scope expansion fails.
EXPECTED_PUBLIC = {
    "index.html", "stories.html", "practice.html", "week.html",
    "next-step.html", "sources.html", "guide.html", "print.html",
    "style.css", "favicon.svg", "music-practice-packet.pdf",
    "facilitator-outline.pdf", "404.html", "deployment.json", "release.json",
}


def verify(archive, expected_commit, expected_version=None):
    if not re.fullmatch(r"[0-9a-f]{40}", expected_commit):
        raise ValueError("Expected source commit must be a full SHA")
    checksum_path = archive.with_name(archive.name + ".sha256")
    checksum_parts = checksum_path.read_text().split()
    if len(checksum_parts) != 2 or checksum_parts[1] != archive.name:
        raise ValueError("Invalid archive checksum file")
    if hashlib.sha256(archive.read_bytes()).hexdigest() != checksum_parts[0]:
        raise ValueError("Archive checksum mismatch")
    files = {}
    with tarfile.open(archive, "r:gz") as tar:
        for member in tar:
            path = PurePosixPath(member.name)
            if not member.isfile() or path.is_absolute() or ".." in path.parts or member.name in files:
                raise ValueError("Unsafe or duplicate archive member")
            if member.size > 20_000_000:
                raise ValueError("Unexpectedly large static file")
            stream = tar.extractfile(member)
            if stream is None:
                raise ValueError("Unreadable archive member")
            files[member.name] = stream.read()
    expected = {f"public/{name}" for name in EXPECTED_PUBLIC} | {"manifest.json", "deployment-contract.json"}
    if set(files) != expected:
        raise ValueError("Static archive does not match the independent publication allowlist")
    manifest = json.loads(files["manifest.json"])
    if manifest["schema_version"] != 1 or manifest["application"] != "versetwo.org":
        raise ValueError("Wrong application manifest")
    if manifest["source"]["commit"] != expected_commit or manifest["source"]["repository"] != "anderson-webops/versetwo.org":
        raise ValueError("Wrong source identity")
    version = manifest.get("version")
    if version is not None and not re.fullmatch(r"(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)", version):
        raise ValueError("Invalid artifact version")
    if expected_version is not None and version != expected_version:
        raise ValueError("Wrong artifact version")
    if expected_version is not None and manifest["source"]["ref"] != f"v{expected_version}":
        raise ValueError("Release artifact must identify its version tag")
    if set(manifest["files"]) != expected - {"manifest.json"}:
        raise ValueError("Incomplete artifact inventory")
    for name, item in manifest["files"].items():
        data = files[name]
        if len(data) != item["bytes"] or hashlib.sha256(data).hexdigest() != item["sha256"]:
            raise ValueError(f"Artifact file integrity failure: {name}")
    contract = json.loads(files["deployment-contract.json"])
    if (contract["schema_version"], contract["application"], contract["kind"], contract["artifact"]["document_root"]) != (1, "versetwo.org", "static", "public"):
        raise ValueError("Unsupported static hosting contract")
    identity = json.loads(files["public/deployment.json"])
    expected_identity = {"commit": expected_commit, "ok": True, "ref": manifest["source"]["ref"], "runtime": "static", "service": "front-end"}
    if version is not None:
        expected_identity["version"] = version
    if identity != expected_identity:
        raise ValueError("Served source identity differs from the manifest")
    if files["public/release.json"] != files["public/deployment.json"]:
        raise ValueError("release.json must mirror deployment.json")
    for name in EXPECTED_PUBLIC:
        data = files[f"public/{name}"]
        if name.endswith(".html") and (b"<!doctype html>" not in data.lower() or b'<main id="main"' not in data):
            raise ValueError(f"Invalid HTML entrypoint: {name}")
        if name.endswith(".pdf") and not data.startswith(b"%PDF-"):
            raise ValueError(f"Invalid PDF: {name}")
    return {"archive": archive.name, "source_commit": expected_commit, "version": version, "public_files": len(EXPECTED_PUBLIC), "integrity": "pass", "publication_allowlist": "pass"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--version", help="Require this version and its matching release tag")
    args = parser.parse_args()
    print(json.dumps(verify(args.archive, args.commit, args.version), indent=2))


if __name__ == "__main__":
    main()
