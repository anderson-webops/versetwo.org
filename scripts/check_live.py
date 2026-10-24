"""Read-only check that a public origin serves an accepted release's exact files.

Fetches every public file named in a release manifest over each requested
address family and compares SHA-256 digests. The served identity files are
compared by commit and version; the host may record its own ref. Nothing is
changed on the host.
"""

import argparse
import hashlib
import http.client
import json
from pathlib import Path
import socket
import ssl
from urllib.parse import urlsplit

IDENTITY_FILES = ("deployment.json", "release.json")
FAMILIES = {"ipv4": socket.AF_INET, "ipv6": socket.AF_INET6}


def fetch(origin, path, family, timeout=10):
    url = urlsplit(origin)
    secure = url.scheme == "https"
    port = url.port or (443 if secure else 80)
    address = socket.getaddrinfo(url.hostname, port, FAMILIES[family], socket.SOCK_STREAM)[0][4]
    sock = socket.create_connection(address[:2], timeout=timeout)
    if secure:
        sock = ssl.create_default_context().wrap_socket(sock, server_hostname=url.hostname)
    connection = http.client.HTTPConnection(url.hostname, port, timeout=timeout)
    connection.sock = sock
    try:
        connection.request("GET", "/" + path, headers={"Host": url.netloc, "Cache-Control": "no-cache"})
        response = connection.getresponse()
        return response.status, response.read()
    finally:
        connection.close()


def check(origin, manifest, families=("ipv4", "ipv6")):
    expected_commit = manifest["source"]["commit"]
    expected_version = manifest.get("version")
    public = {name[len("public/"):]: item for name, item in manifest["files"].items() if name.startswith("public/")}
    report = {"origin": origin, "commit": expected_commit, "version": expected_version, "families": {}}
    for family in families:
        mismatched, identity_ref = [], None
        for name, item in sorted(public.items()):
            status, body = fetch(origin, name, family)
            if status != 200:
                mismatched.append(f"{name}: HTTP {status}")
            elif name in IDENTITY_FILES:
                identity = json.loads(body)
                if identity.get("commit") != expected_commit or identity.get("version") != expected_version:
                    mismatched.append(f"{name}: serves {identity.get('commit')} / {identity.get('version')}")
                identity_ref = identity.get("ref", identity_ref)
            elif hashlib.sha256(body).hexdigest() != item["sha256"]:
                mismatched.append(f"{name}: bytes differ")
        status, _ = fetch(origin, "__versetwo-missing__", family)
        if status != 404:
            mismatched.append(f"missing path: HTTP {status}")
        report["families"][family] = {"files": len(public), "served_ref": identity_ref, "mismatched": mismatched}
    report["ok"] = not any(result["mismatched"] for result in report["families"].values())
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path, help="manifest.json from the accepted release")
    parser.add_argument("--origin", default="https://versetwo.org")
    parser.add_argument("--family", choices=sorted(FAMILIES), action="append", help="default: both")
    args = parser.parse_args()
    report = check(args.origin, json.loads(args.manifest.read_text()), tuple(args.family or ("ipv4", "ipv6")))
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report["ok"] else 1)


if __name__ == "__main__":
    main()
