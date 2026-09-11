# scan_NY1 — gaps and unverified leads

## What could not be fully verified

- **Jamestown BPU — ci_dispatch source is Secondary, not Primary.** The SC-6 "Flex Rate"
  tariff itself (DPS ETS filing, "leaves 124-130") was not located/opened — search results
  and the utility's own pages only summarize it. The claim that SC-6 agreements include a
  demand-response component comes from a March 2026 APPA podcast interview with BPU's
  general manager (publicpower.org), which is trade-press reporting on the program, not the
  tariff. If the actual SC-6 tariff text can be pulled from NYS DPS's ETS system
  (https://www2.dps.ny.gov/ETS/search/searchShortcutEffective.cfm?companyID=4943798&serviceType=ELECTRIC&psc_num=7),
  this could be upgraded to Primary or could reveal the DR provision only applies to specific
  contracted customers rather than being a standing program.

- **Freeport Electric — site is partially stale/JS-rendered.** The static fetch of
  freeportelectric.com/2180/Electric-Rates only returned the first accordion panel
  (Residential Non-Heating); "Residential Space & Water Heating," "Residential Water
  Heating," and "Residential Space Heating" panels required a rendered browser and were not
  individually expanded (Large Commercial and the start of Small Commercial were expanded and
  checked). The page states rates are "Effective as of August 1, 2014," which is unusually
  old for a live rate page — it's possible actual current rates differ, though a flat
  block/seasonal design is very unlikely to have become a TOU or DR design since. Not
  reflected as a distinct row-level flag, but worth a follow-up pass if Freeport is
  prioritized later.

- **NYPA / MEUA shared-program lead — checked, no evidence found reaching these five
  utilities' retail customers.** NYPA's Customer Energy Solutions team is described in NYPA's
  own marketing as offering "demand response capabilities" to "public, commercial, municipal,
  and institutional customers," but this reads as a general service NYPA can arrange for
  large customers (e.g., NYC agencies), not a standing program these five village/city
  utilities enroll their residential or small-C&I customers in. No utility-specific
  confirmation found for any of the five. Not included in any cell.

- **MEUA / NYMPA IEEP — confirmed as an efficiency program, not a TOU/dispatch program.**
  Fairport explicitly participates (cited on its Energy Conservation page); Rockville
  Centre's Peak Savers appliance-rebate line item and Jamestown/Freeport/Plattsburgh likely
  overlap with the same joint MEUA/NYMPA efficiency framework, but IEEP itself only funds
  appliance/heat-pump/lighting rebates — it does not appear to run a shared TOU rate or
  device-dispatch program across members. The one true dispatch program found (Rockville
  Centre's DSM smart-thermostat program) is billed and reported as RVC's own PSC-approved
  program (Case 07-E-1303), not an IEEP/MEUA-wide product, so it was not extrapolated to the
  other four utilities.

- **Rockville Centre ownership_type** — HIFLD lists "NOT AVAILABLE." Confirmed Municipal:
  the Electric Department is run directly by the Village of Rockville Centre government
  (Village-employed Superintendent of Electric Utilities, PSC filings signed on Village
  letterhead).

## Not verified at all

None of the five targets were left at "Unknown" for any cell — every utility's own rates
page/tariff (or, for Rockville Centre's dispatch cells, its own PSC filing) was located and
read directly.
