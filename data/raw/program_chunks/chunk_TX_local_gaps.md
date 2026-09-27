# Gaps — chunk_TX_local.csv (TX utilities outside retail choice: munis, co-ops, Xcel/SPS, Entergy Texas, El Paso Electric)

Run date: 2026-09-27. 45 rows across 14 target utilities; validator passes (45x22).

## Checked, found nothing (no row emitted)

- **CoServ (Denton County Electric Cooperative)** — EVX ChargeSmart Beta pilot program: enrollment is now closed
  per coserv.com/energy-solutions/peaktime-perks/electric-vehicles-ev; no financial/incentive details published
  for the closed pilot, so no row emitted (rule: closed programs only included with financial data and a firm
  closure date after 2024, neither of which is available here).
- **Bluebonnet Electric Cooperative** — checked rates, energy-solutions pages: no TOU rate, no thermostat/DR
  program, no battery/storage incentive found on bluebonnet.coop beyond the flat Wholesale Power Cost +
  Residential/Commercial Service design and Large Power per-kW demand charge (captured as a row). Confirms
  the presence-scan finding.
- **Bryan Texas Utilities** — Critical Load Program (btutilities.com/for-business/critical-load) is a
  must-not-interrupt priority-restoration registry only, no dispatch/incentive component — does not qualify
  as DR-Curtailment per the schema's "alert-only/registry-only doesn't count" convention. PowerShare is a
  bill-round-up donation program, not dispatch. Residential/commercial rate schedules are flat per-kW demand
  tiers with no TOU design (confirmed via rate PDF links on-page).
- **Denton Municipal Electric** — GreenSense Incentive Program Manual PDF would not render via fetch (likely
  scanned/complex PDF); GreenSense is described elsewhere as an EE rebate program (smart thermostats, HVAC,
  insulation) with no evidence of utility dispatch control, consistent with the presence-scan finding, so no
  row emitted for it.
- **Garland Power & Light** — EnergySaver program (gpltexas.org/save-energy-money/energysaver-program) is an
  EE-rebate program (AC/heat pump, insulation, window units); did not confirm any dispatch/DR component in
  the time available. Residential/commercial rate schedules fully captured (seasonal RS rate, GS-L demand
  charge).
- **Southwestern Public Service Co. (Xcel Energy)** — exact $/kWh figures for the "business TOU rate plan"
  and the PUCT-filed "Interruptible Service Option Credit" tariff could not be independently confirmed: the
  tx.my.xcelenergy.com business-rates pages and the PUCT PDF document link returned no extractable content in
  the time available (JS-rendered/site error). Rows for both were still emitted (Unverified confidence) citing
  the best-available source URLs, per the presence scan's original findings — a follow-up pass should try to
  open the PUCT docket document directly or call Xcel's Business Solutions Center for the actual tariff sheet.
- **Entergy Texas** — could not confirm whether a residential/commercial TOU or RTP retail rate exists (only
  standard fuel/energy charge and rate/rider schedule links were found on entergytexas.com/residential/price
  and /business/price; the actual rate schedule PDFs were not opened). Also could not confirm export
  compensation (net metering) terms for Entergy Texas within the time available — worth a follow-up look at
  entergytexas.com's Texas tariff sheet.
- **El Paso Electric** — Business Time-of-Day rate figures redirect to a generic "Texas business rate tariffs"
  landing page (not opened); captured only the confirmed residential TOD rate. Storage-Incentive program (a
  standalone upfront battery rebate outside the Base Power pilot) not found — only the Base Power pilot (a
  hosting/incentive hybrid, captured as VPP) and net metering under Schedule 48 were found.

## Utilities fully covered with strong primary sourcing
Austin Energy, CPS Energy, Pedernales Electric Cooperative, CoServ, Guadalupe Valley Electric Cooperative,
Denton Municipal Electric (commercial TOU rate class confirmed, partial), Garland Power & Light (rate
schedules), Bryan Texas Utilities (SmartBUSINESS), Farmers Electric Cooperative (Texas), Entergy Texas
(Battery Storage Solutions + Demand Solutions thermostat program), El Paso Electric (TOD rate, Base Power
battery pilot, net metering, shared solar).

## Confidence notes
Two Southwestern Public Service (Xcel) rows are marked Unverified because the source pages could not be
opened despite being cited by the earlier presence scan as Primary — a discrepancy likely caused by
JS-rendering differences between fetch methods. Everything else in this file is Primary confidence, sourced
directly from each utility's own rate/program page fetched and read in full this run.

## Search/fetch budget note
Roughly 60 web_fetch calls plus ~10 browser-driven page reads were used across the 14 target utilities. A
brief outage of the fetch tool's safety classifier caused several minutes of retries early in the Pedernales
research; all other utilities were fetched without incident. No WebSearch budget remained for this chunk
(exhausted earlier in session) — all research after Austin/CPS relied on direct URL fetches (from the
scan_TX1/TX2 leads) and site navigation via the browser tool for JS-rendered pages.
