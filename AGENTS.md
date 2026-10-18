# Next Verse repository guidance

Shared Sites policy (`../AGENTS.md` in the Sites checkout) applies. Keep shared policies there; this file records repository-specific rules and standalone safety essentials.

## Project and preserved evidence

- `scripts/build_prototype.py` and its four content modules generate the eight pages in `prototype/`. Change generators, then regenerate; do not hand-edit generated pages.
- Preserve the exact `source-packet/` bytes. `scripts/package_review.py` checks the six original source hashes. Read the handoff, GOAL, exact original brief and preserved sources before substantive content changes. Keep checked evidence distinct from imported claims and untested outcomes.
- Jacob prefers Next Verse; versetwo.org is the repository/domain candidate. Do not silently select Verse Two or imply an artist partnership.
- Keep website wording useful and minimal. Do not put development status or naming decisions in the interface. Preserve accessibility, evidence limits, attribution and necessary disclosures.
- Do not collect youth data, recruit minors, send outreach or purchase domains without separate explicit authorization. Public source/release delivery is authorized; this does not authorize production activation.

## Checks and packaging

- Use the Python 3.13 family declared in `.python-version`. The site and CI have no third-party Python dependencies or JavaScript build toolchain.
- Before committing run `python3 scripts/build_prototype.py`, `python3 scripts/check_static.py`, `python3 scripts/check_release.py`, `python3 -m unittest discover -s tests -v`, and `git diff --check`. Inspect generated changes and source hashes. Use `actionlint` and guarded `codex-zizmor` for workflow edits; guarded `codex-ruff-check` for Python edits. Stop a guarded tool on version drift, report its limit and continue unaffected native checks.
- PDFs are checked-in assets. Content/print changes require WeasyPrint 70.0 with tagged output and file/data-only resources, matching copies in `prototype/` and `output/pdf/`, `scripts/check_print_layout.py`, and visual PDF review. Browser/device/screen-reader gaps must remain documented.
- Only `prototype/`'s independent publication allowlist goes into the deployment archive. The full review ZIP, research exports and outreach drafts must never become the server document root. `scripts/verify_site.py` is independent of the builder's inventory.
- Build from a clean committed checkout using `python3 scripts/build_site.py --commit FULL_SHA --ref REF`; accept the exact result with `python3 scripts/verify_site.py build/versetwo.org-static.tar.gz --commit FULL_SHA`. Tests also serve the unpacked artifact in isolation and check exact bytes and real 404s.

## Commit, tag and release

- Deliver coherent validated work directly to `main`, then push. Use a PR only if requested or branch protection requires one. Do not sweep unrelated or explicitly local edits into a commit. Use an isolated clean checkout when needed.
- `VERSION` is the canonical application version; `CHANGELOG.md` supplies the release notes. Use patch versions for compatible content, security and packaging changes, minor versions for new capabilities, and a major version for an intentional incompatible release. Increment only for a release-worthy deployable state, not every commit.
- For a deployable milestone, align VERSION and the changelog, commit and push main, then create an annotated `vX.Y.Z` tag on that exact accepted main commit. Confirm main CI, run `scripts/check_release.py --tag vX.Y.Z --commit FULL_SHA`, and push the tag in the same work session. Never force-push or move an existing published tag without explicit authorization for that exact rewrite.
- Tag CI repeats all checks, verifies the version/annotated tag/source/main relationship, then independently accepts and smoke-tests the artifact. The release job uses those exact CI files, checks them again, creates a draft, uploads the four deployment files, downloads/verifies all four, then publishes the release. Only that job has `contents: write`; branch/PR validation is read-only.
- Confirm the tag's peeled SHA, successful tag workflow, published release and uploaded asset bytes. Do not overwrite assets on a published release. A failed draft may be resumed with the original accepted files after inspection; a new source change needs a new version/tag. Follow `docs/releasing.md` for the concrete sequence and failure recovery.
- Documentation-only, formatting-only and other non-deployable housekeeping changes are committed/pushed without inventing an application release. Existing v0.1.0 remains immutable.

## Source/host boundary

- Never SSH, SCP, SFTP, tunnel to, configure access to, or administer production from this checkout. Never activate a release or change live services, configuration, data or release pointers. Protected server-side automation owns deployment.
- Preserve existing IPv4/IPv6 and all A/AAAA records. DNS, certificates, routing and host ownership remain operator-controlled. The static host contract is a requirement, not evidence of an installed compatible adapter.
- Report source delivery, CI acceptance, GitHub publication, host acceptance and independently verified live identity separately. A tag or published release does not prove production activation.
- Keep local AI material under indexed, locally excluded `.ai-work/`; inspect worktree state before cleanup. Never discard another task's uncommitted work. Run the available secret checks, preserve hooks and stop on real findings; GitGuardian quota/auth/service failure alone is not a delivery blocker.
