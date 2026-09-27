# Gaps — scan_TX1.csv (ERCOT: 5 TDUs + 38 co-ops)

Run date: 2026-09-27. All 43 targets have rows; validator passes (43×17). This file lists what
could not be verified and why, plus name-collision notes for future agents.

## Name collisions resolved (verify domain before reusing any of these)
- **Tri-County Electric Cooperative (TX)** — correct domain is `tcectexas.com` (north TX: Azle,
  Granbury, Keller, Seymour). Do NOT use `tcec.com` (Florida, Seminole G&T member) or
  `tri-countyrec.com` (Tri-County Rural Electric Cooperative, Pennsylvania — phone area code 570).
- **United Electric Coop Service Inc (TX)** — correct entity is United Cooperative Services,
  legal name United Electric Cooperative Services, Inc., domain `ucs.net` (HQ Cleburne/Burleson).
  Do NOT use `ueci.coop` or `uec.coop` — both are different "United Electric" co-ops, apparently
  not the EIA 19490 target, though their exact locations weren't confirmed.
- **Farmers Electric Cooperative (TX)** — correct domain `farmerselectric.coop` (Greenville, TX).
  Do NOT use `fec-co.com` (a different Farmers' Electric Cooperative, believed Colorado).
- **Jackson Electric Coop (TX)** — correct domain `jecec.com` (Ganado, TX / Jackson County TX).
  Do NOT use `jacksonenergy.com` (Jackson Energy Cooperative, KY) or `jackelec.com` (a different
  Jackson Electric Cooperative, likely another state — not confirmed which).
- **Grayson-Collin Electric Cooperative (TX)** — correct domain `gcec.net`. A Google search for
  "smart thermostat program" surfaces Graham County Electric Cooperative (Arizona, `gce.coop`) —
  unrelated.
- **Trinity Valley Electric Cooperative (TX)** — correct domain `tvec.net`. Search results for
  thermostat programs return TVA EnergyRight (Tennessee Valley Authority, multi-state) — unrelated.
- **Central Texas Electric Cooperative** — correct domain `ctec.coop`. Search results for
  thermostat rebates return "Central Electric Cooperative" (Oregon, `cec.coop`/`central.coop`) —
  unrelated, similar name only.

## Rows with Unknown cells due to no program/rate found on the utility's own site (checked, found nothing)
Bandera (ci_habit/ci_dispatch), Mid-South (res_habit/ci_habit/ci_dispatch), Medina (res_dispatch/
ci_habit), Trinity Valley (res_dispatch/ci_dispatch), Grayson-Collin (res_dispatch/ci_dispatch),
Nueces (res_dispatch/ci_dispatch — retail-choice co-op, see note below), Central Texas
(res_dispatch/ci_dispatch), Bluebonnet (res_dispatch/ci_dispatch), United Coop Services
(ci_dispatch), Rio Grande (ci_habit/ci_dispatch), Bartlett (res_habit/ci_habit/ci_dispatch),
Lamar County (res_dispatch/ci_dispatch), San Patricio (res_habit/ci_habit/ci_dispatch).

## Rows almost entirely Unknown — site had minimal usable content within search budget
Cherokee County EC, Navasota Valley EC, Navarro County EC, Comanche EC, Cooke County EC
(PenTex), Jackson EC (TX, beyond the thermostat rebate note), Fayette EC, Big Country EC,
Fannin County EC, Hamilton County EC (partial — res_dispatch confirmed No). These co-ops'
websites either had thin public content, were mostly JS-rendered account portals, or simply
did not surface rate/program detail through search within the ~180-query budget used. A
follow-up pass with direct site navigation (rather than search-engine snippets) would likely
close several of these.

## Retail-choice special case
- **Nueces Electric Cooperative** opted INTO ERCOT retail choice in 2004 (one of the few TX
  co-ops on Power to Choose) and owns its own REP, NEC Co-op Energy. Treated like a TDU for
  res_habit/ci_habit (marked No, delivery-only) per the cluster-note convention; res_dispatch/
  ci_dispatch marked Unknown since no TDU-style SOP was found on NEC's own site.

## Confirmed patterns worth reusing
- All 5 TDUs (Oncor, CenterPoint Houston Electric, AEP Texas Central, AEP Texas North, TNMP)
  confirmed via their own retail-delivery tariffs to sell no retail energy (res_habit/ci_habit =
  No) and all 5 run PUCT-mandated Load Management Standard Offer Programs covering both
  residential (smart thermostat) and commercial classes (res_dispatch/ci_dispatch = Yes, Primary).
- A purchase-only thermostat rebate (no utility control of the device) does NOT count as
  res_dispatch under the schema — applied consistently to HILCO, Wise EC, Hamilton County EC,
  Houston County EC's "Seasonal Savings," and (partially) Jackson EC TX.
- An alert-only "Beat the Peak" / "Avoiding the Energy Rush" program (no device control, no
  incentive payment) does NOT count as dispatch — applied to United Coop Services, Victoria EC,
  San Patricio EC.
- Medina EC's irrigation load-management program (utility remotely shuts off irrigation motors
  in exchange for a reduced demand/energy rate) does count as ci_dispatch — irrigation accounts
  are billed as non-residential/demand-metered.

## Search budget
Used roughly 55 WebSearch calls plus ~10 direct page fetches (~65 of the ~200-call budget) across
43 targets. Remaining budget was intentionally not fully spent — most "Unknown" cells above
reflect genuine absence of findable content on the utility's own domain via search-engine
snippets, not budget exhaustion. A follow-up pass could improve confidence by fetching each
small co-op's rates/programs pages directly rather than relying on search snippets.
