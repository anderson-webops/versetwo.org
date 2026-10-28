# Next Verse repository guidance

## Standing Dependency Completion Policy

Treat dependency remediation as part of completing authorized work on this
site, not as an optional follow-up. Proactively resolve vulnerabilities,
compatibility problems, broken installations and lockfile issues. Cover direct
and transitive dependencies, production and development dependencies,
workspaces and root-level tools. Do not dismiss findings because they are
pre-existing or development-only.

Before creating a release tag or publishing a release, require a clean locked
installation for every applicable dependency graph, zero known dependency
vulnerabilities in both full and production audits, and all applicable project
checks. An unavailable or incomplete audit is not a clean result. Use supported
upgrades, replacements or maintainable patches that preserve functionality.
Do not silence findings, weaken checks or force incompatible versions merely
to obtain a passing result.

Intermediate commits may capture coherent progress. Commit and push validated
work through this site's authorized delivery process, and complete meaningful
releases rather than stopping after reporting fixable dependency blockers.
Documentation-only housekeeping does not require an application release.

Preserve unrelated work, coordinate with other active chats, and retain existing
security, approval and production-access boundaries. Existing maintenance pauses
and repository exclusions remain in force; this policy does not expand access
or authorize otherwise excluded work. If a genuine blocker prevents completion,
preserve progress and report the exact blocker and remaining work. Distinguish
a published release from verified live deployment.

Treat this as a standing instruction for this site.

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

- Commit coherent validated increments frequently and push completed work directly to `main`. Use a PR only if requested or branch protection requires one. Preserve unrelated or separately scoped edits, using an isolated clean checkout when needed. Finish deployable work through the existing tag-CI release publication workflow and follow protected deployment with read-only public acceptance checks or report the exact remaining blocker.
- `VERSION` is the canonical application version; `CHANGELOG.md` supplies the release notes. Use patch versions for compatible content, security and packaging changes, minor versions for new capabilities, and a major version for an intentional incompatible release. Increment only for a release-worthy deployable state, not every commit.
- For a deployable milestone, align VERSION and the changelog, commit and push main, then create an annotated `vX.Y.Z` tag on that exact accepted main commit. Confirm main CI, run `scripts/check_release.py --tag vX.Y.Z --commit FULL_SHA`, and push the tag in the same work session. Never force-push or move an existing published tag without explicit authorization for that exact rewrite.
- Tag CI repeats all checks, verifies the version/annotated tag/source/main relationship, then independently accepts and smoke-tests the artifact. The release job uses those exact CI files, checks them again, creates a draft, uploads the four deployment files, downloads/verifies all four, then publishes the release. Only that job has `contents: write`; branch/PR validation is read-only.
- Confirm the tag's peeled SHA, successful tag workflow, published release and uploaded asset bytes. Do not overwrite assets on a published release. A failed draft may be resumed with the original accepted files after inspection; a new source change needs a new version/tag. Follow `docs/releasing.md` for the concrete sequence and failure recovery.
- Documentation-only, formatting-only and other non-deployable housekeeping changes are committed/pushed without inventing an application release. Existing v0.1.0 remains immutable.

## Source/host boundary

- Never SSH, SCP, SFTP, tunnel to, configure access to, or administer production from this checkout. Never activate a release or change live services, configuration, data or release pointers. Protected server-side automation owns deployment.
- Preserve existing IPv4/IPv6 and all A/AAAA records. DNS, certificates, routing and host ownership remain operator-controlled. The static host contract is a requirement, not evidence of an installed compatible adapter.
- Report source delivery, CI acceptance, GitHub publication, host acceptance and independently verified live identity separately. A tag or published release does not prove production activation. Use the read-only `python3 scripts/check_live.py <release manifest.json>` to compare the public site over IPv4 and IPv6.
- Keep local AI material under indexed, locally excluded `.ai-work/`; inspect worktree state before cleanup. Never discard another task's uncommitted work. Run the available secret checks, preserve hooks and stop on real findings; GitGuardian quota/auth/service failure alone is not a delivery blocker.
