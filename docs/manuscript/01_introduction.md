# Introduction {#sec:introduction}

## Problem and scope

A useful regional information system must answer two different questions: what
its software can do, and what its retained evidence actually supports. A source
adapter may be implemented without a current observation. A searchable municipal
snapshot may be internally coherent without establishing that every provision
remains current. A well-formed generated answer may still require substantive
review. These distinctions become harder to maintain when a second locality
inherits a first locality's configuration, language and publication artifacts.

This case study concerns Davis, California. Its unit of observation is the
accepted DA4922 municipal-code record set and the deployment documents that
select its operating policy. It examines whether shared software can preserve
regional identity, reproduce a descriptive corpus profile and publish a
manuscript whose numerical statements remain attributable to that record set.
It does not estimate public benefit, legal completeness or hazard exposure.
The original Crescent City application supplies compatibility history in the
shared package; its empirical findings are not Davis observations.

## Scholarship and design commitments

Open-government data scholarship cautions against treating the act of opening
data as a sufficient mechanism for realizing public value
[@janssen2012]. For this project, the practical implication is a research
boundary: accessible records and working interfaces are intermediate artifacts,
whereas usefulness to residents requires separate empirical assessment.

PROV-DM distinguishes entities, activities and responsible agents
[@prov2013]. We use that distinction to separate a retained municipal edition,
the transformations applied to it and the ownership of the resulting packet.
Our receipts are a project-specific implementation of those concerns, not a
claim of complete PROV serialization or formal conformance. The W3C's Data on
the Web Best Practices adds an operational emphasis on provenance, quality,
version indicators and preservation [@dwbp2017].

Dataset documentation offers a complementary perspective. Datasheets describe
motivation, composition, collection and intended uses [@gebru2021]; data
statements make context and limits of generalization explicit [@bender2018].
The Davis claim ledger and data statement adapt those questions to a municipal
text deployment. They do not convert administrative text into a representative
sample of residents or describe a machine-learning training population.

The manuscript makes three bounded contributions: an explicit shared/local
ownership boundary; a reproducible, complete description of article-level
section counts in the accepted snapshot; and a publication workflow that uses
the external template's actual rendering APIs while retaining input and output
commitments. These are engineering and documentation contributions. Novel
civic outcomes, legal interpretation and model capability are outside the
reported evidence.
