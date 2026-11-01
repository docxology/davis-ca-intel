# Results {#sec:results}

## Accepted snapshot and configuration

The accepted Davis edition contains 290 article pages and
2541 section records. These counts refer to the retained DA4922
edition and its verification timestamp, not a new collection conducted for
this manuscript.

| Recorded item | Value | Interpretation |
|---|---:|---|
| Municipality code | DA4922 | Source identity |
| Article pages | 290 | Accepted publisher/extractor article units |
| Section records | 2541 | Retained section objects in those articles |
| Declared sources | 10 | Configured catalog entries |
| Enabled monitors | 8 | Selected adapter policy |

These rows have different denominators. A configured monitor is not an
observation, and the source catalog does not enumerate the city's complete
information environment. Davis selects inland operating policy; unused coastal
fields retained for compatibility do not establish coastal coverage in Davis.

## Article-level structure

Across all 290 article pages, the median is
7 section records per page, with a minimum of
0, maximum of 66 and
4 zero-section article pages. All values are injected
from the shared profile of the accepted seed.

![Article-level section counts in the accepted Davis edition. Panel A includes every article page and marks the median; Panel B shows the twelve largest article pages, ordered deterministically. Counts measure retained source structure, not legal importance or civic burden. The complete numerical fallback is article-sections.csv.](../output/figures/corpus-profile.png){#fig:corpus_profile}

The distribution in @fig:corpus_profile makes the within-edition segmentation visible without
claiming that larger article pages are more important. The associated CSV
contains GUID, article identifier, title and section count for every page.
The aggregate is reconciled against the same accepted article and section
denominators used in the manuscript. No population statistic about Davis
residents is derived from this distribution.

## Reusable boundary and public surfaces

The local dashboard and static edition use the deployment's accepted evidence
and official source links. A successful source search is distinguishable from
a model-generated answer. Retrieval-augmented generation combines retrieval
with a generative model [@lewis2020], but that architectural relationship does
not establish the factuality of this deployment's generated answers. No model
benchmark or answer-quality result is presented here.

![Three evidence planes remain distinct: accepted corpus bytes support snapshot claims, selected policy supports configuration claims, and native output checks support rendering claims. Legal currency, interpretation, usability, civic impact and publication require separate evidence or decisions. This is a conceptual claim-boundary diagram.](../output/figures/evidence-boundaries.png){#fig:evidence_boundaries}

The distinction illustrated in @fig:evidence_boundaries is an explicit
ownership and reporting boundary. Software acceptance and native artifact checks
are retained in the review record rather than interpreted as measurements of
civic usefulness. The rendered packet contains the template identity, input
fingerprint, complete offline asset inventory and output hashes. Those
commitments make a candidate inspectable; they do not certify its interpretation.
