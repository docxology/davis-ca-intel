# Davis manuscript and 0.1 review candidate

Davis owns [ten authored source sections](manuscript/README.md), a bibliography,
claim ledger and manuscript configuration. Shared checking, evidence hydration,
PDF/HTML rendering and packaging remain in region-intel. The manuscript's 0.1.0
review target is independent of the application's 4.0.0 package version.

```sh
bun run manuscript:check
bun run manuscript:render
bun run manuscript:validate-render
bun run manuscript:bundle
bun run manuscript:validate-render -- --bundle
```

The native renderer requires Pandoc, XeLaTeX, qpdf and pdftotext. A clean install
can check the source against tracked public evidence without those native tools.
The review workflow builds PDF/HTML from accepted Davis seed counts and exact
input hashes; it does not refresh the upstream code or import Crescent findings.

The [review PDF](../review/0.1.0-draft/manuscript.pdf),
[standalone HTML](../review/0.1.0-draft/manuscript.html),
[evidence](../review/0.1.0-draft/evidence.json) and
[render receipt](../review/0.1.0-draft/review-receipt.json) form a labelled
pre-publication candidate. Read the [readiness record](review-readiness.md) for
the actual independent review, native page inspection, prerequisites and limits.
Neither a renderer success nor this packet creates a release, tag or DOI.
The retained Crescent reference paper remains separately owned by region-intel.
