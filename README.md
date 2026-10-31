# Davis CA Intel

Civic intelligence for Davis, California, built as a thin deployment of
[region-intel](https://github.com/docxology/region-intel). This repository owns
Davis identity, source selection, monitor policy and regional evidence. Shared
acquisition, search, RAG, analytics, API, publication and manuscript methods live
in the pinned dependency; there is no copied application implementation here.

## Run

```sh
bun install --frozen-lockfile
bun run validate
bun run source-discovery
bun run news
bun run gov-meetings
bun run alerts
bun run gui
bun run pages:export
bun run pages:validate
```

`bun run scrape`, `bun run verify` and `bun run export` acquire, verify and export
the Davis municipal code from eCode360 municipality `DA4922`. Browser acquisition
requires Chromium (`bunx playwright install chromium`). Optional model-backed
features require the configured Ollama/OpenRouter and Chroma services. No model
response or uncollected legal corpus is fabricated when those inputs are absent.

## Regional policy

`region.json` is the deployment entry point. `configs/davis-civic.json` defines
independent output/vector/calendar identity. `configs/davis-region.json` defines
NWS zone `CAZ153`, Yolo County FIPS `06113`, Davis-centred earthquake/air-quality
and wildfire filters, a bounded smoke watch area and highways 80/113. Coordinates,
radii and map bounds are monitoring policy, not surveyed city boundaries.

The enabled inland monitors are earthquake, weather, air quality, wildfire,
drought, smoke, roads and California statewide fuel prices. Statewide fuel data
is not a Davis pump-price survey. The full v1 policy schema retains disabled
coastal fields for compatibility; tides, tsunami, marine, marine forecast,
fishing, Coast Guard, harbor dredging, PacFIN and AIS are not Davis coverage.
Permits, school-closure inference and PG&E PSPS are also disabled pending their
own local adapter acceptance. DJUSD is a reference source only.

The configured publication target is
[the Davis project site](https://docxology.github.io/davis-ca-intel); the public deployment is separately checked after each accepted publication.

## Evidence and documentation

[Source review](docs/sources.md) records the official identity/zone evidence and
known access restrictions. City RSS returned actual XML during configuration
review, while the City homepage and agenda pages returned HTTP 403. A source
catalog is not collection completeness. A passing local gate is not a guarantee
of current upstream availability or legal accuracy.

Generic module documentation and the evidence-bound reference manuscript live
in [region-intel](https://github.com/docxology/region-intel/tree/main/docs).
Its recorded Crescent City findings must never be relabelled as Davis results.
The accepted Davis seed contains only Davis municipal evidence. No Crescent corpus or findings are imported.

See the [accepted municipal edition and exact input hashes](docs/edition.md) and
[acquisition/promotion procedure](docs/acquisition.md).
