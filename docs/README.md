# Davis deployment documentation

| Guide | Purpose |
| --- | --- |
| [Operations](operations.md) | Independent clone, local checks, collection and hosted publication |
| [Architecture](architecture.md) | Thin importer, shared ownership and versioned configuration |
| [Accepted edition](edition.md) | 290 article pages / 2541 sections from DA4922, exact hashes and verification scope |
| [Acquisition](acquisition.md) | Separate candidate acquisition, complete-corpus checks, promotion and public seeding |
| [Manuscript](manuscript.md) | Davis-specific authored manuscript, evidence-bound native rendering and pre-publication review |
| [Review readiness](review-readiness.md) | Exact candidate hashes, independent technical review and native inspection |
| [0.1 publication](publication-0.1.md) | Preflight and remaining author/publication decisions |
| [Sources](sources.md) | Reviewed Davis source identities, enabled inland policy and access observations |

The [repository guide](../README.md) is the starting point. Generic methods and
their documentation live in [region-intel](https://github.com/docxology/region-intel/tree/main/docs).
For documentation matching the installed runtime, use
[the pinned shared revision](https://github.com/docxology/region-intel/tree/dfa78895e45fba9885e0fe9e1edfca152bed88da/docs).
The shared repository's main branch can contain documentation or code newer
than this consumer's frozen dependency. Public source material retains its own
rights; the repository license does not grant additional rights over it.

Before pushing, stage the intended public changes and run
publication:check with --staged; after committing, run publication:check without
that flag. Both commands use shared methods and check exact Git/worktree bytes.
See the [publication preflight](https://github.com/docxology/region-intel/blob/main/docs/publication-preflight.md)
and [security policy](https://github.com/docxology/region-intel/blob/main/SECURITY.md).
