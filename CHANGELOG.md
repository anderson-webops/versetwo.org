# Releases

## v0.1.1

- Add an explicit project version to the static artifact manifest and served deployment identity.
- Validate annotated release tags against VERSION, changelog, the exact clean source commit and main.
- Run the full validation pipeline for version tags and publish verified assets through a draft-first GitHub release job.
- Document the shared Sites commit, tag and release policy in repository guidance.

Website pages and PDFs are unchanged from v0.1.0. The separate local editorial review is not included. These are source/artifact delivery changes, not production activation; protected server-side acceptance is still required.

## v0.1.0

Initial verified static artifact for the existing web server: eight pages, ten sourced artist stories, seven activities, a 23-page practice packet and a one-page facilitator guide. Includes an allowlisted archive, manifest, checksum, deployment contract and hosted CI validation. Source commit: `71857ec7b5fb16f4dfd85bb6976ddf5195a92492`.
