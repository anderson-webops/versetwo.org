# GitHub source and existing web-server deployment

Configured October 17, 2026 for `anderson-webops/versetwo.org`. The repository is private. Jacob selected his existing web server as the hosting target. GitHub Pages, containers, a Node service and an application database are not needed for this static site.

## GitHub build

The `Validate and package static site` workflow runs on main-branch pushes, pull requests and manual requests. It:

1. Regenerates the eight HTML pages and rejects uncommitted differences in the tracked website.
2. Checks local links, fragments, page structure, accessibility basics, privacy constraints and the original budget calculation.
3. Runs seven deployment-boundary and integrity regression tests.
4. Packages the exact source commit and independently verifies the resulting archive.
5. Uploads an artifact named `versetwo-static-site-<full commit SHA>`, retained for 30 days.

The workflow uses read-only repository permissions and verified, full-SHA pins for official actions. It installs Python 3.13, declared in `.python-version`, and no third-party Python packages. It has no server credentials or deployment command. Source delivery, an accepted build and production activation are separate events.

Repository attributes enforce LF line endings for generated code and pages while disabling conversion for the preserved source packet and binary files. Intentional Markdown hard-break spaces in the unchanged research exports are excluded from whitespace warnings; their exact content hashes remain required by the review-package check.

## Deployment files

The workflow artifact contains:

- `versetwo.org-static.tar.gz`
- `versetwo.org-static.tar.gz.sha256`
- `manifest.json`
- `deployment-contract.json`

The tar archive contains `public/`, plus its manifest and contract. Only the eight HTML pages, CSS, favicon, two PDFs and generated `deployment.json` are included in `public/`. All site links are relative, allowing the existing host to choose its URL path. There is no CNAME or DNS configuration in this repository.

Research exports, source code, internal notes, outreach drafts, Git metadata, caches and review ZIPs are not public assets. The independently maintained verifier rejects unexpected archive members, missing pages, symlinks, checksum failures and a different source commit. Serve only the archive's `public/` directory, never the repository root or the full review bundle.

The gzip/tar metadata is normalized, so the same inputs produce identical artifact bytes. Each file's size and SHA-256 are recorded in the manifest. The sidecar checksum covers the exact archive. These integrity checks do not replace obtaining the package from the trusted GitHub repository.

## Reproduce locally

Run from a clean checkout of the commit to package:

```sh
python3 scripts/build_prototype.py
git diff --exit-code -- prototype
python3 scripts/check_static.py
python3 -m unittest discover -s tests -v
git rev-parse HEAD
```

Pass that full SHA to the build and acceptance commands:

```sh
python3 scripts/build_site.py --commit FULL_COMMIT_SHA --ref main
python3 scripts/verify_site.py build/versetwo.org-static.tar.gz --commit FULL_COMMIT_SHA
```

The builder checks that the requested SHA matches HEAD and that the tracked deployment inputs have no uncommitted changes. The verifier works from the archive and sidecar alone; it does not need the source checkout or Python dependencies. Tests use disposable fixtures inside the locally excluded `.ai-work/` area.

PDFs are checked-in static assets. CI does not re-render them, avoiding an unnecessary renderer installation; visual and print checks must still accompany changes that affect print content. See `validation.md` for their current scope.

## Protected server handoff

The versioned `deployment-contract.json` declares a static-directory host capability, its public document root and served identity endpoint. No installed host adapter has been inspected or claimed compatible. The protected server-side system or operator must onboard this new repository using the host's existing paths, ownership, access controls and release policy.

The host should obtain the chosen exact artifact from the private repository, verify its expected source SHA and archive checksum, accept the independent file inventory, and stage it in a new release directory. Existing static hosting can then serve the staged `public/` tree. This is a multi-page site: resolve real files and return 404 for absent paths rather than using an SPA fallback. Standard HTML/CSS/SVG/PDF MIME handling is sufficient.

Activation belongs to the protected server-side system. Preserve the previous accepted artifact and release pointer for rollback; validate the staged bytes after copying and switch atomically only after host checks pass. Do not rebuild the rollback release. Retain accepted artifacts on the server or in an approved immutable release before GitHub's temporary workflow-artifact retention expires.

After activation, compare the full commit in the served `deployment.json` with the chosen manifest, and compare served HTML/CSS/PDF bytes against the manifest. Check normal navigation and both retained IPv4 and IPv6 paths. HTML, `deployment.json` and the unversioned `style.css` should revalidate rather than receive long immutable cache lifetimes.

Production paths, certificates, DNS, ports and ownership remain server-controlled. Do not alter existing A or AAAA records. No production shell access, live service/configuration change, release publication, tag or deployment is performed by this setup. A repository push does not establish that the server has activated the site.

## Local verification limits

The native checks and seven regression tests pass locally, and `actionlint` accepts the workflow syntax. The guarded Zizmor wrapper reports approved 1.29.0 versus installed 1.31.1; the guarded Ruff wrapper reports approved 0.17.0 versus an unavailable/unknown version. Those checks stopped as required by the local preflight policy. No unguarded bypass or successful security/Python lint result is claimed.

The configured global Git hooks delegate local hooks but have GitGuardian scanning disabled in their current files. The explicit local secret scan is recorded with the final verification result. These tool limits do not establish a failed static artifact or a successful production deployment.
