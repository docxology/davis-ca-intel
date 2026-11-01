# Davis 0.1 manuscript review readiness

This exact candidate is technically ready for human and editorial review. The
independent AI native-artifact review returned APPROVE after installed-source
binding, adversarial replay, independent corpus calculation and rendered review.
It remains a review draft; scientific, legal and author publication decisions
retain their own requirements.

## Read the candidate

- [A4 PDF](../review/0.1.0-draft/manuscript.pdf): 13 physical pages, including the cover.
- [Complete offline HTML](../review/0.1.0-draft/web/index.html): keep the whole packet when copying it.
- [All-row CSV](../review/0.1.0-draft/article-sections.csv) and [profile JSON](../review/0.1.0-draft/corpus-profile.json).
- [Architecture](../review/0.1.0-draft/figures/architecture.svg), [measured profile](../review/0.1.0-draft/figures/corpus-profile.svg) and [evidence boundaries](../review/0.1.0-draft/figures/evidence-boundaries.svg).
- [Native provenance](../review/0.1.0-draft/template-render.json), [complete inventory](../review/0.1.0-draft/review-receipt.json) and [technical evidence](review-evidence.json).

## Exact bindings

| Item | Accepted value |
|---|---|
| Shared core | [dfa78895e45fba9885e0fe9e1edfca152bed88da](https://github.com/docxology/region-intel/commit/dfa78895e45fba9885e0fe9e1edfca152bed88da) |
| External template | [c18dae54a07fe6ac3a7b1a1a274251c169a12e7a](https://github.com/docxology/template/tree/c18dae54a07fe6ac3a7b1a1a274251c169a12e7a) |
| Input fingerprint | 2b8dc3d4d9bb8531a59c19f412e5adf11814c3fb6a1f8907580174ebb210a2f8 |
| PDF SHA-256 | 08b2ae6606293a99b1e4fd86ee899f3678cb2f42bd3504129128b03c6a425ec5 |
| HTML SHA-256 | 60be5427f66a5642a6f38ec5f0404b6aad205a81802e9128918ada2a397b539a |
| Packet | 290 declared members plus the review receipt |
| Accepted observation | 290 article pages; 2541 section records |
| Verification clock | 2026-10-31T03:39:57.381Z |
| Independent artifact report SHA-256 | 501200b9d41f6668deb2c0081ee6ac21552c48a4de562d5fb0956cd04b947825 |

The all-article profile has median 7, minimum 0, maximum 66 and four zero-section
article pages. It describes publisher/extractor record segmentation. Rendering
did not reacquire the municipal code or advance its verification clock.

## Verified technical surfaces

| Surface | Observed evidence |
|---|---|
| Complete shared qualification | [Exact-SHA Linux run](https://github.com/docxology/region-intel/actions/runs/41354853182): ordinary and coverage lanes each passed 2132 tests, with 2 explicit live-Ollama skips and 0 failures; 2134 tests across 207 files in each lane; strict application/test types passed |
| Coverage | 86.55% measured lines; 88.96% functions; declared line floor 60%; branch coverage unmeasured |
| Installed ownership | All 240 tracked shared source files matched the public core in both consumers; the thin importers use the frozen Git dependency |
| Genuine template use | Actual combined PDF/web RenderManager APIs at the pinned template revision; frozen Python 3.14.8/Matplotlib 3.11.2 environment |
| Data | Fresh independent all-row seed calculation and exact CSV replay; all recorded denominators unchanged |
| Native PDF | qpdf passed; all 13 final pages inspected or matched to inspected raster bytes; seven embedded Unicode subset fonts; no words outside physical pages |
| Offline HTML | 10 sections, 10 references, 3 figures, 4 images; local fonts/math; no broken images/anchors, remote requests, failed responses, script errors or horizontal overflow at 1440 px and 390 px |
| Command fidelity | Both complete executable lines survive PDF extraction and appear as standalone HTML code lines at both viewports |
| Figure access | Desktop figure fits its viewport; mobile full-size route opens the 2373 by 1149 pixel original |
| Consumer acceptance | Both frozen installs, both Pages export/replay checks and real municipal searches passed; the final Davis release check passed |
| Adversarial replay | Fresh baseline accepted, all 15 malformed packet variants rejected; a real missing-native-tool failure preserved every prior output byte and retained diagnostics |

The [core main recheck](https://github.com/docxology/region-intel/actions/runs/41355890349)
also passed at the same core SHA. Consumer publication and hosted acceptance are
bound separately to the commits shown in [Davis Actions](https://github.com/docxology/davis-ca-intel/actions)
and [Crescent City Actions](https://github.com/docxology/crescent-city-intel/actions).
The artifact approval does not supply those separate publication results.
The PDF is untagged; PDF/UA conformance is not claimed.

## Publication correspondence and retained failures

The shared preflight verifies actual Git/worktree bytes for selected public
inputs and every complete manuscript member. It rejects ignored/missing blobs,
dirty required bytes, links and observed reference drift. Independent real-Git
controls reproduced missing tracked optional-seed and manuscript-marker false
acceptances, then passed unchanged after the selected-reference union repair.
An unstaged deletion rejects HEAD and index; a staged deletion can match index
while still rejecting HEAD. Source acquisition and semantic acceptance remain
separate checks.

Several local macOS ordinary/coverage runs retain deadline failures. Those
platform results remain unresolved. Full source qualification here is the pinned
Linux workflow above, with original command arguments, deadlines, output fences,
failure propagation and coverage floor. Successful coverage output is now retained
alongside its full denominator.

Rendered review caught smart punctuation in a prose flag, then an inserted
typeset hyphen inside an inline command. Earlier packets and reviews remain
preserved. The final fenced command block passes the same whole-command check
that rejected the superseded packet. The final artifact review binds only the
fingerprint and hashes above.

Earlier packet-membership and Linux-font preparation failures remain documented
in the [preceding readiness record](https://github.com/docxology/davis-ca-intel/blob/c8a1a5dc45658968acf040f61ca23a335b5393f6/docs/review-readiness.md).
Fresh-checkout preflight runs before native installation; the native workflow
checks explicit OpenType fonts and retains failed staging diagnostics.

## Scholarship, artwork and publication scope

The ten references supply methodological context with bounded primary-source
reading recorded in the shared [scholarship ledger](https://github.com/docxology/region-intel/blob/dfa78895e45fba9885e0fe9e1edfca152bed88da/docs/scholarship.md).
The cover is [AI-generated conceptual artwork](assets/ARTWORK.md). The corpus
profile reports measured retained structure; the other diagrams explain method
and claim ownership.

Authorship/contribution, funding/conflict declarations, permitted source use,
editorial assessment and scientific/legal interpretation require their appropriate
owner or expert disposition. Technical review does not supply those decisions.
No release, tag or DOI was created. See the [0.1 publication procedure](publication-0.1.md).
