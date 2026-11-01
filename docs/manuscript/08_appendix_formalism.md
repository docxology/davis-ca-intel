# Appendix: Formal Contracts and Worked Records {#sec:appendix}

## Data statement

| Question | Davis record |
|---|---|
| Unit | Accepted article-page and section objects |
| Origin | eCode360 DA4922 municipal-code publication |
| Edition | Snapshot identified in the evidence receipt |
| Observation time | {{VERIFIED_AT}} |
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
profile: {{PROFILE_ID}}
municipality: {{MUNICIPALITY_CODE}}
source edition: {{EDITION_ID}}
shared runtime: {{CORE_PIN}}
template revision: {{TEMPLATE_PIN}}
manuscript input: {{EVIDENCE_FINGERPRINT}}
~~~

The complete file-by-file commitments are in evidence.json and
review-receipt.json. template-render.json records the actual rendering API,
template identity and native versions. Three acceptance questions remain
separate: whether captured inputs match their declared edition; whether the
rendering methods produce a coherent artifact from those inputs; and whether
the research interpretation is suitable for its intended audience and use.
