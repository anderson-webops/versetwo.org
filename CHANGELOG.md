# Releases

## v0.1.5

- Show each artist story as its source and date, followed by two or three labeled fact rows ("Late 2005", "Teacher", "Since kindergarten", and so on) instead of a "said / recalled" paragraph. The rows stay within the checked evidence-register claims.
- Keep story numbers on one line on phones.
- Rebuild the tagged 16-page practice packet.

## v0.1.4

- Serve `/release.json` alongside `/deployment.json`, as the other anderson-webops static sites do. The two files are byte-identical, and the verifier enforces this.
- Add a `404.html` not-found page in the site's own layout, with the main navigation and `noindex`.
- Add `scripts/check_live.py`, a read-only check that the public site serves a release's exact files over IPv4 and IPv6.

Pages and PDFs are otherwise unchanged from v0.1.3. Production activation remains with the protected server-side system.

## v0.1.3

- Rewrite all ten artist accounts so each opens with what the artist did or learned, in fewer words. Dates and publishers stay on each story's eyebrow and source line.
- The Eminem account now matches the CBS interview: reading the dictionary was Anderson Cooper's question, and Eminem's answer was about wanting words at his disposal.
- Rebuild the tagged 16-page practice packet. The facilitator outline is unchanged.

Production activation remains with the protected server-side system.

## v0.1.2

- Remove repeated framing, motivational takeaways, generic onboarding and interface commentary across all eight pages.
- Keep the ten dated artist accounts, seven original activities, worked examples, support routes and essential disclosures.
- Apply the same copy cleanup to the practice packet and facilitator outline.

Includes the previously local October 17 copy review, now authorized for source release. Production activation remains with the protected server-side system.

## v0.1.1

- Add an explicit project version to the static artifact manifest and served deployment identity.
- Validate annotated release tags against VERSION, changelog, the exact clean source commit and main.
- Run the full validation pipeline for version tags and publish verified assets through a draft-first GitHub release job.
- Document the shared Sites commit, tag and release policy in repository guidance.

Website pages and PDFs are unchanged from v0.1.0. The separate local editorial review is not included. These are source/artifact delivery changes, not production activation; protected server-side acceptance is still required.

## v0.1.0

Initial verified static artifact for the existing web server: eight pages, ten sourced artist stories, seven activities, a 23-page practice packet and a one-page facilitator guide. Includes an allowlisted archive, manifest, checksum, deployment contract and hosted CI validation. Source commit: `71857ec7b5fb16f4dfd85bb6976ddf5195a92492`.
