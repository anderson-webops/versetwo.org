"""Serve only an independently accepted unpacked artifact and check its bytes."""

import argparse
from functools import partial
import hashlib
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import tarfile
import tempfile
import threading
from urllib.error import HTTPError
from urllib.request import urlopen

from verify_site import EXPECTED_PUBLIC, verify


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_args):
        pass


def smoke(archive, expected_commit, expected_version=None):
    result = verify(archive, expected_commit, expected_version)
    with tempfile.TemporaryDirectory(dir=archive.parent) as directory:
        isolated = Path(directory)
        with tarfile.open(archive, "r:gz") as tar:
            tar.extractall(isolated, filter="data")
        public = isolated / "public"
        manifest = json.loads((isolated / "manifest.json").read_text())
        server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(public)))
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            url = f"http://127.0.0.1:{server.server_port}"
            for name in EXPECTED_PUBLIC:
                with urlopen(f"{url}/{name}", timeout=5) as response:
                    digest = hashlib.sha256(response.read()).hexdigest()
                    if response.status != 200 or digest != manifest["files"][f"public/{name}"]["sha256"]:
                        raise ValueError(f"Served artifact bytes differ: {name}")
            for name in ("__missing__", "VERSION", "manifest.json", "source-packet/original-research-brief.md"):
                try:
                    with urlopen(f"{url}/{name}", timeout=5):
                        raise ValueError(f"Private or absent path was served: {name}")
                except HTTPError as error:
                    if error.code != 404:
                        raise ValueError(f"Expected a real 404 for {name}") from error
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=5)
    return {**result, "isolated_http": "pass", "missing_and_private_paths": "404"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--version")
    args = parser.parse_args()
    print(json.dumps(smoke(args.archive, args.commit, args.version), indent=2))


if __name__ == "__main__":
    main()
