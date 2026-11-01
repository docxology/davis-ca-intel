# Reproducibility and Artifact Specification {#sec:reproducibility}

The Davis consumer installs its full public Git dependency SHA through a frozen
Bun lockfile. It does not require a sibling core checkout. From that checkout,
the review workflow is:

```sh
bun install --frozen-lockfile
bun run validate
bun run manuscript:check
bun run manuscript:render
bun run manuscript:validate-render
```

The renderer uses native Pandoc citation processing and XeLaTeX for PDF and
standalone HTML for web review. It disables raw HTML/TeX in source Markdown,
uses a finite owned child for each tool, checks the PDF with qpdf and extracts
text for unresolved-content checks. Exact tool versions and member hashes are
recorded alongside the rendered edition. Failed builds preserve the prior
complete edition; successful rendering alone does not imply peer review.

The input fingerprint is recorded in the appendix and evidence JSON. It binds
the accepted seed, configuration, dependency manifest and lock, authored source,
bibliography, claim ledger and renderer source. Re-checking an edition compares
current inputs and exact output members. Rendered PDF timestamps may differ
across independent builds; compare the declared inputs and semantic content
separately from the receipt that identifies one actual PDF/HTML byte edition.

The public data and source are available at the Davis CA Intel repository.
Raw source custody and acquisition diagnostics remain local; the public seed
retains their commitments rather than claiming that omitted raw files can be
reconstructed from a digest. This distinction limits independent re-extraction
from the public bundle and should guide any replication claim.
