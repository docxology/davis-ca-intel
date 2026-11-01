# Introduction {#sec:introduction}

Local civic information is distributed across municipal codes, agency notices,
meeting references and time-sensitive feeds. Combining these materials creates
two distinct problems: implementing reusable data-handling methods and deciding
which sources, geographic policies and interpretations belong to a locality.
A coastal application's defaults are especially unsuitable as implicit policy
for an inland city. A second deployment therefore provides a useful engineering
case for examining the boundary between shared computation and local evidence.

This paper concerns Davis, California, in Yolo County. It describes the public
Davis repository and its dependency on Region Intel. The original Crescent City
application is a compatibility preset in that package; its manuscript findings
and coastal source coverage are not Davis observations. The case study asks
whether deployment identity, accepted corpus evidence and manuscript numbers
can remain independently attributable while implementation is shared.

The design draws on the distinction between provenance entities, activities and
responsible agents in PROV-DM [@moreau2013prov]. Input hashes and execution
receipts are operational commitments, not a claim that this implementation is a
complete PROV serializer. FAIR provides a relevant vocabulary for reusable
metadata and identifiable inputs [@wilkinson2016fair]; this paper does not claim
a formal FAIR assessment or unrestricted redistribution rights. The following
sections describe a reproducible engineering record, rather than an assessment
of governmental performance or community outcomes.
