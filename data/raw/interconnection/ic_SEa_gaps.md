# Gaps - Cluster SEa (NC, SC, GA) interconnection - run 2026-09-24

## Run status
- Run was cut short: WebSearch returned "session limit" and the auto-mode classifier timed out on web_fetch / browser tools after the NC research. Only the NC state row was written. SC and GA state rows and ALL 12 utility-delta rows remain to be done. A relaunch with the same prompt should resume (append SC, GA, then utility rows).
- Duke, Dominion and NCUC tariff PDFs return empty bodies to web_fetch (bot protection / PDF). The NCUC starw1 PDF loads in the browser pane (HTTP 200, 4 MB) - extracting text there with pdf.js is the route to Primary-tier citations next run.

## North Carolina (row written, confidence Secondary)
- Source is the NC Public Staff net metering page (state agency summary of the NCUC E-100 Sub 180 order) plus installer summaries (Southern Energy Management Sep 2026; Cape Fear Energy). Rider RSC / NMB tariff sheets were NOT read directly.
- NEEC value (~3.4 c/kWh) is from installer summaries, not the rider sheet.
- Minimum bill and non-bypassable amounts not written: installer summary gives NBC 0.28 $/kW-mo (DEC) and up to 0.62 $/kW-mo (DEP) and "up to $8 (DEC) / $14 (DEP)" minimum-bill add-on; not verified against tariff.
- Rider NMB annual enrollment cap number not verified.
- NCIP: fee schedule verified from search snippet of NCIP text; Fast Track kW limit, study trigger, external disconnect, insurance, timelines, IEEE 1547-2018 adoption status, and non-export path NOT verified. The "2023 rewrite" of NCIP named in the brief could not be located - the June 2019 E-100 Sub 101 order (storage additions) is the latest found.
- grid_charging_allowed = Unclear: no NCUC or Duke text found addressing grid-charged battery export under RSC/NMB.
- Battery retrofit on a legacy Rider NM system: NOT verified. Legacy NM ends 12/31/2026 for everyone anyway (auto move to NMB), so the grandfathering question in NC reduces to whether a battery addition resets the 15-year NMB term or forces RSC - not found.


## Resume run 2026-09-26 (utility rows 10-14)
- Added: Cobb EMC (GA), GreyStone Power Corporation (GA), Walton EMC (GA), EnergyUnited (NC), Duke Energy Progress, LLC (SC). DEP does serve SC and has its own RSC (Leaf 663) and NMT (Leaf 671) riders on the SC eTariff, so a separate SC row was warranted.
- Method note: etariff.psc.sc.gov PDFs return empty to web_fetch; they load in the browser pane, and text was extracted in-page by inflating content streams with DecompressionStream and mapping Identity-H glyph IDs (+29 offset works for these Word-generated Duke PDFs).
- grid_charging_allowed is Unclear for all four co-ops (Cobb, GreyStone, Walton, EnergyUnited): none of their DG riders/interconnection standards mention storage charging source. Only DEP SC is a firm No (renewable-only charging in the Customer-Generator definition).
- Battery-added-to-legacy treatment: Unclear everywhere. Cobb has a real legacy tier ($0.0683/kWh for DG connected before 7/1/2015) keyed to connection date; EnergyUnited has closed Option A (retail credit) and its Interconnection Standard 4.10 requires a new application for any output-capacity change - neither says whether re-application forfeits the legacy tier. GreyStone and Walton already pay avoided cost on all exports (two-channel), so little is at stake.
- Stale values: GreyStone DG-2 purchase rate $0.02855/kWh is as of the 10/1/2021 rider (the rider says it may be adjusted at any time; no newer value published). Walton EMC's $0.04247/kWh is stated effective only through 12/31/2025; the 2026 value is not published.
- Not found online: Cobb EMC and GreyStone 'Distributed Generation Policy' documents (define DG facility and interconnection rules); Cobb's monthly facility charge amount; Walton's interconnection standard; DEP SC RSC non-bypassable $/kW (it lives in Schedule R-STOU, not read).
- EnergyUnited fee conflict: website says $250 res / $500 non-res; the 2019 Interconnection Standard PDF says $100 / $250. The row uses the website figure.
- State file: remaining blank cells (SC nem_cap_nonres_kw and standby_threshold_kw; GA ic_simplified_kw, ic_timeline_days and standby_threshold_kw) left blank. No source was found this run.
