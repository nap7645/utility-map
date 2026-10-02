# Gaps — scan_W1 (Washington + Idaho, 39 targets)

Cluster: PNW sub-market, WECC-nonRTO. All 39 targets got a row; validator passes (39 rows × 17 fields).

## Sites that didn't render (JS-only or dynamic) — left Unknown rather than guessed
- **Benton Rural Electric Association** (eia 1625) — bentonrea.org returned empty on fetch. Only found via
  search: deploying Landis+Gyr AMI (Revelo/Gridstream Connect) — infrastructure, not a live program.
- **City of Port Angeles** (eia 15231) — cityofpa.us/1407/Current-Utility-Rates is JS-rendered.
- **City of Ellensburg** (eia 6149) — ci.ellensburg.wa.us/1260/Energy-Services is JS-rendered; actual
  rate schedule lives in Municipal Code Ch. 9.91 (not opened).
- **Lewis County PUD** (eia 10944) — lcpud.org/your-account/rates-fees rendered fees only; the linked
  PDF rate schedule was not fetched.

## Pilots / planned programs with ambiguous current status
- **Richland Energy Services** (eia 15979) — rates page didn't render detail; a 2023 Demand Response
  Potential Assessment exists (planning study, not confirmed live program).
- **Jefferson County PUD** (eia 59013) — a multi-year TOU + CPP + DR-incentive pilot is documented by
  American Public Power Association trade press citing the utility, but not independently confirmed
  on jeffpud.org itself, and current/ongoing status unclear.
- **Mason County PUD No. 3** (eia 15419) — a completed water-heater DR pilot (100 units) is documented
  by NW Power & Conservation Council, but not visible on the utility's own current site.
- **Grant County PUD** (eia 14624), **Cowlitz PUD** (eia 4442), **Benton PUD** (eia 1579) — all cite a
  planned/future demand-response buildout (DRPA reports, CEIP targets) with no operating program yet;
  cells marked No/Unknown per "checked and found nothing live" rule.

## Ambiguous evidence, marked Unverified/Unknown rather than guessed
- **Fall River Rural Electric Cooperative** (eia 6169) — has a flat (non-time-of-day) mandatory
  residential demand charge, which the schema counts as res_habit=Yes even though the utility's own FAQ
  explicitly says the charge is NOT time-of-day-based.
- **Douglas County PUD** (eia 5326) — residential demand charge above a 45kW threshold found via search
  snippet (own customer-service-policies page), but the full page wasn't rendered to confirm C&I design
  or any dispatch program.
- **Kootenai Electric Cooperative** (eia 10454) — confirmed residential Peak Use (demand) charge; could
  not verify C&I rate design or programs.
- **Snohomish County PUD** (eia 17470) — res_habit/res_dispatch strongly confirmed (FlexTime, FlexResponse,
  FlexEnergy all on own site); the C&I Time-of-Day pilot (Schedules 20/25/36) is from trade press and its
  post-Dec-2025 status and any C&I dispatch program are unverified.
- **Lakeview Light & Power** (eia 10627) — a "Free Google Nest Thermostat" program exists but the page
  gives no detail on whether it includes utility dispatch/DR control vs. a plain efficiency giveaway.
- **Tacoma Power** (eia 18429) — one industrial DR pilot (green-hydrogen facility) reported by Utility
  Dive, not found on the utility's own site.

## Name-collision / identity notes (per region_west.md cluster notes)
- **Northern Lights, Inc.** (ID/E.WA/W.MT co-op, eia 13758) is distinct from any other "Northern Lights"
  entity — confirmed via nli.coop, HQ Sagle ID.
- **Clark Public Utilities** (PUD No. 1 of Clark County, WA, eia 3660) is distinct from Clark County REMC
  (Indiana) — confirmed WA site (clarkpublicutilities.com).
- **Vigilante Electric Cooperative** (eia 23586, targets file lists state=ID) is headquartered in Dillon,
  Montana and primarily serves southwest Montana with adjacent Idaho territory — flagged in case downstream
  joins assume ID-only service territory.

## Search budget
Used roughly 90 WebSearch/web_fetch calls across 39 targets — well under the ~200 budget. No targets were
left as "search budget exhausted."

## fill3b pass (2026-10-02)
- Cowlitz (4442): res_dispatch=No from residential programs hub; rate schedule PDFs (cowlitzpud.org/wp-content/uploads/Schedule-*.pdf) are blocked by robots.txt for the fetch tool, so habit and C&I cells remain Unknown. Smart-thermostat rebate form exists (rebate only).
- Lewis PUD, Richland, Benton REA, Port Angeles, Ellensburg: rates pages JS/robots-blocked or contain only fees; Unknown remain.
