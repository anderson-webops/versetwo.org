"""Release-policy regressions using disposable local Git repositories."""

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import subprocess
import sys
import tarfile
import tempfile
import threading
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build_site import build
from check_live import check
from check_release import check_tag, read_version, release_notes
from smoke_site import smoke


class ReleaseTests(unittest.TestCase):
    def setUp(self):
        run = ROOT / ".ai-work" / "runs" / "release-tests"
        run.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=run)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.git("init", "--initial-branch=main")
        self.git("config", "user.name", "Release test")
        self.git("config", "user.email", "test@example.invalid")
        self.git("config", "core.hooksPath", "/dev/null")
        self.git("-c", "commit.gpgsign=false", "commit", "--allow-empty", "-m", "Base fixture")
        (self.root / "VERSION").write_text("0.1.1\n")
        (self.root / "CHANGELOG.md").write_text("# Releases\n\n## v0.1.1\n\nFixture release.\n\n## v0.1.0\n\nOlder release.\n")
        self.git("add", "VERSION", "CHANGELOG.md")
        self.git("-c", "commit.gpgsign=false", "commit", "-m", "Release fixture")
        self.commit = self.git("rev-parse", "HEAD")
        self.git("update-ref", "refs/remotes/origin/main", self.commit)
        self.git("-c", "tag.gpgsign=false", "tag", "-a", "v0.1.1", "-m", "Fixture release")

    def git(self, *args):
        return subprocess.check_output(["git", *args], cwd=self.root, text=True, stderr=subprocess.PIPE).strip()

    def test_exact_annotated_main_release_is_accepted(self):
        self.assertEqual(check_tag(self.root, "v0.1.1", self.commit), "0.1.1")
        self.assertEqual(release_notes(self.root, "0.1.1"), "Fixture release.\n")

    def test_wrong_version_tag_fails(self):
        with self.assertRaisesRegex(ValueError, "exactly match VERSION"):
            check_tag(self.root, "v0.1.0", self.commit)

    def test_lightweight_tag_fails(self):
        (self.root / "VERSION").write_text("0.1.2\n")
        (self.root / "CHANGELOG.md").write_text("## v0.1.2\n\nNew fixture.\n")
        self.git("add", "VERSION", "CHANGELOG.md")
        self.git("-c", "commit.gpgsign=false", "commit", "-m", "Next fixture")
        commit = self.git("rev-parse", "HEAD")
        self.git("-c", "tag.gpgsign=false", "tag", "v0.1.2")
        with self.assertRaisesRegex(ValueError, "annotated tag"):
            check_tag(self.root, "v0.1.2", commit)

    def test_tag_pointing_to_another_commit_fails(self):
        self.git("-c", "commit.gpgsign=false", "commit", "--allow-empty", "-m", "Later fixture")
        with self.assertRaisesRegex(ValueError, "different commit"):
            check_tag(self.root, "v0.1.1", self.git("rev-parse", "HEAD"))

    def test_release_not_at_main_head_fails(self):
        self.git("update-ref", "refs/remotes/origin/main", "HEAD^")
        with self.assertRaisesRegex(ValueError, "fetched main head"):
            check_tag(self.root, "v0.1.1", self.commit)

    def test_dirty_or_untracked_files_fail(self):
        (self.root / "untracked.txt").write_text("Uncommitted fixture")
        with self.assertRaisesRegex(ValueError, "clean checkout"):
            check_tag(self.root, "v0.1.1", self.commit)

    def test_missing_changelog_section_fails(self):
        with self.assertRaisesRegex(ValueError, "one section"):
            release_notes(self.root, "0.9.9")

    def test_invalid_version_fails(self):
        (self.root / "VERSION").write_text("01.1.1\n")
        with self.assertRaisesRegex(ValueError, "semantic version"):
            read_version(self.root)


class StaticArtifactSmokeTests(unittest.TestCase):
    def test_unpacked_artifact_serves_exact_bytes_and_real_404_without_source(self):
        run = ROOT / ".ai-work" / "runs" / "release-tests"
        run.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=run) as directory:
            isolated = Path(directory)
            commit = "a" * 40
            version = read_version(ROOT)
            archive = build(ROOT / "prototype", ROOT / "deployment-contract.json", isolated / "build", commit, f"v{version}", version)
            result = smoke(archive, commit, version)
            self.assertEqual(result["public_files"], 22)
            self.assertEqual(result["isolated_http"], "pass")
            self.assertEqual(result["missing_and_private_paths"], "404")



class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_args):
        pass


class LiveCheckTests(unittest.TestCase):
    def test_live_check_accepts_exact_files_and_flags_changed_bytes(self):
        run = ROOT / ".ai-work" / "runs" / "release-tests"
        run.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=run) as directory:
            isolated = Path(directory)
            commit = "b" * 40
            version = read_version(ROOT)
            archive = build(ROOT / "prototype", ROOT / "deployment-contract.json", isolated / "build", commit, f"v{version}", version)
            with tarfile.open(archive, "r:gz") as tar:
                tar.extractall(isolated / "served", filter="data")
            manifest = json.loads((isolated / "served" / "manifest.json").read_text())
            public = isolated / "served" / "public"
            server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(public)))
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            try:
                origin = f"http://127.0.0.1:{server.server_port}"
                self.assertTrue(check(origin, manifest, ("ipv4",))["ok"])
                (public / "style.css").write_text("/* changed on the host */")
                result = check(origin, manifest, ("ipv4",))
                self.assertFalse(result["ok"])
                self.assertEqual(result["families"]["ipv4"]["mismatched"], ["style.css: bytes differ"])
            finally:
                server.shutdown()
                server.server_close()
                thread.join(timeout=5)


if __name__ == "__main__":
    unittest.main()
