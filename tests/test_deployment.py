"""Regressions for accidental source publication and corrupted deployable files."""

import hashlib
from pathlib import Path
import sys
import tarfile
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build_site import ARCHIVE_NAME, PUBLIC_FILES, build
from verify_site import verify

COMMIT = "a" * 40


class DeploymentTests(unittest.TestCase):
    def setUp(self):
        run = ROOT / ".ai-work" / "runs" / "20261017-github-deployment"
        run.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=run)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "prototype"
        self.source.mkdir()
        for name in PUBLIC_FILES:
            (self.source / name).write_bytes((ROOT / "prototype" / name).read_bytes())

    def build(self, destination="build"):
        return build(self.source, ROOT / "deployment-contract.json", self.root / destination, COMMIT, "main")

    def test_exact_archive_is_reproducible_and_accepted(self):
        first, second = self.build("one"), self.build("two")
        self.assertEqual(first.read_bytes(), second.read_bytes())
        self.assertEqual(verify(first, COMMIT)["public_files"], 13)

    def test_private_or_unknown_material_is_not_published(self):
        (self.source / "private-notes.md").write_text("Private draft, not a site asset")
        with tarfile.open(self.build(), "r:gz") as tar:
            self.assertFalse(any("private-notes" in name for name in tar.getnames()))

    def test_missing_entrypoint_fails(self):
        (self.source / "index.html").unlink()
        with self.assertRaisesRegex(ValueError, "Missing or non-regular"):
            self.build()

    def test_symlink_asset_fails(self):
        path = self.source / "style.css"
        path.unlink()
        path.symlink_to(ROOT / "prototype" / "style.css")
        with self.assertRaisesRegex(ValueError, "Missing or non-regular"):
            self.build()

    def test_corrupt_archive_fails(self):
        archive = self.build()
        archive.write_bytes(archive.read_bytes() + b"changed")
        with self.assertRaisesRegex(ValueError, "checksum mismatch"):
            verify(archive, COMMIT)

    def test_wrong_source_commit_fails(self):
        with self.assertRaisesRegex(ValueError, "Wrong source identity"):
            verify(self.build(), "b" * 40)

    def test_missing_required_member_fails_even_with_updated_checksum(self):
        archive = self.build()
        with tarfile.open(archive, "r:gz") as tar:
            members = [(entry, tar.extractfile(entry).read()) for entry in tar if entry.name != "public/index.html"]
        import io
        with tarfile.open(archive, "w:gz") as tar:
            for entry, data in members:
                tar.addfile(entry, io.BytesIO(data))
        archive.with_name(ARCHIVE_NAME + ".sha256").write_text(f"{hashlib.sha256(archive.read_bytes()).hexdigest()}  {ARCHIVE_NAME}\n")
        with self.assertRaisesRegex(ValueError, "publication allowlist"):
            verify(archive, COMMIT)


if __name__ == "__main__":
    unittest.main()
