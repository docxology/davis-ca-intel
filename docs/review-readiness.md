# Davis 0.1 manuscript review readiness

The tracked packet is a 0.1.0 review draft. Its direct byte bindings below come from the [tracked receipt](../review/0.1.0-draft/review-receipt.json). The [earlier independent technical review](review-evidence.json) assessed a different fingerprint and output hashes. Its findings remain evidence for that earlier candidate.

## Read the candidate

- [A4 PDF](../review/0.1.0-draft/manuscript.pdf): 13 physical pages, including the cover.
- [Complete offline HTML](../review/0.1.0-draft/web/index.html): keep the whole packet when copying it.
- [All-row CSV](../review/0.1.0-draft/article-sections.csv) and [profile JSON](../review/0.1.0-draft/corpus-profile.json).
- [Architecture](../review/0.1.0-draft/figures/architecture.svg), [measured profile](../review/0.1.0-draft/figures/corpus-profile.svg) and [evidence boundaries](../review/0.1.0-draft/figures/evidence-boundaries.svg).
- [Native provenance](../review/0.1.0-draft/template-render.json), [complete inventory](../review/0.1.0-draft/review-receipt.json) and [earlier independent technical evidence](review-evidence.json).

## Tracked packet bindings

| Item | Tracked value |
|---|---|
| Shared core | `51b18faeec1454e80a533795c6e3859eaeb5fc9b` |
| Native Template | `c18dae54a07fe6ac3a7b1a1a274251c169a12e7a` |
| Input fingerprint | `81b99f78d577a16cd88a71a1da2880bc789232aaaacb203d94140d95ae0823d3` |
| PDF SHA-256 | `77deadfb4528a012881cc9af5852aa6a98a95083e3270b019a0cff876cb24659` |
| HTML SHA-256 | `4991a48dd5ea3b95d404155f69e7cdfaad962e3f12cc8cc2851401a9233eefa3` |
| Packet inventory | 290 declared members and the review receipt |

The all-article profile has median 7, minimum 0, maximum 66 and four zero-section
article pages. It describes publisher/extractor record segmentation. Rendering
did not reacquire the municipal code or advance its verification clock.

## Current verification

Use the [offline manuscript procedure](manuscript.md#pinned-template-offline-check) to validate the source-bound counts and render the authored case study through the documentation Template. Use the [native procedures](manuscript.md) for a current complete review packet on the production renderer revision.

The [prior readiness record](https://github.com/docxology/davis-ca-intel/blob/5468bd905066c28d3cc4dc472c5d2ba98b89bc8c/docs/review-readiness.md) preserves the original technical findings, native inspection, and recorded failures. The exact previous candidate is identified by the earlier evidence file. Author approval, rights, scientific and legal review, and publication have their own requirements. See the [0.1 publication procedure](publication-0.1.md).
