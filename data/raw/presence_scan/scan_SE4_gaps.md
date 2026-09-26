# SE4 (Florida) presence scan — gaps

WebSearch budget was exhausted (200/200 calls) partway through this cluster. The following
utilities got only partial or no direct-site verification and are recorded with `Unknown` cells
and `confidence=Unverified`. Re-run with a fresh search budget to fill these in — try each
utility's own domain directly with `web_fetch` first (many are WordPress/Drupal sites that render
fine without JS), since several plain fetches of `.gov` sites returned empty JS-shell content in
this run.

## Fully unresearched (all 4 cells Unknown)
- **City of Ocala** (eia 13955) — ocalafl.gov rates/tariffs subpages return empty content via
  fetch (JS-rendered). Try a direct PDF guess (`ocalafl.gov/.../Electric-Rate-Schedule.pdf`) or a
  search engine once budget resets.
- **City of Homestead** (eia 8795) — homesteadfl.gov pages return empty content via fetch.
- **Utility Board of the City of Key West / Keys Energy Services** (eia 10226) —
  kwutilities.com and kwboard.org both return empty content via fetch. Correct domain not
  confirmed — verify the utility's actual current domain first.
- **Utilities Commission of New Smyrna Beach** (eia 13485) — cityofnsb.com electric-rates page
  returns empty content.
- **City of Leesburg** (eia 10868) — leesburgflorida.gov electric department page timed out.
- **City of Lake Worth Beach** (eia 10620) — lakeworthbeachfl.gov utilities/electric page returns
  empty content.
- **City of Winter Park** (eia 58124) — not reached at all before budget ran out.
- **City of Bartow** (eia 1300) — not reached at all before budget ran out.
- **Florida Keys Electric Cooperative** (eia 6443) — fkec.com/rates returns empty content. Not
  confirmed as a Seminole G&T member (not in Seminole's 9-member list); its actual wholesale
  supplier is unverified.
- **Choctawhatchee Electric Cooperative** (eia 3502) — DeFuniak Springs, panhandle. Site not
  reached. `rto=SERC-nonRTO` is an *inference* from geography (west of the Apalachicola River,
  likely Southern Company balancing area / PowerSouth Energy Cooperative G&T member per the
  region-plan hint) — **verify directly**, don't treat as confirmed.
- **West Florida Electric Cooperative** (eia 20371) — Graceville, panhandle. Same caveat: rto is
  inferred, not verified.
- **Gulf Coast Electric Cooperative** (eia 7785) — Wewahitchka, panhandle. Same caveat.
- **Escambia River Electric Cooperative** (eia 5964) — Jay, panhandle (far west). Same caveat.

## Partially verified — flagged for re-check
- **Peace River Electric Cooperative** (eia 14606) — res_habit (RS-TOU) and ci_dispatch
  (Interruptible Service tied to Seminole supply) are marked Yes at Secondary confidence from an
  older/secondary source (OpenEI/PSC filing); PRECO's own current rate book PDF
  (`preco.coop/wp-content/uploads/PRECO-Rate-Book-Final-Eff-2025.pdf`) would not render via fetch.
  Re-fetch that PDF directly to confirm sheet numbers are still current.
- **Central Florida Electric Cooperative** (eia 3245) — ci_dispatch (interruptible C&I) is
  Unknown; no dedicated rate-schedule PDF was located, only the bill-explainer page.
- **Tri-County Electric Cooperative (FL)** (eia 19161) — the only rate PDF found on tcec.com is
  dated 2018 and may be stale; res_habit/ci_habit/ci_dispatch could have changed since.
  ci_dispatch marked Unknown for lack of a schedule listing.
- **Glades Electric Cooperative** (eia 7264) — rates page is a news-style blog with no rate
  schedule table; ci_dispatch Unknown for lack of a schedule PDF.
- **Withlacoochee River Electric Cooperative** (eia 20885) — ci_dispatch Unknown; no C&I
  interruptible/curtailable rider found in the search snippets available.

## Follow-up pass (2026-09-26)

- **FL panhandle co-op rto verification (priority item)** — already resolved by an earlier fill
  pass before this one started: PowerSouth Energy Cooperative's own site (powersouth.com) lists
  Choctawhatchee (CHELCO), West Florida, Gulf Coast, and Escambia River as member distribution
  co-ops (confirmed directly from the homepage member-map image alt-text this pass too), so
  rto=SERC-nonRTO is Primary-sourced for all four, not inferred from geography. No further change
  needed; noting it here since it was this job's priority #4.
- **Utility Board of the City of Key West / Keys Energy Services (eia 10226)** — filled from
  mostly-Unknown: the correct own domain is **keysenergy.com**, not kwutilities.com/kwboard.org
  (both tried in the prior pass and both wrong/empty). Own "Time-of-Use Pilot Program" page
  confirms a voluntary Residential + Small Commercial TOU rate -> res_habit=Yes, ci_habit=Yes
  (Small Commercial TOU tariff pages 14 and 19 linked from the same page). res_dispatch/
  ci_dispatch remain Unknown.
- **City of Homestead (eia 8795)** — filled from all-Unknown: the City's own "Customer Service -
  Schedule of Rates" PDF (homesteadfl.gov DocumentCenter) shows flat residential and commercial
  rates with a single flat KW Demand Charge, no on/off-peak differential -> res_habit=No,
  ci_habit=No. res_dispatch/ci_dispatch remain Unknown. Caution for future passes: a search hit
  for a "Demand Response" login portal that looked plausible for Homestead turned out on
  inspection to belong to **Hilton Head PSD (South Carolina)** running the same third-party
  SmartC/SEW platform template — a real name/content collision, not used for this row.
- **City of Ocala (eia 13955)** — partially filled: ocalafl.gov's electric-utility subpages remain
  JS-rendered/unreachable directly, but the city's own "Beat the Peak" program page (mirrored via
  a govaccess.org URL, read via search snippet) describes a voluntary peak-conservation alert
  program with no device control -> res_dispatch=No at Secondary confidence. res_habit/ci_habit/
  ci_dispatch remain Unknown; a residential/commercial rate-schedule PDF was never located.
- Still fully Unknown after this pass: City of Winter Park, City of Bartow, Utilities Commission
  of New Smyrna Beach, City of Leesburg, City of Lake Worth Beach, Florida Keys Electric
  Cooperative (fkec.com) — all remain JS-rendered/unreachable or budget-limited.

## Confirmed shortcuts used
- **Seminole Electric Cooperative** runs "Cooperative Rewards" (Bring-Your-Own-Thermostat DR,
  EnergyHub-powered) across all nine of its member distribution co-ops — cited directly at
  `seminole-electric.com/cooperative-rewards/` and mirrored on several members' own sites
  (preco.coop, jea.com-style local pages). Applied as `res_dispatch=Yes` for: Withlacoochee River,
  Clay, SECO Energy, Talquin, Central Florida, Peace River, Suwannee Valley, Tri-County (FL), and
  Glades — the full nine-member roster confirmed via `seminole-electric.com/members/`.
