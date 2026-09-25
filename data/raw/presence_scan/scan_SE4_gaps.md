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

## Confirmed shortcuts used
- **Seminole Electric Cooperative** runs "Cooperative Rewards" (Bring-Your-Own-Thermostat DR,
  EnergyHub-powered) across all nine of its member distribution co-ops — cited directly at
  `seminole-electric.com/cooperative-rewards/` and mirrored on several members' own sites
  (preco.coop, jea.com-style local pages). Applied as `res_dispatch=Yes` for: Withlacoochee River,
  Clay, SECO Energy, Talquin, Central Florida, Peace River, Suwannee Valley, Tri-County (FL), and
  Glades — the full nine-member roster confirmed via `seminole-electric.com/members/`.
