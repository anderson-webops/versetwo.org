# Validation record

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
