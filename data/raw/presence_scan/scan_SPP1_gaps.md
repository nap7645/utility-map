# Gaps — scan_SPP1 (OK, SPP cluster A)

Search budget was used efficiently but several targets' own sites either returned no
machine-readable content (JS-only rate pages) or embed rate sheets as non-text
documents (issuu flipbooks, Google Drive PDFs not fetched). These are marked
`Unknown` in the scan with `confidence=Unverified` rather than guessed.

## Could not verify (site unreachable / non-text rates page)

- **CKENERGY ELECTRIC COOPERATIVE** (60482) — ckenergy.coop/rates returned no
  readable content (likely JS-rendered). All 4 cells Unknown.
- **NORTHWESTERN ELECTRIC COOP INC** (13807) — nwecok.coop/rates returned no
  readable content. Only found a possible EV off-peak charging incentive
  (10pm-5am), not confirmed as a whole-home TOU rate.
- **PEOPLE'S ELECTRIC COOPERATIVE** (14775) — peopleselectric.coop rate/program
  pages not indexed/reachable via search within budget.
- **TRI-COUNTY ELECTRIC COOP, INC (OK)** (19160) — tcec.coop (Hooker, OK) rate
  pages not reachable within budget. **Name collision flag**: at least 4 other
  "Tri-County Electric Cooperative" entities exist (TX — tcectexas.com, MI —
  tcec.com/HomeWorks, tri-countyelectric.net, and the AECI-adjacent MO Tri-County
  in the AECI member list) — do not conflate rate data across these in any
  follow-up pass.
- **TAHLEQUAH PUBLIC WORKS AUTHORITY** (18433) — no published rate schedule found
  online; only a 2025 news item about a GRDA-driven rate increase.
- **COTTON ELECTRIC COOP, INC** (4401) — rates are published only as an embedded
  issuu flipbook (non-machine-readable); member-resources page confirms rates
  exist but not their structure.
- **CENTRAL RURAL ELECTRIC COOPERATIVE, INC** (3226) — confirmed as an AECI
  member via aeci.org (listed as "Central Electric Cooperative," Stillwater OK —
  matches OAEC's "Central Rural Electric Cooperative" address), but its own
  site (mycentral.coop) rate/program pages were not reached within budget.

## Partially verified — flagged for a follow-up pass

- **RED RIVER VALLEY RRL ELEC ASSN** (15746) — own page confirms "time-of-use
  and curtailable rates ... for qualifying consumers" but doesn't specify
  whether residential customers qualify (reads as C&I/large-load oriented).
  Marked ci_habit/ci_dispatch=Yes, res_habit/res_dispatch=Unknown; the full
  tariff PDF (linked from rrvrea.com/services-rate-information) should be
  pulled to confirm residential eligibility.
- **SOUTHEASTERN ELECTRIC COOP INC - (OK)** (17603) — the OAEC directory lists
  this co-op's address as Durant, OK, but southeasternelectric.com's own
  footer shows a Lennox, SD headquarters and East River Electric Power
  Cooperative (SD) as its G&T. This may be two organizationally distinct
  "Southeastern Electric Cooperative" entities sharing a name (there is also
  a Southeastern Electric Cooperative in South Dakota per the region plan's
  name-collision warning) — the domain found (southeasternelectric.com) and
  its water-heater-control / load-control programs should be re-verified
  against the OK entity's own tariff/EIA filing before this row is relied on
  for anything customer-facing.
- **KIAMICHI ELECTRIC COOP, INC** (10170) — curtailable Large Power rider
  explicitly cites Western Farmers Electric Cooperative (WFEC) as the entity
  designating curtailment periods, even though Kiamichi is an AECI member per
  aeci.org. Both G&T relationships may be real (wholesale power vs.
  transmission curtailment coordination) but this wasn't reconciled.
- **INDIAN ELECTRIC COOP, INC** (9246) — confirmed AECI member via aeci.org's
  own service-area page, but the region plan's cluster notes did not list
  Indian Electric among the AECI co-ops to check — this was discovered
  independently and should be cross-checked against AECI's member list if it
  changes.

## Rate schedules found but not fully read (partial reviews)

- **East Central Electric Cooperative** (5598) — full ~2,100-line tariff PDF
  confirms TOU-R/TOU-C/TOU-P/TOU-LP rate schedules (residential + commercial +
  pumping + large-power TOU) but was not read past section 165 (of ~315+); no
  explicit curtailable/interruptible C&I rider was found in the reviewed
  portion, so ci_dispatch is marked Unknown rather than No.
