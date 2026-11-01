# Davis 0.1 manuscript review readiness

**Disposition: ready for technical review.** A separate AI-assisted reviewer
approved this exact source/evidence/native candidate after independent executable
controls and rendered-output inspection on 2026-11-01 UTC. No technical blockers
remain in that review. This is not human peer review, scientific/legal acceptance
or authorization to publish version 0.1.

## Frozen candidate

The [five-page PDF](../review/0.1.0-draft/manuscript.pdf) and
[standalone HTML](../review/0.1.0-draft/manuscript.html) are labelled version 0.1.0,
`review-draft`. The application retains its existing package version. The
[evidence](../review/0.1.0-draft/evidence.json),
[claim ledger](manuscript/claim_ledger.json) and
[render receipt](../review/0.1.0-draft/review-receipt.json) supply the recorded
inputs, output inventory, tool versions and claim boundaries.

| Binding | Exact value |
|---|---|
| Shared core commit | `7cb15fa1af0455e4d756551ddf828da0cbf5095e` |
| Input fingerprint | `2d34a2664e2f140bdee02d53277b93225a76122f8848ed3620d00d74c5067af3` |
| PDF SHA-256 | `3c4a6977a366d5e35213d36225a90fc7de1b3f8b5a320a5825ff7163c09aa4b1` |
| HTML SHA-256 | `3b95875d08b51560fb253bc375528786792ca9fb0bd440057971b3e5554fd0f5` |
| Shared renderer source SHA-256 | `62cd33591f10a0c1319c70b4d7537db4ea84484ace649fd54cc2b6469b5a10f0` |
| Accepted municipal edition | `2d74bf8205ecde96b88b4183d4d47169d83ee910e5d1ce125fd6c77bd31eca8b` |
| Recorded seed verification | `2026-10-31T03:39:57.381Z` |

The empirical scope remains 290 article pages and 2541 sections from DA4922.
The 10 source declarations and 8 enabled monitors describe configuration;
they are not successful-collection counts. No Crescent empirical findings
are represented as Davis observations.

## Verification and independent review

- The shared implementation gate passed 2118 tests, with two optional live-model
  skips and zero failures. Measured line coverage was 85.67% (60% gate), function
  coverage 87.52%; branch coverage was not measured. The final dependency-only
  commit preserved the qualified package graph and passed frozen installation
  and contracts. The [full hosted core gate](https://github.com/docxology/region-intel/actions/runs/41254701433)
  then passed at the exact final core SHA above.
- The installed Davis importer passed frozen installation, consumer types and
  acceptance, authored-manuscript contracts, native bundle generation and
  `bun run release:check`. Current-input replay validates all 19 bundle members.
  Both consumers passed fresh Pages export/validation and relative-link checks
  with intentionally invalid link controls.
- Real desktop/mobile reader search passed in both regions. Davis static code
  search followed official eCode360 links and expandable news/meeting lists
  remained usable. No page errors or horizontal overflow were observed at the
  tested widths, 1440 and 390 pixels.
- The independent reviewer exercised 16 scenarios against the actual installed
  package, including pristine replay, changed effective configuration, byte and
  member corruption, changed sources, BOM config, symlink escape, forged receipt
  assertions and a genuinely unavailable Pandoc. A failed build preserved all
  prior packet bytes. Earlier symlink and BOM defects were reproduced, repaired
  in core and independently checked again before approval.
- Nine additional copied-bundle mutations rejected: changed PDF, missing HTML,
  unexpected member, stale fingerprint, forged version/publication/review/status,
  and altered hydrated prose even with its output hash recomputed.
- qpdf accepted the native PDF. Every one of its five A4 pages was inspected for
  clipping, overlap, tables, citations, glyphs and draft labels. Desktop/mobile
  HTML captures were inspected using Chrome for Testing 145.0.7632.6 with the
  installed Playwright 1.58.2. Each exposed ten sections and three references,
  with no page errors, horizontal overflow or remote content requests. All
  owned browser/server processes closed normally.

The committed HTML preserves native Pandoc output bytes. Its generated CSS has
29 lines with trailing spaces; a file-specific `.gitattributes` rule exempts only
that artifact from blank-at-end-of-line checks. A synthetic authored-file
whitespace defect still failed, and the exact HTML hash above remained unchanged.

The independent review read the shared code/tests, all ten Davis sections,
bibliography, claim ledger and final generated text. Three contextual references
were checked against their primary publisher/standards pages. Full source,
controls, screenshots, raw logs and earlier failures are retained in the local
review evidence; this public record summarizes their disposition. The renderer's
receipt deliberately does not manufacture independent review or publication
approval. That disposition is recorded here separately.

## Rechecking and publication boundary

```sh
bun install --frozen-lockfile
bun run release:check
bun run pages:export
bun run pages:validate -- .pages
```

Use the [native procedure](manuscript.md) to regenerate a changed candidate.
Changes to captured source, seed, effective configuration, package/lock or renderer
require a new packet and renewed relevant review. Do not edit generated members.
The [native workflow](../.github/workflows/manuscript.yml) checks the committed
packet and independently renders another edition; inspect Actions at the actual
consumer commit for hosted results. Local acceptance does not establish Pages
publication or hosted native execution.

Legal currency, all-page currentness, civic impact, usability, accessibility and
model-answer factuality remain unqualified. Source rights and final author,
funding/conflict and contribution declarations require the owner's disposition.
The [0.1 publication prerequisites](publication-0.1.md) remain in force. No tag,
release or DOI has been created by this review-readiness work.
