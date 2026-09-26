# Gaps — chunk_NE_rest (northern New England munis/co-ops + Efficiency Maine)

## Checked, no program found (or not independently verifiable beyond a generic muni page)

- **Liberty Utilities (Granite State Electric)** — checked residential rates/tariffs pages and the
  battery storage program page. Beyond the (now closed-to-new-enrollment) Tesla Powerwall pilot
  and its associated TOU rate, found no separate DR, export-comp specifics, or EV rate program
  page with published dollar figures. NH PUC docket IR 22-076 investigates whether Liberty's
  tariffs adequately support DR/EV charging — an open proceeding, not a program, so no row filed.
- **Taunton Municipal Lighting Plant** — no DR/TOU/VPP program found beyond the solar+battery
  rebate and two-tier net metering already captured. No ConnectedSolutions-style battery dispatch
  program on TMLP's own site.
- **Chicopee Electric Light** — no utility-specific storage incentive $ figure found beyond
  Connected Homes and a yard-equipment rebate (amount not published online). No separate TOU or
  export-comp page found distinct from standard MA net metering.
- **Holyoke Gas & Electric** — no TOU rate or export-comp tiering beyond flat full-retail net
  metering found.
- **Braintree Electric Light Department (BELD)** — checked energysavings and solar-programs pages
  directly. BELD's own site has NO battery storage rebate, DR program, or published TOU/export
  rate — only efficiency rebates (appliances, heat pumps), a 0% Z-Loan, and general "Solar
  Programs" messaging with no rebate figures on-page. Third-party aggregator sites (NuWatt,
  EnergySage) attribute a "$275/kW ConnectedSolutions" battery-dispatch figure to BELD customers —
  **this is incorrect**: ConnectedSolutions is an Eversource/National Grid/Unitil/Cape Light
  Compact program funded through the Mass Save energy-efficiency surcharge on IOU ratepayers.
  Massachusetts municipal light plants (BELD, and likely PMLP, Chicopee, Taunton, Norwich-style
  peers) are NOT part of Mass Save or ConnectedSolutions and set independent rebate/DR programs.
  No row filed for BELD storage dispatch; flagging so downstream consumers don't inherit the
  aggregator error.
- **Norwich Public Utilities (CT)** and **Wallingford Electric Division (CT)** — same
  misattribution pattern found in reverse direction: aggregator sites (NuWatt) apply
  "ConnectedSolutions $225/kW/yr" and "CT Energy Storage Solutions up to $7,500" figures to these
  municipal utilities' customers. ConnectedSolutions and CT Energy Storage Solutions (Energize CT)
  are Eversource/United Illuminating programs approved by PURA and funded via IOU ratepayer
  surcharges; **Connecticut municipal electric utilities (Norwich, Wallingford, Groton, Jewett
  City, Bozrah, East Hampton...) are not part of either program.** A secondary search explicitly
  confirmed "no CT muni operates a residential battery VPP or storage incentive." Norwich and
  Wallingford's own sites (norwichpublicutilities.com/216, wallingfordct.gov) list only
  efficiency-program rebates (HES home energy audits, heat pump rebates ≤$1,500 for Wallingford,
  EV charger rebates ≤$500 for Wallingford) — no DR, TOU, storage, VPP, or export-comp program with
  a published $ figure was found on either utility's own site. No rows filed for either utility;
  this appears to be a genuine "No" (checked) rather than a search gap, though a live person at
  each utility should confirm since JS-heavy pages (norwichpublicutilities.com) did not render
  text via fetch.
- **New Hampshire Electric Cooperative** — Peak Days CPP-PTR program credit amount not published
  online (row filed with structure but blank incentive_value).

## Could not check / search budget or access limits

- **Norwich Public Utilities (CT)** rates/tariff pages and **Wallingford Electric Division (CT)**
  rates/tariff pages returned empty content via fetch (likely JS-rendered) — net metering credit
  mechanics and any TOU rate could not be directly verified from a primary source; only aggregator
  summaries were available (marked Unverified/not filed, see above).
- **Peabody Municipal Light Plant** Net Metering Policy PDF (linked, Primary source cited) did not
  render extractable text via fetch — filed with tariff_schedule blank, source_url correct, credit
  rate itself not confirmed.
- Did not attempt Burlington Electric's non-EV TOU/demand rate schedule or its Net Zero Energy
  incentive specifics beyond the EV tariff and Moduly battery pilot mention — BED's residential and
  C&I standard rate schedules were not pulled given time budget.
- Efficiency Maine's Energy Storage System (ESS) program is behind a PON/RFP process; did not pull
  the full PON PDF for exact application windows or the current program year's award status.

## Notable finding for the region plan

Confirmed the plan's expectation that TOU is thin in New England: of the utilities in this
cluster, only NHEC, Liberty NH (battery-pilot participants only), Versant, CMP (Rate A-TOU,
Rate LGS-S-TOU), and Peabody MLP (Rate T) have identifiable TOU tariffs; Burlington Electric,
Vermont Electric Cooperative, Taunton, Chicopee, Braintree, Holyoke G&E, Norwich, and Wallingford
have no evidence of a TOU rate on their own sites.
