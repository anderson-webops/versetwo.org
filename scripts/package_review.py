"""Build the small offline copy and full review ZIP from explicit inputs."""

import hashlib
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


root = Path(__file__).resolve().parents[1]
expected_sources = {
    "deep-research-report.md": "36b5ec9e3cd766566fb5846a72a92cca8fa6e41719c4291c1fe8686d1271b2d1",
    "kickoff-brief.md": "154ff0012684f02626da3498838fbe4b19615358eec510a43bae81a24e17584b",
    "conversation-source-notes.md": "a89e8b3c311f159cd23ff46002fae32750b56edec267675234f9616dd9590ef8",
    "deep-research-youth-2026-10-03.md": "67aebf31dbb2f17971b8d923e4c4112857388c8c53b34bbba905ea731075aa58",
    "youth-deep-research-README.md": "51f9bf5a13395fd59154ad060a844f0d73e5354359bf6e2eeab8799b42cddce2",
    "original-research-brief.md": "6155d48b31345e6cc1fab29f949f0727bac7dc9c244415fc55de3e50ea05b119",
}
for name, expected in expected_sources.items():
    actual = hashlib.sha256((root / "source-packet" / name).read_bytes()).hexdigest()
    if actual != expected:
        raise ValueError(f"Original source changed: {name}")


def inspect_archive(path, expected_members):
    with ZipFile(path) as archive:
        if archive.testzip() is not None:
            raise ValueError(f"Archive CRC failed: {path.name}")
        members = archive.namelist()
        if set(members) != set(expected_members):
            raise ValueError(f"Archive members differ: {path.name}")
        for member, original in expected_members.items():
            if archive.read(member) != original.read_bytes():
                raise ValueError(f"Archive bytes differ: {member}")
    return {
        "filename": path.name,
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "files": len(members),
        "crc": "pass",
        "member_bytes_match_source": "pass",
    }


offline = root / "music-practice-offline.zip"
prototype_files = sorted(
    path for path in (root / "prototype").iterdir()
    if path.is_file() and path.suffix in (".html", ".css", ".svg", ".pdf")
)
with ZipFile(offline, "w", ZIP_DEFLATED) as archive:
    for path in prototype_files:
        archive.write(path, path.name)
    archive.write(root / "OFFLINE.txt", "START-HERE.txt")
offline_members = {path.name: path for path in prototype_files}
offline_members["START-HERE.txt"] = root / "OFFLINE.txt"
for name in ("music-practice-packet.pdf", "facilitator-outline.pdf"):
    if (root / "prototype" / name).read_bytes() != (root / "output/pdf" / name).read_bytes():
        raise ValueError(f"PDF copies differ: {name}")

review = root / "youth-music-learning-review.zip"
review_members = {}
with ZipFile(review, "w", ZIP_DEFLATED) as archive:
    for name in ("next-verse-work-handoff.md", "GOAL.md", "README.md", "REVIEW.md", "OFFLINE.txt", "AGENTS.md", "VERSION", "CHANGELOG.md", ".gitattributes", ".gitignore", ".python-version", "deployment-contract.json", offline.name):
        archive.write(root / name, name)
        review_members[name] = root / name
    for folder in (".github", "docs", "prototype", "scripts", "source-packet", "tests", "output/pdf"):
        for path in sorted((root / folder).rglob("*")):
            if not path.is_file() or path.suffix == ".pyc":
                continue
            if path.name in ("library-deliverable.md", "package-checks.json"):
                continue
            archive.write(path, path.relative_to(root))
            review_members[str(path.relative_to(root))] = path

report = {
    "original_source_hashes": "pass",
    "pdf_copies_identical": "pass",
    "offline": inspect_archive(offline, offline_members),
    "review": inspect_archive(review, review_members),
}
(root / "docs" / "package-checks.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
