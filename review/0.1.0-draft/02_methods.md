# Methods {#sec:methods}

## Deployment identity and source admission

The versioned deployment document selects a civic profile, regional provider
policy, output directory, accepted-seed directory, enabled monitors and source
catalog. The loader rejects crossed profile identities before starting a
producer. Davis uses municipality code DA4922. Configured zones, routes and
watch bounds are operating parameters, not surveyed city boundaries.
Generic acquisition, artifact contracts, search, rendering and algorithm tests
belong to Region Intel. Davis owns its regional declarations, evidence and
authored manuscript.

Acquisition, when separately undertaken, uses a candidate root rather than
overwriting accepted output. The accepted edition records article and section
membership, local extraction/binding checks, a current table-of-contents
comparison and a bounded deterministic live sample. A sample pass is not an
all-page currentness claim. Source-marked reserved or repealed sections can
remain legitimate retained records when the corresponding heading is present;
an unmarked empty extraction is a different state. Failed or interrupted
candidates retain their evidence instead of replacing the accepted edition.

This paper reads the tracked accepted public seed. It does not rerun acquisition
or substitute whichever live producer output is newest. Its verification clock
therefore remains 2026-10-31T03:39:57.381Z through later figure generation and rendering.
Raw acquisition diagnostics remain local; public commitments identify their
recorded role without making omitted source files reconstructible from a hash.

## Descriptive corpus profile

Let the accepted article-page set be $A$, with $n=|A|$, and let $c_i$ be the
number of retained section objects in article page $i$. The total section-record
count is $N=\sum_i c_i$. The shared profiler computes these quantities and the
minimum, median and maximum of the complete vector of counts. Duplicate article
identifiers or malformed article structure fail admission.

The histogram includes every accepted article page, including a zero count if
present. The companion horizontal bars display at most the twelve article pages
with the largest counts; ties are resolved by article identifier and GUID.
The exact CSV retains every row, so a reader can inspect the complete
distribution rather than infer it from the selected bars. The histogram uses
at most 25 equal-width bins, bounded by the observed range. No resampling,
population inference, significance test or uncertainty interval is applied:
these are descriptive properties of a finite retained snapshot.

Counts describe publisher/extractor segmentation. They are not measures of
policy importance, regulatory burden, textual difficulty or neighborhood
experience. Article titles and numbers help a reader locate records; the
analysis does not infer legal topics or assign normative weights.

## Evidence projection and figure production

Required and optional seed members are captured through bounded, no-follow
reads into a private snapshot before the existing publication validator parses
them. Counts must agree with the accepted verification report. The manuscript
also captures deployment/configuration bytes, the immutable shared dependency
and frozen lock, bibliography, claim ledger, numbered sources and cover image.
The effective selected configuration participates even when a caller explicitly
selects an alternative deployment document.

A composite renderer fingerprint binds the shared input, projection, membership,
template-adapter and figure-generation modules, together with the pinned
template asset inventory. Evidence tokens hydrate prose from those captured
inputs. Matplotlib produces the measured corpus plot and two explicitly
conceptual method diagrams as PNG, PDF and SVG. The CSV and profile JSON remain
available alongside them. The cover is an AI-generated editorial illustration;
it is not a map, observation or analytical figure.

## Template-backed publication

The native backend is docxology/template at revision
c18dae54a07fe6ac3a7b1a1a274251c169a12e7a. The shared adapter verifies the checkout's identity, commit
and tracked cleanliness and verifies that the imported rendering module belongs
to that checkout. It calls the actual combined PDF and HTML RenderManager APIs.
The template supplies title/cover composition, graphical front matter,
typography, citations and offline reader assets. Direct Pandoc invocation is
not an alternative regional backend.

Native work occurs in a fresh ignored namespace under the selected template
checkout because its offline asset writer confines outputs to that root. The
adapter copies only declared publication members to the regional staging
directory. The template source remains unchanged. Source inputs are checked
again before recoverable promotion; failed staging and the previous complete
edition remain available. Rendering behavior follows reproducibility principles
that connect reported results to the code and data that produced them
[@sandve2013], while making the rendering toolchain an explicit dependency.
