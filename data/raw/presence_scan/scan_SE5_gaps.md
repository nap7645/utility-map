# Gaps — scan_SE5 (TN, TVA local power companies)

All 62 targets are TVA local power companies (LPCs), confirmed via TVA's own EnergyRight
Smart Thermostat Rewards participating-LPC list and TVA's PowerFlex/Demand Response LPC
dropdown (both TVA's own domain, energyright.com / greatergrid.com). `rto=TVA` and the
dispatch cells (`res_dispatch`, `ci_dispatch`) are Primary-sourced from those two lists for
all 62 rows.

## Habit cells (res_habit / ci_habit) — only 9 LPCs individually verified

Per the region plan's TVA shortcut caveat ("retail rates are opt-in/utility-set — check each
LPC's own rate page, do not infer from TVA alone"), I individually checked the 9 largest LPCs
named in the cluster notes, plus Nashville Electric Service:

- Nashville Electric Service — res_habit=No, ci_habit=Yes (Schedule TDGSA)
- Memphis Light, Gas & Water — res_habit=Yes (RS-TOU, pilot-enrollment only), ci_habit=Unknown
- Middle Tennessee Electric — res_habit=Yes (NiteFlex), ci_habit=Yes (Key Accounts TOU)
- Knoxville Utilities Board — res_habit=Yes (RS-TOU pilot), ci_habit=Yes (GSA-TOU/TDGSA pilot)
- EPB (Chattanooga) — res_habit=Yes (Time of Use Rate / Night Shift), ci_habit=Unknown
- Volunteer Energy Cooperative — res_habit=No (checked, no TOU schedule listed), ci_habit=Unknown
- Cumberland EMC — res_habit=No, ci_habit=Yes (TOU/MS schedules, >5,000 kW accounts only)
- BrightRidge (Johnson City) — res_habit=No, ci_habit=Yes (TDMSA/TDGSA for large accounts)
- CDE Lightband (Clarksville) — res_habit=No, ci_habit=No (checked, flat rates only)

## Remaining 52 LPCs — habit cells left Unknown

For the other 52 targets (mostly smaller municipal/co-op TVA distributors — e.g. Duck River
EMC, Lenoir City Utilities Board, Sevier County Electric System, Tri-County EMC, Upper
Cumberland EMC, Southwest TN EMC, Appalachian EC, Greeneville, Gibson EMC, Sequachee Valley EC,
Dickson, Jackson Energy Authority, Mountain EC, Meriwether Lewis EC, Fort Loudoun EC, Caney
Fork EC, Bristol TN Essential Services, Columbia P&W, Powell Valley EC, Cleveland Utilities,
Holston EC, Alcoa, Clinton UB, Elizabethton, Gallatin, Lexington, Newport, LaFollette,
Maryville, Paris, Chickasaw EC, Lawrenceburg, Pickwick EC, Weakley County, TN Valley EC,
Cookeville, Fayetteville, Plateau EC, Oak Ridge, Carroll County, Morristown, Rockwood, Pulaski,
Loudon, Athens, Dyersburg, Bolivar, Harriman, Dayton, Tullahoma, Shelbyville, Benton County,
Forked Deer EC) — `res_habit` and `ci_habit` are left `Unknown`. Each LPC sets its own retail
rate structure independently of TVA, so a per-LPC rate-page check is needed before these can be
marked Yes or No. This is a clean follow-up task: visit each LPC's own rates page and look for
an optional residential TOU/off-peak rate (the "NiteFlex"/"Night Shift" naming pattern is common
in this region) and a C&I time-of-day or TOU rate schedule.

## Other notes

- `ownership_type` for "CARROLL COUNTY - (TN)" (eia_id 3075) is recorded as Cooperative based on
  a name match to "Carroll County Electric Cooperative" in TVA's own LPC dropdown — worth
  double-checking against EIA's own classification, since a Tennessee municipal system of the
  same naming pattern (e.g. "Benton County") turned out to be municipal, not cooperative.
- Two Athens entries exist in TVA's LPC lists (Athens Utilities Board, TN vs. Athens Electric
  Department, AL) — used "Athens Utilities Board" / "Athens Utilities" (TN) throughout, matching
  hifld_state=TN.
- Search budget: not exhausted (~30 calls used of the ~200 budget). The Unknown habit cells
  reflect a scope decision (prioritize verified big-LPC data + confirmed dispatch/rto for all 62)
  rather than a budget cutoff — a follow-up pass could burn through the remaining budget on the
  52 small-LPC rate pages.
