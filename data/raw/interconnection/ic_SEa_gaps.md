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
