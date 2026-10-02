# Rank 1 plan: bill structure, LMP history, hosting capacity, aggregators

Status: draft v1, 2026-10-02. Starts after the Rank 0 audit passes (SPEC 6.2). Facts marked (verify) were not checked this session.
Rules carried over: Definition of done = a different agent verified it, with evidence (SPEC 5). Max 3 agents, Sonnet for breadth, Opus for precision. Source tiers Primary/Secondary/Unverified. A blank beats a guess. Nathan pushes and re-runs `snapshot_boundaries.py`.

## 0. Why these four, and how they connect (the multiplier lens)
- **Bill structure** says what a kWh, a kW and a time of day cost the customer: the base for every savings number.
- **LMP history** says what the wholesale market pays or charges at the same time: the arbitrage and VPP revenue ceiling.
- **Hosting capacity** says whether the grid lets the customer export at all, and how fast and at what cost: a gate on PV+BESS, not a revenue stream.
- **Aggregators** say who can monetize the customer's flexibility today, and in which program or market.
A multiplier = a territory where a TOU/demand-charge structure (bill) + an export rule (interconnection, already in Rank 0 data) + a paid DR path (programs/aggregator) stack. Build order below follows that dependency.

## 1. Full bill structure (do first)
**Goal.** For every researched territory, the residential and small-C&I default tariff plus the main optional rates, in machine-readable form: fixed charge, energy tiers/TOU periods and prices, demand charges, seasonal splits, riders that scale with kWh, NEM/export credit linked to the existing `programs`/`interconnection` rows.
**Sources.** (1) OpenEI Utility Rate Database (URDB) API: the repo already uses `api.openei.org` per project notes; base layer, free, JSON in SAM-compatible structure; known stale and incomplete for many co-ops and munis (verify current API/key terms). (2) Utility tariff PDFs and web pages for the gap-filling: the same pages the presence scans already cite. (3) PUC tariff dockets for IOUs. (4) Commercial feeds (Arcadia/Genability, WattBuy) only if URDB coverage is too thin: costs money, decide later.
**Data model.** New `data/processed/tariffs.csv` + `tariff_periods.csv` (one row per rate schedule / per energy-or-demand period) keyed on `eia_id` + `rate_schedule`. Fields: sector, rate name, effective date, fixed $/mo, energy $/kWh by period (TOU window, season), demand $/kW (and ratchet/coincident flag), minimum bill, riders (fuel, delivery, transition) as separate rows, source URL, tier, last_verified. Export JSON mirrors URDB field names so the electrotech app and SAM can consume it unchanged.
**Method.** Phase A (automated): pull URDB for every target `eia_id`, keep the latest approved residential + commercial schedules, flag stale (>24 months) and missing. Phase B (agents, Sonnet): per territory with a Yes in `res_habit`/`ci_habit` or a missing/stale URDB entry, fetch the tariff PDF/page and fill or correct. Phase C (Opus): reconcile riders, check one computed monthly bill per utility against the utility's own bill calculator or sample bill.
**Check (automated).** Every Yes in `res_habit` has a matching residential schedule with TOU periods; TOU windows cover 24 h x 7 d x 12 mo with no gap or overlap; prices positive and in plausible bands (flag outside 3-60 c/kWh); effective date present; URL live.
**Effort.** About 700 territories where a researchable tariff exists. Estimate 2-3M tokens for B+C if URDB covers 60%; Opus verification on a 10% sample plus 100% of the top-10 per region (~1.5M). Confidence 50%: URDB coverage is the swing factor, so run Phase A first and re-estimate.
**Map/UI.** Drawer section "Bill structure" (fixed charge, headline energy price, TOU window table, demand charge). No new layer until the data exists; a "bill-structure completeness" color-by layer is optional.

## 2. Historical LMP
**Goal.** For each organized market, hourly (and 5-min where available) day-ahead and real-time LMP history for settlement points relevant to customers, summarized as arbitrage-relevant statistics: price spread by hour-of-day/season, p90/p10 spreads, negative-price hours, scarcity-price counts, plus a mapping from each utility territory to its zone/load aggregation point.
**Sources.** Each ISO's public archive: PJM Data Miner 2, MISO market reports, CAISO OASIS, ERCOT public reports, NYISO and ISO-NE public data, SPP portal (all free; some need registration; verify rate limits). The open-source `gridstatus` Python library wraps most of them (it exists and documents these ISOs; verify version coverage and whether its hosted API needs a paid key). Non-RTO regions have no LMP: use balancing-authority or hub-level proxies (EIA-930 BA data, Southeast EIA price data) and label them as proxy, or leave blank.
**Data model.** Do not store raw hourly data in the repo. Store `data/processed/lmp_summary.csv` (market, zone, year, hour-of-day x season mean/p10/p90 spreads, negative hours, count of >$500 hours) plus a `zone_map.csv` (eia_id -> market, zone/LAP, method). Raw pulls live outside git (script + cache) and are reproducible from `scripts/lmp_pull.py`.
**Hard part.** The utility-to-node mapping: zones are rarely published as polygons. Start with one default zone per territory from the ISO's published utility-to-zone tables (PJM zones, MISO LRZ/commercial nodes, NYISO zones, ISO-NE load zones, CAISO LAPs (PG&E, SCE, SDG&E), ERCOT load zones). Territories spanning zones get the dominant zone and a flag.
**Check.** Spread statistics recomputed independently by a second agent from the raw pull for 3 zones per market; zone mapping spot-checked against ISO documents; no market in the table without a source URL; years and units stated.
**Effort.** Mostly code, little research: about 0.5-1M tokens (pipeline + one Opus review per market). Highest data volume, lowest token cost. Confidence 65%.
**Map/UI.** Drawer card "Wholesale price shape" with a 24-hour spread sparkline and a headline "typical daily spread". Rank 2 export feeds the same JSON to the electrotech app's dispatch optimizer.

## 3. DER hosting capacity
**Goal.** For each territory: does the utility publish a hosting-capacity or interconnection-capacity map, where, at what granularity, and with what data access (download/API vs viewer only), and are there regulator requirements to publish. Numeric hosting capacity per feeder is out of scope here: it is huge, changes monthly, and is not comparable across utilities.
**Sources.** DOE "U.S. Atlas of Electric Distribution System Hosting Capacity Maps" (exists; verify scope/date and download format). Utility ICA/hosting-capacity pages. State regulator orders requiring maps (CA, NY, MN, MA, IL, and others; verify the current list). IREC and Interconnection Innovation e-Xchange summaries.
**Data model.** `data/processed/hosting_capacity.csv`: eia_id, map_url, access (download/API/viewer/none/by-request), granularity (feeder/line-segment/substation), update frequency, state mandate citation, last_verified, tier. Presence-style tri-state (Yes/No/Unknown) with the same rule: No only if the utility's site was checked.
**Check.** Every Yes has a URL that loads and shows a map or dataset; sample of 10% opened by a second agent in a browser (viewer-only maps are JS-heavy: use the built-in browser).
**Effort.** About 1-1.5M tokens for ~400 utilities with online presence (most small co-ops/munis are quick No/Unknown). Confidence 55%.
**Map/UI.** Drawer line "Hosting capacity map: [link] (download / viewer only)"; optional color-by layer. Later (Rank 1.5): pull numeric feeder data only for the 10 largest IOUs where a download exists.

## 4. DER aggregators
**Goal.** For each territory and market: which third-party aggregators/VPP operators can enroll customers (and for which assets and programs), which utility-run aggregation programs exist, and the wholesale-market route (FERC Order 2222 status by market). Connects to existing `programs` rows (`DR-BYOD`, `VPP`, aggregator-facing C&I DR).
**Sources.** Utility program pages (already cited in programs rows); aggregator websites (Sunrun/CalReady-type VPPs, Tesla, OhmConnect/Renew Home, Voltus, CPower, Enel X successors, EnergyHub, Leap, Generac Concerto: verify which are active); ISO Order 2222 compliance filings and market-rule pages; trade press (RTO Insider, Utility Dive). Order 2222 timelines have moved repeatedly: verify each ISO's current go-live date from the ISO's own page before writing anything.
**Data model.** `data/processed/aggregators.csv`: aggregator, asset types, customer segment, eia_id or state/market coverage, program(s) used, enrollment basis, payment structure, source URL, status, tier. Plus `order2222_status.csv` per ISO (stage, go-live date, source). Add an `aggregator_active` Yes/No/Unknown to the presence scan only after the layer exists (SCAN_SCHEMA reserves `ViaAggregator` for dispatch cells).
**Check.** Every aggregator-territory row confirmed from the aggregator's own availability page or the utility's program page; a company that has exited or merged is marked Closed with a date; Order 2222 dates quoted from ISO documents.
**Effort.** Research-heavy and change-prone: about 1.5-2M tokens. Confidence 45%. Re-verify quarterly.
**Map/UI.** Drawer card "Who can monetize your flexibility here" (utility program, aggregator names, market route). Filter on the program layer for aggregator-enabled territories.

## 5. Order, cost and decisions
| Order | Layer | Est. tokens | Why this order |
|---|---|---|---|
| 1 | Bill structure | 3-4.5M | Needed for every savings and multiplier calculation; URDB gives a head start |
| 2 | LMP history | 0.5-1M | Cheap, mostly code; unlocks arbitrage value |
| 3 | Aggregators | 1.5-2M | Rides on programs rows already built; most volatile, so do it close to use |
| 4 | Hosting capacity | 1-1.5M | Presence-style first; numeric data later |
Total about 6-9M tokens (confidence 45%); the Rank 0 audit adds 3.5-5M before it. Re-estimate after the bill-structure Phase A (URDB coverage) and the LMP pull.

**Nathan decides before starting:**
1. Paid tariff data (Arcadia/WattBuy) allowed if URDB coverage is below ~60%? Default: no.
2. Scope for bill structure: default tariff + TOU/EV options only, or every schedule? Default: default + optional TOU/EV/demand rates for residential and small C&I; large-C&I deferred.
3. LMP in non-RTO regions: proxy (BA-level) with a label, or blank? Default: blank, with the nearest hub shown as context.
4. Hosting capacity: links only for now (default), or numeric data for the top IOUs?
5. Aggregators: US-wide company list, or only those with a program row or a Order 2222 route in the territory? Default: the latter.

## 6. Definition of done per layer
Schema file in `data/processed/`, a prompt template in `plans/prompts/`, an extension of `scripts/audit.py` (new check IDs B1..), a rubric section in `audit/RUBRIC.md`, drawer card on the live site verified by a different agent, and a `PLAN.md` handoff. Nothing counts as done on "wrote the file".
