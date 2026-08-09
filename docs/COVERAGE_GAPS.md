# Appendix: per-cluster research gap notes

_Compiled from the individual research agents. Clusters 01 (MISO North), 03 (MISO IA/IL/MO) and 06 (PJM Mid-Atlantic) have no gaps file — those agents were cut off by a session limit after writing their CSV but before writing notes._


---

## Source: chunk_02_miso_wi_mi_gaps.md

# Cluster 2 — MISO Wisconsin & Michigan: Research Gaps

## Utilities with no retail tariffs found (structural gap, not an oversight)

- **Dairyland Power Cooperative (WI)** — Confirmed to be a generation & transmission (G&T) wholesale cooperative that supplies power to 24 member distribution cooperatives across WI/MN/IA/IL. It does not sell retail power directly to end-use customers and therefore has no retail TOU/DR/EV/export-compensation tariffs of its own to report. Its member co-ops (which are NOT on the target list for this cluster) hold the retail tariffs. Battery storage and solar activity by Dairyland is limited to wholesale-side generation projects (e.g., USDA PACE-funded battery/solar projects), not customer-facing programs.
- **Wolverine Power Cooperative (MI)** — Could not locate a working corporate website. `wolverine.org` is a squatted/for-sale domain, `wolverinepower.com` belongs to an unrelated company (Wolverine Power Systems, a Generac generator dealer), and `wolverinepower.coop` returned an empty/unresponsive page. Wolverine Power Cooperative is understood to be a Michigan G&T wholesale cooperative (headquartered in Cadillac, MI) supplying member distribution co-ops, similar in structure to Dairyland — meaning it likely has no direct retail tariffs of its own either, but this could not be confirmed with a live source in this session.
- **Michigan Public Power Agency (MPPA)** — `mppa.org` and `mppa.org/about` returned near-empty responses (likely JS-rendered content not captured by static fetch). MPPA is understood to be a joint action agency that provides wholesale power supply, financing, and shared services to its municipal member utilities (e.g., small Michigan municipal electric systems not on this cluster's target list) — it is not itself a retail utility and would not be expected to hold retail TOU/DR/EV/export tariffs. This could not be verified with a live source in this session.

## Utilities fully researched with programs found

The following 16 utilities were successfully researched with verified tariff/program data captured in the CSV: Wisconsin Electric Power Co (We Energies), Wisconsin Public Service Corp, Wisconsin Power & Light Co (Alliant Energy), Madison Gas and Electric Co, Northern States Power Co - Wisconsin (Xcel Energy), Superior Water Light & Power Co, WPPI Energy, Consumers Energy Co, DTE Electric Co, Upper Peninsula Power Company (UPPCO), Upper Michigan Energy Resources (UMERC), Lansing Board of Water & Light, Holland Board of Public Works, Traverse City Light & Power, Cloverland Electric Cooperative, Great Lakes Energy Cooperative, Indiana Michigan Power - Michigan.

## Notes on partial/lower-confidence findings within the covered utilities

- **UMERC (Upper Michigan Energy Resources)**: Its own MPSC No. 1 tariff book (combined WEPCo/WPSC rate zones) confirms rate codes Rg2 (residential TOU) and Cp-I (large C&I interruptible rider) exist, but the fetched tariff excerpt was table-of-contents/index level only — specific $/kWh and $/kW figures were not recoverable from the extracted text, so those two rows are marked Low confidence. The Distributed Generation Program (DG-1) tariff was fetched in full and is High confidence.
- **Northern States Power Co - Wisconsin (Xcel)**: Interruptible Service Option Credit — no published $ credit figures found; marked Low confidence.
- **DTE Electric**: Several C&I interruptible/curtailable riders (D3.3, D8, Rider 10, Rider 12, Rider 1.1 Metal Melting) do not publish exact $ credit amounts on the public site; marked Medium confidence.
- **Lansing Board of Water & Light**: RES22 (separately metered EV charging rate) tariff exists but rate figures were not present in the extracted PDF text; marked Low confidence.
- **Indiana Michigan Power - Michigan**: DG Rider / legacy Net Metering Service Rider 1 (NMS-1) confirmed to exist (referenced on the EV charging page) but no dedicated tariff page/PDF with credit rates was fetched; marked Low confidence. The RS-PEV EV charging tariffs (Options 1-3) are High confidence with full published rates.
- **Holland Board of Public Works / Traverse City Light & Power / Cloverland Electric Cooperative / Great Lakes Energy Cooperative**: All fully verified with High confidence tariff/program pages and PDFs.

## Search/access constraints encountered

- WebSearch tool budget was exhausted partway through the session (200/200 calls used), forcing exclusive reliance on direct URL fetches (mcp__workspace__web_fetch) with known or guessed utility URL patterns for the remainder of the research.
- UPPCO's `wp-content/uploads` PDF paths returned empty content via direct fetch; the same files hosted on UPPCO's CloudFront CDN (`d2x43qaqyo0a2i.cloudfront.net`) worked and were used instead.
- `umerc.com` is a squatted/parked domain unrelated to Upper Michigan Energy Resources; the real corporate site is `uppermichiganenergy.com`.
- `wolverine.org` and `wolverinepower.com` do not belong to Wolverine Power Cooperative (see gap note above).


---

## Source: chunk_04_miso_south_gaps.md

# Cluster 4 — MISO South: Gaps and Non-Findings

## Utilities checked with no verifiable program found (no row emitted)
- **Entergy Arkansas** — No residential TOU, RTP, or CPP/PTR rate found (only inclining-block or standard schedules referenced); no dedicated storage-incentive or VPP program found (unlike MS/LA/TX/NOLA sister companies).
- **Entergy Louisiana** — No residential TOU/RTP rate could be verified as currently active/marketed (AFDC references an "EV TOU Rate" system-wide but no LA-specific rider PDF was located); no residential storage-incentive or VPP program found (the New Orleans VPP is City-Council/ENO-specific, not ELL).
- **Entergy Mississippi** — No residential or C&I TOU/RTP rate found; no dedicated EV rate/rider found (only system-wide eMobility infrastructure riders); no interruptible/curtailable C&I rider text located (unlike LA's Rider IES/EIO) — EML almost certainly has an equivalent MISO LMR/interruptible rider but the specific tariff PDF was not found in this pass.
- **Entergy New Orleans** — No TOU, RTP, EV-specific rate, or C&I interruptible rider found; ENO's regulatory structure (City Council, not LPSC) means it does not share Entergy Louisiana's Rider IES/EIO.
- **Entergy Texas** — No residential TOU or storage rebate beyond the FranklinWH/Tesla VPP found; no CPP/PTR program found.
- **Southwestern Electric Power Co (SWEPCO)** — Could not verify exact net-metering compensation rate or interruptible rider ($/kW or terms) for AR, LA, or TX jurisdictions in this pass; tariff books are large PDFs that were not fully parsed for the specific rider text (LMSOP terms referenced only in secondary/historical sources). No TOU, EV, storage-incentive, or VPP program found.
- **Mississippi Power (Southern Co)** — No dedicated EV rate/tariff exists yet (company states rebates only, "plan to have rates to benefit EV charging" in the future); no residential TOU rate found (R-59/R-60 are inclining-block, not TOU); no DR/interruptible C&I rider (e.g., PowerSecure/curtailable) located; no storage-incentive or VPP program found.
- **Lafayette Utilities System (LUS)** — Net metering confirmed, but the specific compensation rate (1:1 vs. avoided cost, and $/kWh value) was not published in the pages retrieved; no TOU, DR, storage, or EV program found.
- **Alexandria (LA) Utilities** — Not located; no net-metering, DR, TOU, storage, or EV program could be found or verified for this municipal utility in this pass. Flagged as an open gap requiring direct outreach or a Louisiana PSC filing search (note: Alexandria's electric utility status/vertical structure should be reconfirmed — no independent tariff was found).
- **Louisiana Energy & Power Authority (LEPA)** — LEPA is a joint-action wholesale power agency for ~20 member municipalities; it does not itself retail to end customers or set net-metering tariffs. Individual member cities (e.g., Plaquemine) have their own net-metering rules per Louisiana's municipal-utility statute, but city-by-city tariffs were not individually verified beyond Plaquemine being referenced. Only one general row was emitted; most LEPA member cities remain unverified.
- **DEMCO (Dixie Electric Membership Corp)** — Net metering (avoided cost) verified with a hard number; a "Residential Time-of-Use Rate" page exists but is JavaScript-gated and its rate structure/values could not be extracted — row emitted with Low confidence and blank rate fields.
- **SLECA / Louisiana co-ops** — SLECA net metering verified in detail. Other Louisiana co-ops (e.g., Beauregard Electric, Claiborne Electric, Jeff Davis Electric, Northeast Louisiana Power, Washington-St. Tammany Electric, Concordia Electric) were NOT individually researched — treat as an open gap; likely similar avoided-cost net-metering tariffs under the same 2019 LPSC General Order R-33929 framework.
- **Arkansas Electric Cooperative Corp (AECC)** — AECC is a generation & transmission cooperative serving ~17 distribution co-op members; only one representative member tariff (Carroll Electric) was checked as a proxy. Individual AECC member co-ops (North Arkansas Electric, Woodruff Electric, South Central AR Electric, etc.) were not each verified — treat as open gap.
- **Ozarks Electric Cooperative** — Net metering verified; no TOU, DR, storage, or EV program found/verified.
- **Conway Corp** — Net metering confirmed to exist but compensation methodology/rate not found in pages retrieved (row emitted at Low confidence); no DR, TOU, storage, or EV program found.
- **North Little Rock Electric (NLRED)** — Net metering verified in detail; no TOU, DR, storage, or EV program found.
- **East Mississippi Electric Power Association (EMEPA)** — Net metering existence confirmed but exact rate/tariff PDF not located (Low confidence, no rate values); no DR, TOU, storage, or EV program found.
- **Coast Electric Power Association** — Rooftop net metering and a subscribed/community solar rate ($18.10/kW-month) both verified; no DR, TOU (beyond the solar subscription), storage-incentive, or EV program found.
- **Jackson (MS) area co-ops** — Central Electric Power Association (headquartered Carthage, MS, serves Jackson-area exurbs) and Southern Pine Electric Power Association were identified as candidates but could NOT be verified for any program in this research pass (web search budget was exhausted before dedicated searches could be run) — no rows emitted per the "never invent a row" rule. This is a genuine open gap.

## Utilities/entities explicitly flagged as NON-MISO (per cluster instructions)
- **Tallahatchie Valley Electric Power Association (TVEPA)** — TVA service territory (northeast MS), not MISO. No row emitted.
- **Pontotoc Electric Power Association** — TVA service territory, not MISO. No row emitted.
- **Northcentral Electric Cooperative (MS)** — TVA service territory (DeSoto/Marshall/Tate/Lafayette counties), not MISO. No row emitted.
- **North East Mississippi Electric Power Association (NEMEPA)** — TVA service territory, not MISO. No row emitted.
- General note: TVA directly and indirectly serves a large swath of northeast Mississippi (Alcorn, Attala, Benton, Calhoun, Chickasaw, Choctaw, Clay, DeSoto, Grenada, Itawamba, Kemper, Lafayette, Leake, Lee, Lowndes, Marshall, Monroe, Neshoba, Newton, Noxubee, Oktibbeha, Panola, Pontotoc, Prentiss, Quitman, Rankin, Scott, Tallahatchie, Tate, Tippah, Tishomingo, Tunica, Union, Webster, Winston, Yalobusha counties) via municipal and cooperative distributors — none of these are in MISO and none were researched for this cluster beyond confirming their non-MISO status.
- East Mississippi Electric Power Association and Coast Electric Power Association were treated as MISO/Entergy-footprint cooperatives (not TVA) based on their service territories (east-central MS / Gulf Coast MS respectively) — this was not independently cross-checked against MISO's member list and should be verified if precision matters.

## Data-quality caveats on rows that WERE emitted
- Several rows (Conway Corp, Lafayette Utilities System, East Mississippi EPA, SWEPCO net metering AR/LA, SWEPCO LMSOP, Cleco IES rider, LGS-TOU-17 for Mississippi Power) are marked **Low or Medium confidence** because the specific $/kWh or $/kW rate could not be extracted from the pages retrieved — only the existence and general structure of the program was confirmed. These are flagged rather than omitted per the instruction that a verified row with a real link beats an omission, but the incentive_value_usd / peak_offpeak_rates fields were deliberately left blank rather than guessed.
- The Mississippi Power LPO-TOU rate row uses 2021-vintage dollar figures pulled from an older PDF (LPO-TOU-15I) because the current schedule (LPO-TOU-16, effective 6/20/2022) PDF was not directly retrieved; the tariff code and window structure should still be broadly representative but the cents/kWh and $/kVA figures are likely stale by 2026.
- Research was cut short by exhaustion of the session's web-search quota (200/200 used) partway through verification; remaining gaps above (Alexandria LA, most individual LA/AR co-ops beyond the ones named, Jackson MS co-ops, exact SWEPCO and Entergy AR/LA/MS TOU rates) reflect that constraint rather than confirmed absence of programs.


---

## Source: chunk_05_in_ky_gaps.md

# Cluster 5 (Indiana + Kentucky) — Research Gaps

## Utilities covered with at least one verified row
NIPSCO, Duke Energy Indiana, AES Indiana (formerly IPL), Indiana Michigan Power (AEP/PJM), CenterPoint Energy Indiana South (formerly Vectren), Hoosier Energy, Wabash Valley Power Alliance, Jackson County REMC, Richmond Power & Light, Louisville Gas & Electric, Kentucky Utilities, Duke Energy Kentucky (PJM), Kentucky Power (AEP/PJM), East Kentucky Power Cooperative, Big Rivers Electric (via member co-op Kenergy), Owensboro Municipal Utilities.

## Utilities checked but with little/no verifiable retail program found
- **Indiana Municipal Power Agency (IMPA)**: IMPA is a wholesale joint-action agency supplying 53 municipal members; it does not publish a single retail tariff. Its board adopted a resolution permitting purchase of excess member-generated energy, but no published $/kWh rate, TOU rate, or DR program could be found at the IMPA (wholesale) level. Retail net metering / EDG-equivalent terms are set independently by each of its 53 member municipal utilities (e.g., Richmond P&L, which is covered separately). Flagging as a gap for IMPA itself — recommend researching individual IMPA member cities if per-city granularity is needed.
- **Anderson Municipal Light & Power**: Confirmed net metering is offered (city ordinance / IURC filing 50507), but no specific $/kWh credit rate, cap size, or TOU/DR program details could be located in public search results. Rate schedule details were not found in an accessible tariff PDF.
- **Jackson County REMC**: Confirmed net-metering-like interconnection exists (rate schedule "R13 Rate-G" referenced) and a smart-thermostat DR pilot (with Hoosier Energy/NRECA) is documented in detail and included as a row. However, the specific solar/DG credit rate ($/kWh) for Jackson County REMC could not be verified from public sources — flagged Low confidence would have been needed; no export-comp row emitted for this utility beyond noting the pilot.
- **Big Rivers Electric**: As a generation & transmission cooperative, Big Rivers does not serve retail customers directly — retail net metering/DG terms are set by its three member cooperatives (Kenergy Corp, Meade County RECC, Jackson Purchase Energy Corp). Only Kenergy's program was verified (interconnection required, capacity-constrained by substation, no published $/kWh credit rate found). No verifiable TOU, DR, or EV program found at the Big Rivers G&T level itself.
- **East Kentucky Power Cooperative**: EKPC is also primarily a G&T cooperative; the interruptible industrial service program is real and documented (via PSC-filed Industrial Power Agreements), and net metering/DG credit terms are set per member distribution cooperative rather than uniformly by EKPC. No EKPC-level TOU, CPP, storage incentive, VPP, or EV program could be verified.

## Program categories not found for any IN/KY utility in this cluster
- No dedicated **Storage-Incentive** (upfront $/kWh rebate for BESS) program was found at any Indiana or Kentucky utility in this cluster (Duke's PowerPair/Power Manager Battery Control programs are confirmed only in the Carolinas, not Indiana or Kentucky — excluded for lack of verification).
- No **VPP** (aggregated dispatchable BESS fleet) program beyond Hoosier Energy's broader CPMP (which is closer to C&I curtailment/capacity) was verified for any utility in this cluster.
- No residential **RTP-Rate** (hourly/real-time indexed) retail rate was found for any IN/KY utility; NIPSCO's Rate 831/832 and I&M's curtailment riders are large-C&I products tied to wholesale prices but are not true hourly retail RTP tariffs.
- Kentucky Power's residential EV rate / managed charging program (if any, beyond the interruptible/net-metering programs found) could not be verified — Kentucky Power's EV program specifics were not found in search results (only Kentucky Power's general PJM DR/net-metering info was verifiable).
- Duke Energy Kentucky's demand response / interruptible program (analogous to LG&E/KU's Curtailable Service Rider or Duke Indiana's IDR) could not be located with a working source link; only a Time-of-Day rate tariff reference (partially confirmed, low confidence, cancelled/superseded tariff page) was found.

## Utilities not independently researched in depth (time-boxed)
- Anderson Municipal Light & Power — only net metering existence confirmed, not rate specifics (see above).
- Indiana Municipal Power Agency — wholesale-only entity, no direct retail tariff (see above).

## Notes on RTO/market labeling
- LG&E and Kentucky Utilities are **non-RTO** (self-supply / not members of MISO or PJM as a bundled retail utility) — labeled `Non-RTO` in the `rto` column per cluster instructions, even though this value is not in the base schema enum. This is intentional per the cluster note to flag LG&E/KU as non-RTO.
- Duke Energy Kentucky and Kentucky Power are labeled `PJM` (AEP and Duke transmission territory in Kentucky is functionally under PJM).
- Big Rivers Electric and Owensboro Municipal Utilities are labeled `MISO` (Big Rivers joined MISO as a transmission-owning member in 2013; western KY footprint is inside the MISO footprint) — flagged Low/Medium confidence on program specifics given limited published detail.


---

## Source: chunk_07_pjm_south_gaps.md

# Cluster 7 — PJM South (VA/WV/MD) — Research Gaps

## Utilities checked with NO verifiable BTM PV+storage-relevant program found (beyond what's in the CSV)

- **Wheeling Power Co (AEP - West Virginia)**: Confirmed net metering (shared PSC case/tariff with Appalachian Power WV, included in CSV). Could not verify whether Wheeling Power offers its own Off-Peak EV charging tariff (RS-PEV) or a Smart TOU/Smart Demand plan analogous to Appalachian Power's — Wheeling Power's public-facing rate pages largely redirect to Appalachian Power's tariff library and don't list EV/TOU schedules distinctly. Likely shares APCo WV's tariff structure but this was not confirmed with a direct source.
- **Old Dominion Electric Cooperative (ODEC)**: ODEC is a generation & transmission (wholesale) cooperative supplying 11 member distribution co-ops (including NOVEC, REC, SVEC, BARC, CVEC — all covered individually in the CSV). ODEC itself does not administer retail rate schedules, net metering, or DR programs directly to end customers; its "Energy Programs" page describes efficiency/DR support delivered through member co-ops rather than a distinct ODEC-branded program. No standalone row was created for ODEC; its member co-ops carry the actual customer-facing programs.
- **Bristol Virginia Utilities (BVU Authority)**: Confirmed it is a municipal electric utility with a residential rate schedule (Schedule RS: ~$31.50 customer charge, ~7c/kWh seasonal energy charge). Could not verify whether BVU offers net metering, TOU, EV rates, or DR programs — search results only noted that as a municipal utility, net metering participation is optional (not state-mandated) and did not confirm BVU has adopted it. Recommend direct outreach to BVU Authority or review of their tariff PDFs at bvua.com.
- **Town of Front Royal (Department of Energy Services)**: Confirmed as one of Virginia's ~16 municipal electric systems (~8,000 customers). Could not verify net metering, TOU, EV rate, or DR program details — public site (frontroyalva.com) references rate schedules and municipal code (Chapter 70-23/§134-71) but no program specifics were retrievable within the search budget. Note: Virginia Code §56-594 net metering provisions become effective for additional utility classes January 1, 2027, which may extend/clarify municipal utility obligations — worth re-checking after that effective date.
- **Manassas City Electric**: Net Metering Policy (2015) confirmed to exist (row included, Low confidence) but the specific credit rate, true-up mechanics, and system size caps were not published on the public-facing page; only a policy landing page with no rate table was found.
- **NOVEC (Northern Virginia Electric Cooperative)**: Net metering confirmed active since 2003 (row included, Low confidence) but no public rate schedule/rider document with credit mechanics (1:1 vs. avoided cost, caps, true-up timing) was located — NOVEC's site defers to a Net Metering Agreement obtained on request rather than publishing it.
- **BARC Electric Cooperative — battery storage / SolarizeBARC**: BARC's "SolarizeBARC" program is described as combining "utility scale, rooftop, battery storage, and community solar," but no specific member-facing storage incentive, rebate amount, or program terms could be found — appears to be more of a utility-side/community-scale initiative than a BTM residential storage rebate. Also could not verify specifics of BARC's "Thermostat Program" (DR-BYOT) beyond its existence (page found, no incentive amount/event terms published).
- **Shenandoah Valley Electric Cooperative (SVEC) — Beat the Peak**: Confirmed a peak-conservation alert program exists, but could not verify any bill credit or cash incentive — appears to be a voluntary conservation appeal only (Low confidence, included in CSV for completeness).
- **Central Virginia Electric Cooperative — Solar Share**: Confirmed a community solar tariff exists (SCC-approved Community Solar Order), but subscription pricing/credit mechanics were not in the retrievable page text (only a link to the PDF order, not parsed).

## Utilities/topics not reached due to time/search-budget constraints

- **NC and TN utility detail beyond Dominion's parenthetical NC service territory**: The cluster brief's utility list did not name separate NC or TN operating companies distinct from those already covered (Dominion's Virginia tariff also covers its small NC service area under the same Schedule 1/1S/1T structure — not separately verified for NC-specific riders).
- **WV PSC docket numbers**: Net metering reform outcomes for Appalachian Power/Wheeling Power (12.4c/kWh) and Mon Power/Potomac Edison (9.15–9.34c/kWh) were sourced from news coverage (WV MetroNews, West Virginia Watch, Dominion Post) rather than the primary PSC case order/docket PDF — recommend pulling the actual PSC order for docket-number-level citation if higher confidence is needed.
- **Virginia Clean Economy Act (VCEA) storage mandate**: Confirmed VCEA requires Dominion and Appalachian Power to pursue significant utility-scale/company-owned energy storage targets (widely reported ~2,700 MW by 2035 for Dominion), but this is a utility-owned generation/storage procurement mandate, not a customer-enrollable BTM program, so no row was created per the schema's customer-program focus. Flagging here since the cluster notes specifically asked for it to be captured.
- **Dominion Schedule GS-3/GS-4 demand-charge structures and standby generation Rider GEN** for C&I BESS peak-shaving economics were identified in the tariff index but not opened/parsed in detail — potential additional Demand-Charge category rows for LargeC&I customers.
- Additional WebSearch queries were not possible after the session's search budget (200 calls) was exhausted mid-research; remaining gaps (NOVEC net metering rate detail, CVEC Solar Share pricing, Wheeling Power EV/TOU, Bristol VA Utilities, Front Royal) would benefit from direct web_fetch of utility tariff PDFs in a follow-up pass.


---

## Source: chunk_08_pjm_oh_il_gaps.md

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


---

## Source: chunk_09_rto_wholesale_gaps.md

# Cluster 9 — RTO Wholesale Products: Gaps and Unverified Items

## Covered with High/Medium confidence
- PJM: Capacity Performance product, Demand Resource, BRA clearing prices for 2025/2026, 2026/2027, and 2027/2028 delivery years (all by RTO/LDA where prices diverged), Emergency Load Response, Economic Load Response, Synchronized/Non-Sync/Secondary Reserve (structural), RegA and RegD formulas and current values, DA/RT energy arbitrage (TB4 spreads), Order 2222 DER aggregation rules, Price Responsive Demand.
- MISO: DRR-I, DRR-II, LMR (including the LMR-DR/LMR-BTMG split and the DLOL availability-based accreditation reform — confirmed this is live and cuts LMR value), EDR (confirmed being phased out), PRA clearing prices for 2025/2026 and 2026/2027 by LRZ/sub-region, Regulating/Spinning/Supplemental/Short-Term Reserve, ARC opt-out rules, Order 2222 compliance status/timeline, ESR participation model, DA/RT LMP spread commentary by hub.

## Could not verify / low confidence — flagged in the data
1. **PJM Non-Performance Charge Rate (current $/MWh value).** Confirmed the formula concept (Net CONE / EFORd-adjusted factor) and that aggregate 2025 charges were estimated at $1–2 billion system-wide, but could not pull the exact current per-MW Non-Performance Charge Rate or Bonus Rate for the 2025/2026 or 2026/2027 Delivery Year from Manual 18 / Attachment DD Section 10A directly (paywalled/complex PDF navigation). Marked Medium confidence.
2. **PJM Synchronized Reserve, Non-Synchronized Reserve, and Secondary Reserve — actual clearing price ranges.** Found the market structure and the 2023 reserve price formation reform (Tier 1/Tier 2 consolidation, DA/RT alignment) but could not extract specific $/MWh clearing price data for 2025/2026 from Data Miner 2 or the IMM State of the Market report tables (data is in charts/tables not extracted by text search). Marked Low/Medium confidence — flagged as needing direct Data Miner 2 or IMM report pull.
3. **PJM RMCCP/RMPCP current numeric values.** Have the 2023 RMCP average ($21.08/MW) and the full payment formulas, but not more recent (2025/2026) RMCCP/RMPCP average values — PJM's Regulation Redesign (Oct 2025 Phase 1, Oct 2026 Phase 2) also complicates a clean "current" number since the RegA/RegD product is being replaced.
4. **MISO Short-Term Reserve (STR) clearing price.** Confirmed this is a new 30-minute product tied to MISO's 2025 shortage-pricing reforms, but could not extract a numeric average clearing price from the IMM Fall 2025 Quarterly Report (data in tables/charts not captured by search extraction). Marked Low confidence.
5. **MISO DA/RT LMP spread by specific hub (Indiana/Michigan/Minnesota Hub) — full-year 2025 annualized average.** Only found a specific February 2026 Winter Storm Fern data point (148% RT vs DA premium at Indiana Hub); a clean full-year hub-by-hub average TB spread was not located. Marked Low confidence.
6. **PJM zone-by-zone BRA breakdown for 2026/2027 and 2027/2028.** Both auctions cleared at the FERC price cap RTO-wide, so no sub-LDA breakdown was needed/available for those years (this is a real result, not a gap) — only the 2025/2026 auction had LDA-level divergence (BGE, Dominion).
7. **MISO Order 2222 — DRR Type I rejection detail.** Confirmed FERC rejected using the 1 MW-minimum DRR Type I model as an Order 2222 vehicle (violates the 0.1 MW minimum), but the current interim participation pathway for small DERs before the 2027/2029 DEAR phases was not fully clarified.

## Not checked
- PJM Manual 11 Section 12 full text for Price Responsive Demand quantitative parameters (only summary-level detail obtained).
- MISO Module E-1 full tariff text for exact ESR minimum size and metering language (used FAQ/help-center summary instead of primary tariff redline).
- Historical (pre-2024) PJM Synchronized Reserve and MISO ancillary clearing price trends for context/comparison.

