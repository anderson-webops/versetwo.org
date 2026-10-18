"""Check version/changelog consistency and immutable annotated release identity."""

import argparse
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
VERSION_PATTERN = r"(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)"


def read_version(root):
    path = root / "VERSION"
    if path.is_symlink() or not path.is_file():
        raise ValueError("VERSION must be a regular file")
    version = path.read_text().strip()
    if not re.fullmatch(VERSION_PATTERN, version):
        raise ValueError("VERSION must be a stable semantic version")
    return version


def release_notes(root, version):
    heading = f"## v{version}\n"
    text = (root / "CHANGELOG.md").read_text()
    if text.count(heading) != 1:
        raise ValueError("CHANGELOG.md must contain one section for VERSION")
    notes = text.split(heading, 1)[1].split("\n## ", 1)[0].strip()
    if not notes:
        raise ValueError("The release changelog section must not be empty")
    return notes + "\n"


def git(root, *args):
    return subprocess.check_output(["git", *args], cwd=root, text=True).strip()


def check_tag(root, tag, commit):
    version = read_version(root)
    release_notes(root, version)
    if tag != f"v{version}":
        raise ValueError("Release tag must exactly match VERSION")
    if not re.fullmatch(r"[0-9a-f]{40}", commit) or git(root, "rev-parse", "HEAD") != commit:
        raise ValueError("Release commit must match the full checkout SHA")
    if git(root, "status", "--porcelain", "--untracked-files=normal"):
        raise ValueError("Release requires a clean checkout")
    tag_ref = f"refs/tags/{tag}"
    if git(root, "cat-file", "-t", tag_ref) != "tag":
        raise ValueError("Release requires an annotated tag")
    if git(root, "rev-parse", f"{tag_ref}^{{commit}}") != commit:
        raise ValueError("Release tag targets a different commit")
    if git(root, "rev-parse", "refs/remotes/origin/main") != commit:
        raise ValueError("Release commit must match the fetched main head")
    return version


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tag")
    parser.add_argument("--commit")
    parser.add_argument("--notes-output", type=Path)
    args = parser.parse_args()
    if bool(args.tag) != bool(args.commit):
        parser.error("--tag and --commit must be supplied together")
    version = check_tag(ROOT, args.tag, args.commit) if args.tag else read_version(ROOT)
    notes = release_notes(ROOT, version)
    if args.notes_output:
        args.notes_output.parent.mkdir(parents=True, exist_ok=True)
        args.notes_output.write_text(notes)
    print(json.dumps({"version": version, "tag": args.tag, "source_commit": args.commit}))


if __name__ == "__main__":
    main()
