# Youth music and learning

October 20 copy cleanup: removed repeated framing, profile takeaways, generic onboarding and interface commentary across all eight pages and both downloads. The ten factual artist accounts, seven activities and essential disclosures remain. Jacob authorized including the earlier local copy review in the normal source release. Verification is recorded in [Validation](docs/validation.md).

GitHub deployment setup: the public repository is [anderson-webops/versetwo.org](https://github.com/anderson-webops/versetwo.org). Pushes run validation and build a checked static deployment package for the existing web server. Read [deployment.md](docs/deployment.md) for the artifact, exact-source checks and protected server handoff. This does not activate the public website.

October 17 update: Jacob authorized public repository visibility. The [CI rerun](https://github.com/anderson-webops/versetwo.org/actions/runs/39030144180) passed after that change, including all seven deployment tests and the artifact build/upload. The earlier private-repository billing failure is historical; no billing settings were changed.

October 16 update: the local site now has ten sourced artist stories and seven original activities. Added Eminem, Rakim, Lupe Fiasco and Doechii, plus a word-and-sound exercise. [Research and source ledger](docs/artist-learning-research-2026-10-16.md) records what was checked and what remains uncertain. The older October 9 handoff describes version 7; this update supersedes its story/activity/print counts.

For a receiving Work chat, start with [next-verse-work-handoff.md](next-verse-work-handoff.md), including its ready-to-paste continuation prompt. The complete review ZIP includes all preserved sources, editable prototype, print materials and review documents. Recent naming/preview exchanges are in [conversation-update-2026-10-09.md](docs/conversation-update-2026-10-09.md). A supported direct chat transition is unavailable here; no new chat is claimed.

Open [REVIEW.md](REVIEW.md) for the handoff and [prototype/index.html](prototype/index.html) to inspect the local website. No build needed. For the smallest self-contained copy, extract [music-practice-offline.zip](music-practice-offline.zip) and follow START-HERE.txt. The 16-page PDF is available from the print page; the adult guide links a one-page facilitator PDF.

The long-term goal is in [GOAL.md](GOAL.md). Sources and exact original brief are preserved in source-packet; [source manifest](docs/source-manifest.md) records their identities and hashes. [Validation](docs/validation.md) distinguishes passed and untested checks. [Decisions](docs/decisions.md) and [backlog](docs/backlog.md) track future work.

Jacob prefers Next Verse and is considering versetwo.org; the final displayed name/domain pairing remains undecided. The prototype still displays Music / Practice. No affiliation implied and no educational impact proven. Local review only; outreach drafts remain unsent.

Adult reviewers can use [accessibility-review.md](docs/accessibility-review.md) for the remaining browser, device and assistive-technology checks. Rebuild both archives with `python3 scripts/package_review.py`.

Regenerate HTML with `python3 scripts/build_prototype.py` and run `python3 scripts/check_static.py`. Print rendering uses the installed WeasyPrint 70.0 CLI with `--pdf-tags --allowed-protocols file,data`; copy each output PDF into prototype before packaging. Run `scripts/check_print_layout.py` with that CLI’s Python environment for print geometry checks. This is a renderer check, not a browser or screen-reader audit.
