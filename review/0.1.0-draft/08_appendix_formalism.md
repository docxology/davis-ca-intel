# Appendix: Formal Contracts and Worked Records {#sec:appendix}

## Data statement

| Question | Davis record |
|---|---|
| Unit | Accepted article-page and section objects |
| Origin | eCode360 DA4922 municipal-code publication |
| Edition | Snapshot identified in the evidence receipt |
| Observation time | 2026-10-31T03:39:57.381Z |
| Intended use | Source-linked inspection, descriptive corpus structure and reproducible software study |
| Not represented | Resident population, complete city activity, legal adjudication or a model benchmark |
| Excluded public members | Credentials, raw acquisition HTML and private operational diagnostics |
| Numerical fallback | Complete article-sections.csv and corpus-profile.json |

This compact statement is informed by dataset documentation scholarship
[@gebru2021; @bender2018]. It supplements the source and claim ledger; it does
not claim compliance with every proposed datasheet question.

## Constructed arithmetic control

For a deliberately synthetic vector of article section counts
$[2,0,4]$, the profiler must return three article pages, six section records,
a median of two, a minimum of zero, a maximum of four and one zero-section
page. This example tests the transformation; none of these values is a Davis
observation. A duplicate article identifier must fail rather than silently
increase a denominator.

## Candidate bindings

~~~text
profile: davis-ca
municipality: DA4922
source edition: 2d74bf8205ecde96b88b4183d4d47169d83ee910e5d1ce125fd6c77bd31eca8b
shared runtime: 0eb390bc804c5a3ae5304839187f914364d0bec3
template revision: c18dae54a07fe6ac3a7b1a1a274251c169a12e7a
manuscript input: 9972083bd6e22a59e86de4eb590378402963e32c06af0f35e4b9fd1d436e5215
~~~

The complete file-by-file commitments are in evidence.json and
review-receipt.json. template-render.json records the actual rendering API,
template identity and native versions. Three acceptance questions remain
separate: whether captured inputs match their declared edition; whether the
rendering methods produce a coherent artifact from those inputs; and whether
the research interpretation is suitable for its intended audience and use.
