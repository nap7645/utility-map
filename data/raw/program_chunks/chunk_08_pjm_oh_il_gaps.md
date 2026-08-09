# Cluster 8 — PJM Ohio + Northern Illinois — Gaps & Coverage Notes

## Utilities with verified rows (40 rows total)
Commonwealth Edison (ComEd) — 8 rows (Hourly Pricing RTP, Peak Time Savings, IL DG Rebate, SDVPP, DTOD/EV credit, C&I VLR, Net Metering/CEJA transition, EV charger rebate)
Ohio Power Company (AEP Ohio) — 4 rows (Residential TOU, PEV rate, Interruptible Power Rider, Net Metering/net billing) + Power Rewards Smart Thermostat = 5
Duke Energy Ohio — 7 rows (Rate TD, Rate TD-CPP, Rate RTP/Rider RTP II, Rider NM, Rider LM, Rider PLM, Rider TES)
Ohio Edison Company — 2 rows (Time-of-Day Option, Net Energy Metering Rider)
The Cleveland Electric Illuminating Company — 2 rows (Time-of-Day Option, Net Energy Metering Rider)
Toledo Edison Company — 2 rows (Time-of-Day Option, Net Energy Metering Rider)
AES Ohio (Dayton Power & Light) — 3 rows (Net Metering, EVSE Charger Rebate, Home EV Off-Peak Charging Rewards)
Cleveland Public Power — 2 rows (Net Metering Service, Capacity Enhancement Incentive Rate Schedule — closed to new post-2024)
Bowling Green Municipal Utilities — 1 row (Net Metering)
South Central Power Company (cooperative) — 1 row (Net Billing via Buckeye Power)
Buckeye Power Inc. — 1 row (QF/net-billed generation purchase rate, representing Ohio's rural co-op sector generally)
American Municipal Power Inc. (AMP) — 1 row (Community Energy Savings: Smart Thermostat Program, administered across ~10+ member municipalities)
City of Wadsworth (Wadsworth Electric) — 1 row (Community Energy Savings smart thermostat program)
City of Westerville (Westerville Electric Division) — 3 rows (Community Energy Savings thermostat DR, PowerUp Residential EV Off-Peak Charging, Commercial Solar Rebate)
City of Cuyahoga Falls (Cuyahoga Falls Electric) — 1 row (Schedule GSL/GSD on-peak demand ratchet, Demand-Charge relevant to BESS)

## Utilities checked with NO verifiable BTM-relevant program found (no row emitted)
- **Hamilton (OH) Municipal** — Utility page confirms net metering exists generically ("net metering policies can help solar owners") and provides Residential Solar Interconnection Standards PDF, but no specific compensation rate, TOU rate, or DR program could be verified from public sources within budget. Net metering terms likely negotiated per Hamilton Codified Ordinances (not accessed in full).
- **Orrville Utilities** — Full residential/commercial rate schedule reviewed (flat block rates, no demand response, no TOU, no published net-metering compensation rate — treatment of net excess generation is negotiated case-by-case, not published).
- **Painesville Municipal** — Utility website confirms it is a public power utility with own generation but provides no net metering rate, TOU rate, or DR program details; municipal utilities in Ohio are not required to follow the PUCO net metering rule and Painesville has not published its own policy online. Not confirmed as an AMP Community Energy Savings participant (only inferred from generic AMP-partnership language).
- **Westerville Electric Division net metering** — Westerville does not appear to run its own net metering compensation tariff; secondary sources suggest solar interconnection/net metering paperwork for Westerville addresses is handled through AEP Ohio (Westerville's likely wholesale/interconnection point), so no standalone Westerville net-metering row was created to avoid conflating with the AEP Ohio row.
- **Cuyahoga Falls Electric net metering** — Confirmed to exist ("one of 36 Ohio utilities offering net metering") but no specific compensation rate (1:1 vs. generation-only) could be independently verified from the city's published rate/ordinance pages within the search budget.

## Utilities in the cluster list that could not be researched at all (time/search-budget exhausted)
- No dedicated searches were completed for smaller municipals beyond those listed above (e.g., deeper Painesville/Hamilton ordinance-level detail) once the session's web-search quota (200 calls) was reached. Remaining research relied on direct page fetches (web_fetch) rather than new searches.

## Other notes
- Ohio's statewide net metering rule (PUCO-adopted, generation-only excess credit at unbundled generation rate, 120% of annual usage system-size cap) is confirmed to apply uniformly across AEP Ohio, Duke Energy Ohio, and the three FirstEnergy Ohio operating companies (Ohio Edison, CEI, Toledo Edison). AES Ohio's net metering is structurally similar (credited at Standard Offer/generation rate) though AES's rule citation was less explicit on the 120%-of-usage cap.
- Rural electric cooperatives (South Central Power, Buckeye Power's other 23 member co-ops) and municipal utilities are legally exempt from Ohio's statutory net-metering rule and set their own excess-generation compensation — South Central Power/Buckeye Power's move to hourly net billing (March 2022) is a useful, verified example of this divergence and is likely broadly representative of other Buckeye Power member co-ops (Buckeye Rural Electric, Consolidated Cooperative, Frontier Power, Guernsey-Muskingum, Mid-Ohio Energy, etc.) though each was not individually verified.
- ComEd's Scheduled Dispatch Virtual Power Plant (SDVPP) is newly approved (2026) and not yet operational — incentive/dispatch payment structure was not yet published; flagged as Proposed/pending with Medium confidence.
- Duke Energy Ohio's Rate RTP/Rider RTP II, Rate TD-CPP, Rider LM, Rider PLM, and Rider TES were identified from the utility's official PUCO tariff table of contents (P.U.C.O. Electric No. 19) but the underlying rate sheets (specific $/kWh, $/kW-month, or event-limit values) were not retrievable within the tools available (the tariff PDF is very large and the fetch only returned the table of contents/index pages, not the full sheet text) — these rows are flagged Low confidence pending direct sheet-level verification.
- AEP Ohio's PEV (Plug-In Electric Vehicle) rate and Time-of-Use rate were verified directly from the utility's own program pages with full rate detail (High confidence) — among the most complete Ohio IOU data points found in this cluster.
