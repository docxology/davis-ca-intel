# Davis 0.1 manuscript review readiness

The exact candidate below is technically ready for human and editorial review.
The independent AI technical gate returned APPROVE after source inspection,
installed-package verification, adversarial replay and final rendered inspection.
This is a review draft. It is not a formal publication or independent human
scientific or legal peer review.

## Read the candidate

- [A4 PDF](../review/0.1.0-draft/manuscript.pdf): 13 physical pages, including the cover.
- [Offline HTML entry](../review/0.1.0-draft/web/index.html): retain the complete packet's assets and figures when copying.
- [Corpus CSV](../review/0.1.0-draft/article-sections.csv) and [profile JSON](../review/0.1.0-draft/corpus-profile.json).
- [Architecture SVG](../review/0.1.0-draft/figures/architecture.svg), [measured corpus SVG](../review/0.1.0-draft/figures/corpus-profile.svg), [evidence-boundary SVG](../review/0.1.0-draft/figures/evidence-boundaries.svg).
- [Native receipt](../review/0.1.0-draft/template-render.json), [complete byte inventory](../review/0.1.0-draft/review-receipt.json) and [technical evidence summary](review-evidence.json).

## Exact bindings

| Item | Accepted value |
|---|---|
| Shared core | [7667ae7fdfa7cc54fc80d90153c2873051f29ac4](https://github.com/docxology/region-intel/commit/7667ae7fdfa7cc54fc80d90153c2873051f29ac4) |
| External template | [c18dae54a07fe6ac3a7b1a1a274251c169a12e7a](https://github.com/docxology/template/tree/c18dae54a07fe6ac3a7b1a1a274251c169a12e7a) |
| Input fingerprint | 08013accbc134f81375f357fd0f2422f2a324105e43fdd81de84b4b1e0e29cd7 |
| PDF SHA-256 | 0473c66f705d89debd22cc63c4ed4fba6860d9af274fd0838f55e78605dddd85 |
| HTML SHA-256 | 1bf28676703449a86641c357e8b66e5874737d43bdc1dea9f5c56cf761aa5529 |
| Packet | 290 declared members plus the review receipt |
| Accepted observation | 290 article pages; 2541 section records |
| Verification clock | 2026-10-31T03:39:57.381Z |

The complete article profile has median 7, minimum 0, maximum 66 and four
zero-section article pages. It describes accepted record segmentation.
It does not measure legal importance, regulatory burden or resident experience.
Rendering did not reacquire the municipal code or advance its verification clock.

## What passed

| Surface | Observed evidence |
|---|---|
| Complete shared qualification | 2126 passed, 2 explicit live-Ollama skips, 0 failed; 2128 tests across 206 files in ordinary and coverage runs; strict application and test TypeScript passed |
| Coverage | 85.5% measured lines and 87.43% functions; the project's declared line floor is 60%; branch coverage was not measured |
| Genuine template rendering | Actual RenderManager combined PDF and web APIs at the declared public revision; Python 3.14.8 with frozen template dependencies, including Matplotlib 3.11.2 |
| Installed ownership | All 239 tracked shared source files matched the published core bytes in both regional installations; no sibling implementation bridge |
| Corpus calculation | Independent all-row seed calculation, profile values and exact CSV replay matched |
| Native PDF | qpdf passed; all 13 final raster pages inspected by builder and independent reviewer; seven embedded subset fonts with Unicode maps; no words outside the physical page |
| Offline reader | 10 numbered source sections, 10 references, three figures and four images; local fonts and mathematics loaded; no broken image, internal anchor, external request, failed response, script error or horizontal overflow at 1440 px and 390 px |
| Figure access | The full desktop plot fits its viewport; the mobile full-size link opened the original 2373 by 1149 pixel PNG |
| Consumer acceptance | Davis release check, Crescent validation, both frozen installs, fresh Pages export/validation and real municipal-code search passed |
| Adversarial replay | Baseline accepted; all 15 malformed packet variants rejected; real missing-native-tool failure preserved every member of the prior complete edition and retained diagnostics |

The pinned shared core's [hosted qualification](https://github.com/docxology/region-intel/actions/runs/41263401775)
also passed. Consumer hosted runs are separately bound to their pushed source
commits and remain visible under each repository's Actions history.
The PDF is untagged; this record does not claim PDF/UA conformance.

## Review findings and preserved failures

The independent reviewer reproduced three false accepts in the superseded
96b6748 runtime: comma-colliding filenames, a prototype-named extra member and
comma-colliding tool keys. Commit 7667ae7 replaces delimiter comparison with
structural name comparison, counts prototype-named files and requires explicit
own SHA-256 entries. Real-files tests failed before that fix; the final installed
packet rejects all three variants. Earlier candidates and their failed controls
remain preserved and are not used as final approval.

The initial full coverage run also retained one unexpected local-fixture HTTP
404 in an unchanged connector test. Its isolated 13-test run and subsequent
complete unchanged-source reproduction passed; the corrected final core's full
ordinary and coverage runs passed too. No connector behavior was changed to
hide it. That initial transient's root cause remains unresolved.

Earlier native font-name and staging-membership failures remain in the retained
execution evidence. The completed edition uses verified font files and validates
the whole staged packet before promotion. Matplotlib SVG and pinned native web
bytes retain generated whitespace under bounded path attributes; a real authored
trailing-whitespace control still failed as required.

## Scholarship, artwork and publication scope

The ten cited works supply methodological context. Their primary-source reading
scope and limits are recorded in the shared
[scholarship ledger](https://github.com/docxology/region-intel/blob/7667ae7fdfa7cc54fc80d90153c2873051f29ac4/docs/scholarship.md).
The cover is [AI-generated conceptual artwork](assets/ARTWORK.md).
Only the corpus-profile figure reports measured source structure; the other
diagrams explain method and evidence ownership.

Final authorship, contribution, funding/conflict declarations, permitted source
use, editorial assessment and any scientific or legal interpretation still need
their appropriate owner or expert disposition before publication. Technical
review does not supply those decisions. No release, tag or DOI was created.
See the [0.1 publication procedure](publication-0.1.md).

## Fresh-checkout publication correction

The first hosted native run for the 519b1b8 consumer commit rejected the shipped
packet before rendering: an unanchored output-directory ignore rule omitted
MathJax's two output JavaScript modules from Git even though both were present
in the reviewed local packet. The failed [Actions run](https://github.com/docxology/davis-ca-intel/actions/runs/41264307024)
is retained. The corrected root-only ignore rule includes both exact declared
members; committed-tree replay is now part of fast consumer acceptance and runs
before native tool installation. The approved manuscript inputs, PDF, HTML and
complete packet hashes are unchanged. A staged Git-tree archive is validated for complete membership and replay before the corrective push.

The prior independent AI technical approval binds the unchanged manuscript
inputs and complete packet bytes. This correction changes publication assembly
and CI ordering; it does not regenerate or edit the reviewed PDF or HTML.
