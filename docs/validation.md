# Validation record

## October 24, 2026 one-line page titles (v0.1.6)

Jacob asked for page titles on one line, not two oversized lines. The screen-only rule sizes the title from the screen width and the longest title (11.85em), capped at 2.75rem.

- Browser pane: all nine page titles measure one line at 320, 375, 768 and 1280px (22.6px, 27.1px, then 44px), with no horizontal overflow.
- WeasyPrint 70.0: the packet render is pixel-identical at 60 dpi across all 16 pages to v0.1.5, so the PDFs are unchanged.
- Python 3.15.0: regeneration, static checks, the version check, all 22 regression tests and `git diff --check` pass.

## October 24, 2026 story fact rows (v0.1.5)

Jacob found the "said / recalled" story openings vague. Each story now shows its source and date first, then two or three labeled rows. The wording stays within the BT, RP, MG, GZ, EB, LS, EM, RK, LF and DC register claims. No verbatim artist quotes were added: The Paris Review and Johns Hopkins sources still return HTTP 403 to automated fetching, and the other pages were only read through a summarizer, so exact wording could not be verified.

- After Jacob asked for summaries that get straight to the point, the rows were shortened to the decisive words. A longer narrative would belong only on a separate per-artist page.
- Python 3.15.0 (Homebrew): regeneration, static checks, the version check, all 22 regression tests and `git diff --check` pass. The shell's default `/usr/bin/python3` is 3.9.6, below the declared 3.13. It fails the two artifact tests because `tarfile` lacks the `filter` argument there, so that is an interpreter problem, not a code regression. Use Python 3.13 or newer.
- WeasyPrint 70.0, tagged, file/data resources only: the packet is still 16 Letter pages, `check_print_layout.py` passes, and all pages were visually reviewed. Matching copies are in `prototype/` and `output/pdf/`.
- Browser pane at 1280 and 375px: the rows read as a two-column list on desktop and stacked label/value pairs on phones, with no horizontal overflow. Story numbers no longer split across lines on phones.

## October 24, 2026 main v0.1.6 merged into the redesign branch (branch only)

- This brings in the story fact rows and one-line titles. The fact rows use the redesign's panel styling, and their print rules are copied from main, so `print.html` and both PDFs match main's v0.1.6.
- In the redesign, page titles are sized against the longest title (12.0em), and activity-page titles against the longest activity title (14.2em, inside the panel padding). Apple's system font uses a wider "Text" cut below about 20pt, so small titles need extra room. Browser pane: all 16 titles measure one line at 320, 360, 375, 414, 521, 700, 1000 and 1280px, with no horizontal overflow.
- Python 3.15.0: static checks, the version check, all 24 regression tests and `git diff --check` pass.

## October 23, 2026 main v0.1.4 merged into the redesign branch (branch only)

- Glanceable-information follow-up: activity pages now show a compact 01–07 overview on phones (36×44px links with full accessible names), and the home page groups the ten stories five and five. At 320/375px there is no horizontal overflow, and Practice starts at 1,167px on the home page at 375px. `print.html` is still byte-identical to main's.
- Merge result: 16 pages. Static checks (including both theme palettes, the contents lists and both pager sequences), the version check, all 24 regression tests and `git diff --check` pass.
- `print.html` is byte-identical to main's. The WeasyPrint 70.0 packet render is pixel-identical at 60 dpi across all 16 pages to main's v0.1.3 PDF, and `check_print_layout.py` passes (16 + 1 pages). The checked-in PDFs are main's, unchanged.
- Claude desktop browser pane (Chromium), 320 and 375px: no horizontal overflow on Start, Stories, Practice, Your week, Next step, an activity page or `404.html`. Heights after the phone tightening are recorded in `redesign-2026-10-22.md`. Rewritten story text and the 404 page were reviewed visually. This is not a device, zoom or screen-reader audit.

## October 23, 2026 release identity, not-found page and live check (v0.1.4)

Jacob asked for `/release.json` and other similarly useful pieces from the other anderson-webops sites. A read-only survey of the Marietta Violin, math.avasan, avasan, Audiot and jacobdanderson.net sources and live endpoints found a `release.json` that mirrors `deployment.json`, a `404.html`, and a live smoke check. Those three were adopted. Not adopted:

- `healthz` and `readyz` files. Shared policy says static sites should not add artificial health services.
- `robots.txt` and `sitemap.xml`. The host already serves `robots.txt` with `Disallow: /` and an `x-robots-tag: noindex` header for this site, and the artifact should not contradict that.

- Regeneration adds only `404.html`; the other eight pages are byte-identical. Static checks, the version check, all 22 regression tests (including the new release-identity and live-checker tests) and `git diff --check` pass.
- `check_live.py` against the downloaded v0.1.3 manifest: versetwo.org serves all 13 public files, plus a real 404, identically over IPv4 and IPv6, at commit `81e3dd8` / version 0.1.3. The served ref is the host's `commit/…` form.
- Note: `/404.html` is served as a file. Whether missing paths display it depends on the host's error-page configuration, which this repository does not control.

## October 23, 2026 artist account rewrite (v0.1.3)

Jacob said the artist accounts had the right idea but meandered. All ten were rewritten to lead with the practice and drop the repeated "In a 20XX interview" openers. Dates and publishers remain on the eyebrow and source line. Each paraphrase stays within its evidence-register claim (BT1–2, RP1–2, MG1–2, GZ1, EB1–2, LS1–2, EM1, RK1–2, LF1–2, DC1–2).

- Rechecked the original sources on October 23. CBS: "used to read the dictionary" is Anderson Cooper's phrasing; Eminem's answer was about wanting words at his disposal, so the account no longer states that he read it. The Believer: Rakim said he had played instruments since kindergarten, learned jazz timing from his brother at a community center and brought Coltrane's playing into his delivery. The Paris Review and Johns Hopkins pages returned HTTP 403, so those two accounts were not rechecked. Their wording stays within the previously inspected BT and LF claims.
- WeasyPrint 70.0, tagged, file/data resources only: the packet is still 16 Letter pages, and 411/40 nonempty text boxes are within page bounds. All pages were visually reviewed. Matching copies are in `prototype/` and `output/pdf/`. The facilitator outline is unchanged.

## October 22, 2026 screen redesign proposal (branch only)

Jacob asked for a usability, readability and flow redesign on a dedicated `claude/` branch. The rationale and the open suggestions are in [redesign-2026-10-22.md](redesign-2026-10-22.md). Copy is unchanged apart from the navigation labels.

- Python 3.15.0 local interpreter. `.python-version` declares 3.13; CI uses 3.13. Regeneration, static checks (including the new light/dark contrast, contents-list and pager checks), the version check, all 20 regression tests, `py_compile` and `git diff --check` pass.
- WeasyPrint 70.0, file/data resources only: `print.html` is byte-identical to v0.1.2. The packet render is text-identical and pixel-identical at 60 dpi across all 16 pages. `check_print_layout.py` passes (16 + 1 pages). The checked-in PDFs were not regenerated.
- Claude desktop browser pane (Chromium): all eight pages were checked at 320px for horizontal overflow (none). Home, Stories, Practice, Your week, Next step and For adults were reviewed at 1280px and 375/320px in light and dark schemes. The first Tab reaches a visible skip link. This is not a physical-device, browser-zoom or screen-reader audit.
- The guarded Ruff preflight stopped: it expected 0.17.0 and found an unavailable binary. No lint pass is claimed.
- One page per activity (same branch): the generator produces 15 pages. Static checks, all 22 regression tests (including the new allowlist-completeness and missing-activity-page tests) and the version check pass. `print.html` is still byte-identical, and the packet is still pixel-identical across all 16 pages. All 15 pages were checked at 320 and 375px with no horizontal overflow. Activity pages were reviewed at 1280px and 375px. The legacy `practice.html#word-sound` link lands on its card.

## October 20, 2026 copy cleanup

Jacob requested retaining only substantive content, necessary operation/navigation and essential accessibility/safety/legal text, and explicitly authorized committing, tagging and releasing the combined copy review. This supersedes the local-only delivery restriction in the historical October 17 entry below.

Removed page introductions, motivational profile headlines and takeaways, repeated learning-transfer wrap-ups, redundant instructions and interface/project commentary. Artist pages now contain the dated account, source and relevant activity link. The homepage opens with the artist list. Research about the proposed intervention stays in the preserved research documents rather than framing the visitor interface. The adult guide retains actual facilitation and safeguarding content.

Verification:

- All ten factual artist-account paragraphs and all artist/activity external source URLs are unchanged from the prior local copy review. All seven worked verse examples remain byte-equivalent as visible text. All six original source-packet hashes match. Ten profiles, seven activities and the complete week/support/guide content remain in print.
- Python 3.13.15: regeneration, static semantic/link/ARIA/privacy/budget checks, version/changelog checks, all 20 regression tests and whitespace checks pass. Native validation now checks that the removed repeated profile/transfer framing does not return.
- Playwright CLI 0.1.22 / isolated Chrome: all eight pages return HTTP 200 at 1280, 390 and 320 CSS pixels without horizontal overflow; all eight also fit 1280/320 with a 32px root font (40 layout checks). Reviewed desktop/mobile screenshots of Home, Stories, Practice and Sources. First Tab reaches the skip link and Enter focuses main; all seven disclosures open with Enter and close with Space. Both browser PDF downloads match the final project bytes. Enlarged CSS text is not a physical-device, browser-zoom or screen-reader audit.
- WeasyPrint 70.0, tagged output, file/data resources only: 16 Letter pages in the packet and one in the facilitator outline. All 413/40 nonempty text boxes are within page bounds. All final packet pages and the facilitator were visually reviewed. Print spacing keeps source stories and safeguarding sections together; text size is unchanged. PDF copies in prototype and output/pdf match. Existing unsupported-CSS warnings remain.
- The guarded Ruff preflight stopped on expected 0.17.0 versus an unavailable/unknown version. No lint pass or tool-policy change is claimed. The browser wrapper's CRLF shell entry point was unavailable; the already-cached CLI was used directly. Transient permission-review timeouts were retried through the supported approval mechanism.
- Staged Gitleaks scanning found no secrets. The explicit GitGuardian pre-commit scan was blocked by automatic permission review because it would upload staged contents to an external service without payload/destination-specific authorization. No hosted scan or bypass is claimed; the independent local scan and normal repository hooks remain in place.

Local baseline and check evidence live under `.ai-work/runs/20261020-copy-only/`, including `copy-checks.json`, browser scripts/screenshots and PDF previews. Review/offline archives are rebuilt by the source-preserving package checker. Public source release is separate from protected host acceptance and production activation. No production shell access, DNS mutation, outreach or youth-data collection occurred. Physical-device use, assistive technology, browser printing and intended-user/qualified partner review remain open.

## October 17, 2026 editorial restraint — local changes

Applied Jacob's refreshed shared Website Copy instructions to the current clean `main` checkout at `71857ec7b5fb16f4dfd85bb6976ddf5195a92492`. The owning source is `/Volumes/Storage/General Storage/Sites/versetwo.org`; `scripts/build_prototype.py` and the four content modules generate the eight `prototype/` pages consumed by the deployment packager. The October 9 handoff remains historical and unchanged. This batch stays uncommitted and local at Jacob's request.

Removed stacked introductions, repeated footer reassurances and prototype/naming status, homepage card taglines, the project-origin/privacy sections, the unsupported-next-step reassurance section, and repeated activity explanations. The home page opens with “Start with four lines.” and its activity/story links. Page headings now identify Stories, Practice, Your week, Sources and the adult guide directly. Main-content word counts fell from 238 to 98 on Home, 454 to 328 on Next step, 2,008 to 1,750 on Practice, and 873 to 614 on Sources. These counts exclude shared navigation/footer and include native disclosure text.

All ten artist story blocks are byte-identical to the baseline. Each page retains the same set of external source links. Seven substantive activities, their worked examples, silent/written/spoken response alternatives, budget qualifications, source limitations and adult safeguarding guidance remain. Artist non-endorsement and no implied partnership remain in Sources; teaching attribution remains alongside the relevant exercises and in the standalone facilitator PDF.

Verification on the final files:

- Python 3.13.15 (the pinned 3.13 family): HTML regeneration, all eight-page static checks, all seven deployment tests, parsing of all eleven scripts, and `git diff --check` pass. Regenerating again leaves all eight HTML hashes unchanged. Deployment tests build the current edited assets twice and independently accept them, including private-file exclusion and corruption/source-identity failures. No release artifact was attributed to the old HEAD or published from the dirty checkout.
- Playwright CLI 0.1.22 with isolated local Chrome: all eight pages return HTTP 200 and have no horizontal overflow at 1280, 390 and 320 CSS pixels. All eight also fit 1280/320 widths with a 32px root font (40 page/size checks total). Desktop and mobile screenshots were visually reviewed. Enlarged root text is a stress check, not actual browser zoom or a physical-device test.
- The home writing link reaches `practice.html#four-lines`; all seven native examples open with Enter and close with Space. “Words & meanings” reaches its anchor. The first Tab reaches the visible skip link, and Enter focuses `main`. Story, week, support and footer navigation work. Both download controls succeed and downloaded PDF bytes exactly match the final project files. Sources visibly retain endorsement context.
- WeasyPrint 70.0 rebuilt both tagged PDFs with file/data resources only. The packet remains 23 Letter pages; the facilitator remains one. All 585/40 nonempty text boxes are within page bounds. Rendered page overviews and full-size representative exercise/facilitator pages were inspected. Existing unsupported-CSS warnings remain; no clipping or overlap was found.
- The guarded Ruff preflight stopped with `expected Ruff 0.17.0, found unknown; re-audit before use`. No lint pass or tool-policy change is claimed. Other checks proceeded.

Evidence is retained in `.ai-work/runs/20261017-editorial-restraint/`: baseline source/pages, `native-checks.log`, `editorial-checks.json`, browser layout/control JSON and logs, screenshots under `output/playwright/`, and rendered PDF previews under `output/pdf-preview/`. The final offline and review ZIPs are rebuilt and verified by the existing packaging script; current inventories/hashes are in `package-checks.json`.

Remaining limits: physical-device use, actual browser zoom, screen readers, browser printing, intended-user relevance and qualified partner review. This local review makes no claim about current domain registration or public-site activation. No commit, push, deployment, domain purchase, outreach, youth recruitment or data collection occurred.

## October 17 public repository and hosted CI

Jacob explicitly authorized public GitHub visibility. The repository is now public, and run 39030144180 succeeded on rerun for `2011ad381cda76f69063c5f3f2a2a5b6586c8fa3`, including the seven tests and deployment artifact build/acceptance/upload. This supersedes the billing-blocked status below. Server activation and DNS/configuration remain unchanged. Later commits require their own green run; see GitHub Actions for the exact source identity.

## October 17, 2026 deployment preparation

The existing website and PDFs are unchanged. Added GitHub CI, a static packaging script, independent archive acceptance, a versioned deployment contract and seven regression tests. Local static checks, the seven tests and workflow syntax validation pass. Guarded Zizmor and Ruff checks stopped on tool-version mismatches; neither is reported as passing. The protected server was not accessed or changed. See [deployment.md](deployment.md) for the exact source/artifact handoff and remaining host onboarding.

The explicit local Gitleaks directory scan completed without findings. It skipped the nested copy of the offline ZIP at the configured archive depth; that duplicate is not part of source delivery. The staged Git source is scanned separately before commit.

Staged-source and initial full-history Gitleaks scans passed. The exact initial committed static artifact passed independent acceptance with 13 public files. The first GitHub run (39030008432) did not execute any project steps: GitHub blocked job startup because recent account payments failed or the spending limit needs increasing. No remote CI pass, GitHub-hosted artifact upload or server activation is claimed. The workflow pins Ubuntu 24.04 to avoid the announced `ubuntu-latest` migration; billing remains an owner action.

## October 16, 2026 update

Current scope: eight static pages, ten stories, seven activities, a 23-page Letter packet and the unchanged one-page facilitator outline. New research and claim limits are in [artist-learning-research-2026-10-16.md](artist-learning-research-2026-10-16.md). The October 3 record below is historical and its older counts do not describe this increment.

- Regenerated HTML and ran the existing semantic, local-link, fragment, privacy, dependency, color-pair and budget checks. All ten stories and seven activities are present in print; worked examples are visible there. All scripts compile. No dependencies were installed and no lint pass is claimed.
- Rendered the packet with WeasyPrint 70.0 using only file/data resources. It is tagged, has 23 Letter pages and contains no forms or JavaScript. Inspected rendered thumbnails for all 23 pages and the new activity at full page size; no clipping, overlapping text or stranded headings observed. Existing print separation is preserved.
- Renderer geometry found all 625 nonempty packet text boxes and 41 facilitator boxes within page bounds. The renderer emitted font-cache and existing unsupported-CSS warnings; rendering completed. These checks do not establish assistive-technology reading order or browser print behavior.
- The local preview returned HTTP 200. In the in-app browser, confirmed the four new homepage links, followed the Eminem story link into the new activity, inspected their visual presentation, and opened the new worked-example disclosure with the Return key. This is a representative interaction check, not an exhaustive keyboard, mobile, zoom or screen-reader audit.
- Both PDF copies match. Packaging checks retain all six original source hashes, inspect exact archive membership/member bytes/CRCs and rebuild both review and offline ZIPs. See package-checks.json for current hashes after packaging. No Library replacement or external publication is claimed by a local archive build.

Remaining: real device and disconnected-device use, narrow-width and actual zoom checks of the expanded content, exhaustive keyboard use, screen readers, browser printing, qualified editorial review and intended-user relevance. The prior accessibility backlog remains open. Artist self-report and a completed activity do not establish educational outcomes.

## Earlier validation record

October 3, 2026 · current eight-page local prototype · no accessibility certification

## Current scope and passed checks

Six checked process stories, six original activities, flexible seven-step music/learning plan, support routes, source notes and adult guide. Attributed facts and source limits are in evidence-register.md. All four original supplied files plus the new report/README remain byte-identical to their recorded inputs.

- Local links/assets/fragments; language/page titles; one h1 and focusable main; unique IDs; nonempty links; heading progression; valid ARIA references and native disclosures. All six activities, learner-choice prompts and the complete plan appear in print, with worked answers visible.
- No scripts/events/forms/embeds, remote assets or CSS network dependencies. HTML/CSS/favicon: 91,313 bytes before compression; packet PDF: 81,441 bytes; facilitator PDF: 15,187 bytes. No dependencies installed.
- Chosen foreground/background pairs exceed 4.5:1: ink/white 17.38, muted/white 7.90, blue/white 7.11, focus/white 5.45. This is a color-pair check, not a WCAG audit. Invented budget arithmetic and reserve/expense distinction checked.
- WeasyPrint 70.0 rendered with only file/data resources. All 18 Letter packet pages visually inspected: root pages 7–12; independent agent pages 1–6 and 13–18. Revised one-page facilitator outline visually inspected. No clipping, overlapping text, unreadable text or stranded headings found.
- Renderer geometry: all 504 nonempty packet text boxes and 41 facilitator text boxes within page bounds. PDFs are tagged and have no forms/JavaScript; tags do not establish correct reading order or assistive-technology usability.
- Python compilation passed for all project scripts. The optional guarded Ruff command stopped with expected 0.16.2 versus installed 0.16.10. The [local preflight skill](/Users/jacobanderson/.codex/skills/local-code-preflight/SKILL.md) says: “Stop if a guarded command reports version drift; re-audit before changing the approved manifest.” This blocks that lint check only; no pin change, bypass or lint-pass claim.
- Packaging checks all six preserved source hashes, exact ZIP membership/member bytes/CRCs and identical PDF copies. Final counts/sizes/hashes are in package-checks.json, excluded from the archive to avoid circular checksums. Library upload provenance is recorded after confirmed replacement in library-deliverable.md, also excluded.
- Independent source/content review found no concrete factual error in this increment. Its requested refinements were implemented: “no connection” without “yet,” identical chosen step for any confidence comparison, and independent/library/collaborator routes in the week plan. Agent source checks were corroborated by root inspection of the originals.

## Browser evidence and remaining limits

Earlier seven-page version: all pages fit 320 and 1280px at normal and 32px root text; representative disclosure/skip/focus keyboard checks passed. Those CSS stress checks were not actual browser zoom or screen-reader testing. The current expanded eight-page content has static/print checks above; older browser results are not extended to it.

No supported browser/Computer Use tool is exposed in this turn. No terminal UI automation or denied native application route was used. Current browser reflow, exhaustive keyboard use, actual 200% browser/text setting, screen-reader use, touch-device use, browser-specific printing and disconnected-device opening remain untested. Print-renderer geometry cannot settle those checks. Protocols are in accessibility-review.md.

Artist relevance, naming, reading difficulty, musical usefulness, support feasibility and negative reactions need qualified-partner and intended-user review under separately authorized safeguards. No youth data, target-belief prevalence or causal attendance/graduation/justice evidence exists.

## Evidence access and inference limits

The dedicated 5,813-word report and its README were fully read and preserved unchanged. Selected original relevance/action/cost papers were independently inspected; the ledger distinguishes neutral-control comparisons, units opened from completion/learning, exclusions from intention-to-treat and exploratory cost results from measured reactance. Prompt order and website effects remain hypotheses. Little Simz's process story is attributed to her official interview; no lyrics/audio copied. Tierra Whack and other unresolved artist markers were not added.

Evans 2019 and Evans 2021/2023 are separate studies, distinct from Adjapong/Emdin 2015. Kelly 2020's exact publisher abstract matched, but sample, instruments, analysis and author-stated limitations remain inaccessible behind access controls. Kelly/Sawyer 2019 is another account. No full-text purchase or bypass occurred.

Other imported claims remain candidates. The digest is not a transcript; first-report evidence-register attachments and generated image are missing. Neither gap is silently reconstructed as an original.

## Reproduce light checks

Regenerate HTML with `python3 scripts/build_prototype.py`; run `python3 scripts/check_static.py` and `python3 -m py_compile scripts/*.py`. Render packet and facilitator with the installed WeasyPrint CLI using `--pdf-tags --allowed-protocols file,data`; keep identical copies in output/pdf and prototype. Run check_print_layout.py using WeasyPrint's Python environment. Rebuild archives with `python3 scripts/package_review.py`. No app build is needed. Real browser/assistive-technology/device checks need appropriate tools or a reviewer.
