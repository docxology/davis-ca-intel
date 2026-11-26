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

The native renderer uses [docxology/template](https://github.com/docxology/template)
at the exact revision declared by the shared package. Set REGION_TEMPLATE_ROOT
and REGION_TEMPLATE_PYTHON to that prepared checkout and interpreter. Pandoc,
pandoc-crossref, XeLaTeX, qpdf and pdftotext must also be available. See the shared
[template procedure](https://github.com/docxology/region-intel/blob/main/docs/manuscript.md). A clean install
can check the source against tracked public evidence without those native tools.
The review workflow builds PDF/HTML from accepted Davis seed counts and exact
input hashes; it does not refresh the upstream code or import Crescent findings.

The [review PDF](../review/0.1.0-draft/manuscript.pdf),
[offline HTML](../review/0.1.0-draft/web/index.html),
[evidence](../review/0.1.0-draft/evidence.json) and
[render receipt](../review/0.1.0-draft/review-receipt.json) form a labelled
pre-publication candidate. Read the [readiness record](review-readiness.md) for
the actual independent review, native page inspection, prerequisites and limits.
Neither a renderer success nor this packet creates a release, tag or DOI.
The retained Crescent reference paper remains separately owned by region-intel.

The complete offline HTML tree includes assets and figures. Corpus CSV/JSON,
vector/raster figures and the template provenance receipt accompany the packet.
The cover is [conceptual artwork](assets/ARTWORK.md); the corpus profile is measured.
A [citation-to-claim reading record](https://github.com/docxology/region-intel/blob/main/docs/scholarship.md)
limits each external reference to its supported contextual use.

Direct numerical downloads: [all article counts](../review/0.1.0-draft/article-sections.csv)
and [the complete profile](../review/0.1.0-draft/corpus-profile.json).
The three figures are supplied in PNG, SVG and PDF, with full-size image links
in the native reader. The [earlier technical evidence summary](review-evidence.json)
binds the independently reviewed earlier candidate and controls.

## Pinned Template offline check

This check uses all ten canonical sections, accepted public seed bindings, and the figures and numerical fallbacks from the retained review draft. The staging script verifies the source bindings, checks that token substitution reproduces the archived hydrated sections, and checks the reused figures against the archived receipt. It writes only ignored output. A changed source or evidence binding requires a new native candidate before reusing this procedure.

From a clean Davis checkout with Python 3.11 or newer:

```sh
python3 docs/examples/stage_review.py
```

Use a separate [Template checkout](https://github.com/docxology/template/tree/87704feae0a4490ef7dad9c931d268e8c30273c2) at `87704feae0a4490ef7dad9c931d268e8c30273c2`, with Pandoc, pandoc-crossref, and LaTeX from the [Template run guide](https://github.com/docxology/template/blob/87704feae0a4490ef7dad9c931d268e8c30273c2/docs/RUN_GUIDE.md). Set `davis_checkout` to the absolute Davis checkout path. Run from Template with an unused project slot.

```sh
uv sync --locked --no-dev
mkdir -p projects/working
ln -s "$davis_checkout" projects/working/davis-ca-intel
uv run --no-sync python scripts/pipeline/stage_03_render.py --project working/davis-ca-intel --skip-manuscript-hydration
uv run --no-sync python scripts/pipeline/stage_04_validate.py --project working/davis-ca-intel
```

Read the combined PDF under `output/pdf/`, the combined HTML at `output/web/index.html`, and the reports in `output/reports/` in the Davis checkout. This documentation check retains the archived observation time and original candidate bindings in the prose. The new render receipt records the renderer used for this check. The archived review packet uses a different, separately pinned production renderer.
