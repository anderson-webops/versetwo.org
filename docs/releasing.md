# Source delivery and releases

This repository follows the shared Sites policy: commit and push coherent validated work to `main`; create an annotated semantic-version tag and corresponding GitHub release for each release-worthy deployable milestone. Do not tag every commit or invent releases for documentation-only/formatting-only housekeeping. No force pushes, moved published tags, or overwritten published release assets.

`VERSION` is the canonical application version. `CHANGELOG.md` contains one `## vX.Y.Z` section per release. Compatible content, security and packaging changes normally increment the patch version; new capabilities increment minor, intentional incompatibilities major. The original review-bundle “version 7” is a historical document revision, not the application's release version. `v0.1.0` remains unchanged at `71857ec7b5fb16f4dfd85bb6976ddf5195a92492`.

## Validate and integrate

Inspect the working tree first. Preserve unrelated and explicitly local changes; use a registered, indexed worktree under `.ai-work/worktrees/` if a clean release checkout is needed. Do not claim an artifact represents HEAD while packaging uncommitted files.

For a deployable change, update VERSION and the matching changelog section alongside implementation, then run:

```sh
python3 scripts/build_prototype.py
python3 scripts/check_static.py
python3 scripts/check_release.py
python3 -m unittest discover -s tests -v
git diff --check
```

Also run applicable workflow/Python/secret checks and inspect outgoing files. Print changes require tagged-PDF rebuild, geometry/visual review and identical PDF copies; UI changes need proportionate browser/accessibility checks. Preserve original source-packet hashes with `scripts/package_review.py` when preparing review bundles. It rewrites the local package report, so inspect that diff before staging. Existing evidence limits remain in `validation.md`.

Stage only the intended coherent changes, commit and push `main`. Wait for the exact commit's **Validate and package static site** run to pass, not an older green run. Documentation-only follow-ups do not require a new version/tag/release.

## Tag and publish

From a clean checkout at the accepted main commit, fetch current branch/tag identity. Replace the example version and full SHA below with the reviewed values:

```sh
git fetch origin main --tags
git rev-parse HEAD
git rev-parse origin/main
git tag -a vX.Y.Z -m "vX.Y.Z: concise milestone"
python3 scripts/check_release.py --tag vX.Y.Z --commit FULL_COMMIT_SHA
git push origin refs/tags/vX.Y.Z
```

Do not use `git tag -f`, `git push --force`, or automatic tag creation by `gh release create`. The checker requires exact VERSION/changelog/tag agreement, an annotated tag pointing to HEAD, a clean tree, and HEAD matching fetched `origin/main`.

Tag pushes repeat regeneration, static checks, release checks, all regression tests and isolated artifact HTTP smoke checks. They build the exact tagged source. Only after validation succeeds can the release job use its scoped write permission. Branch/PR validation has read-only permissions; the job is not available to pull requests or manual branch runs.

The release job downloads this run's accepted package rather than rebuilding it, verifies commit/version/tag and external manifest/contract bytes, creates a draft, and attaches exactly:

- `versetwo.org-static.tar.gz`
- `versetwo.org-static.tar.gz.sha256`
- `manifest.json`
- `deployment-contract.json`

It downloads all four uploads, compares their bytes with the accepted CI files, independently verifies the downloaded archive, then publishes. VERSION appears in the manifest and served `deployment.json`; it is not visitor-facing page copy. The verifier's `--version X.Y.Z` also requires the matching `vX.Y.Z` source ref. Without that option it can still accept the legacy v0.1.0 archive by its exact source SHA.

## Verify and recover

Confirm the tag is annotated and peels to the intended commit, the tag run passes, the release is published (not draft), and all four assets are present. Download them and run:

```sh
gh release download vX.Y.Z --repo anderson-webops/versetwo.org --dir build/release-check
python3 scripts/verify_site.py build/release-check/versetwo.org-static.tar.gz \
  --commit FULL_COMMIT_SHA --version X.Y.Z
tar -xOf build/release-check/versetwo.org-static.tar.gz manifest.json | cmp - build/release-check/manifest.json
tar -xOf build/release-check/versetwo.org-static.tar.gz deployment-contract.json | cmp - build/release-check/deployment-contract.json
```

The automation refuses to overwrite an existing release or asset. On failure, inspect the exact run, tag, release state and uploaded bytes first. A draft can be resumed manually using the original accepted artifact: compare any existing assets, upload only missing files without `--clobber`, re-download and verify every file, then publish the draft. Never publish a partial or unverified draft. A source correction requires a new version and tag; never move the failed tag. A GitHub API quota/network interruption is not evidence of publication or a reason to alter deployment gates.

## Deployment boundary

A published release means source/artifact delivery, not host acceptance or a live website. The protected server-side system must accept the contract, verify the exact artifact, stage only `public/`, retain rollback and activate according to the existing host policy. No compatible installed host adapter has been verified. Do not access or administer production from this source workspace, and do not change A/AAAA records. See [deployment.md](deployment.md) for the host handoff and independent live-identity requirements.
