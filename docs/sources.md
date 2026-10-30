# Davis source configuration review

Reviewed 2026-10-30. These are configuration observations, not a comprehensive
source collection or legal-code verification certificate.

| Decision | Primary evidence | Scope |
| --- | --- | --- |
| eCode360 municipality `DA4922` | [Provider TOC](https://ecode360.com/DA4922), [provider help](https://ecode360.com/help/DA4922), [City-hosted municipal-code attachment](https://documents.cityofdavis.org/Media/Default/Documents/PDF/CityCouncil/Recreation-and-Park-Commission/Agenda/20240918/05C-Chapter%2027%20MC%20Update%20SR.pdf) | The City-hosted attachment names the same provider identity. No full corpus was acquired in this configuration review. |
| Forecast zone `CAZ153` | [NWS points response](https://api.weather.gov/points/38.5449,-121.7405), [NWS point forecast](https://forecast.weather.gov/MapClick.php?lat=38.5449&lon=-121.7405) | Direct points request returned HTTP 200, Davis/CA, county `CAC113`, timezone America/Los_Angeles and forecastZone ending `/CAZ153`. Old Sacramento-area zone numbers are not used. |
| Yolo County `06113` | NWS county `CAC113` and radio SAME `006113` in the same points response | County policy; this is not a city boundary. |
| Official City news | [City RSS](https://www.cityofdavis.org/Home/Components/RssFeeds/RssFeed/View?ctID=5&cateIDs=1) | Direct HTTP 200 returned RSS 2.0 with City title, channel and actual dated news items. Category 1 is the selected feed, not all City communications. |
| Council and commission references | [Council meetings](https://www.cityofdavis.org/city-hall/city-council/city-council-meetings), [agenda directory](https://www.cityofdavis.org/city-hall/agendas), [City Granicus publisher](https://davis.granicus.com/ViewPublisher.php?view_id=6) | Official City pages were discoverable in indexed primary pages; direct City homepage and agenda reads returned HTTP 403. Runtime must report access failure, never an empty-success archive. |
| DJUSD reference | [District homepage](https://www.djusd.net/) | Primary district page identifies Davis Joint Unified School District. Generic closure parser has not been qualified here, so school monitoring remains disabled. |

## Enabled monitoring policy

Eight adapters are selected: earthquake, weather, airquality, wildfire, drought,
smoke, roads and fuel. The USGS past-hour all-event feed is filtered around Davis
at magnitude 4 or greater within 200 km. It cannot reconstruct polling gaps.
Air quality uses a 50 km public-station radius and ZIP 95616 for optional keyed
access; nearby observations are not citywide exposure measurements. Wildfire
policy includes Yolo and adjacent Sacramento, Solano, Napa, Lake and Colusa
counties with a 150 km radius. Smoke bounds span longitude -121.90 to -121.55
and latitude 38.40 to 38.72. These are explicit operating choices rather than
provider-authoritative administrative polygons. Highway 80 and 113 queries use
the existing Caltrans road-condition adapter. EIA fuel prices are California
statewide weekly averages, not local retail prices.

The retained `region-config/v1` contract requires all adapter sections. Values
for disabled tide, marine, fisheries, harbor, vessel, permit and Coast Guard
adapters are compatibility data only. They are intentionally excluded from
`enabledMonitors`. Do not infer coverage from the presence of those fields.
PSPS and school monitors also remain disabled until local parser/live acceptance.

## Acceptance boundaries

Read the actual output health receipts after each collection. Config validation
proves schema, identity and monitor admission; it does not prove upstream uptime,
complete event archives, hazard absence, legal currency, predictive value, or
native rendering. Source references retain their own terms; article bodies must
not be republished merely because their links can be discovered. The package's
reference manuscript reports its own inputs; no Davis findings are inherited.

## Recorded configuration checks

The same-attempt direct HTTP receipts returned 200 for NWS points and City RSS,
and 403 for City agendas and the eCode360 help page. Provider identity was
independently visible through indexed first-party provider and City-hosted
materials; direct scraper access remains a separate browser acceptance step.
The captured RSS parsed as RSS 2.0 with 35 items. The shared deployment loader
accepted Davis configuration and rejected changed profile binding, parent-path
output escape, an unknown monitor and duplicate source identity. These checks
validate the configured seam only; they do not certify the complete application.
