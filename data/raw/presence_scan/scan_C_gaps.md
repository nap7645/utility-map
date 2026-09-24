# scan_C gaps — Indiana + Ohio (52 targets)

Completed 2026-09-24. All 52 targets have a row; validator passes clean (52 rows x 17 fields,
every eia_id from targets_C.csv present exactly once).

## Approach

Given the volume (52 utilities) and a co-op/muni-heavy cluster, most rows lean on the G&T/
aggregator shortcut the schema explicitly permits: Hoosier Energy (MISO), Wabash Valley Power
Alliance (WVPA, IN/IL/MO), Buckeye Power (PJM, OH co-ops), IMPA (mostly MISO, IN munis), and AMP
(PJM, OH munis). Membership in each G&T/aggregator was confirmed against that org's own "our
members" page before tagging rto and citing its dispatch program. Rate-design cells (res_habit,
ci_habit) are NOT G&T-run, so those were only marked Yes/No where I actually opened the member's
own rates page; most were left Unknown rather than extrapolated from the pattern seen in verified
peers (several Hoosier/WVPA members that WERE individually checked do have TOU/RTP residential
rates — Hendricks Power, South Central Indiana REMC, Southeastern Indiana REMC, Clark County REMC,
Johnson County REMC, UDWI REMC, Whitewater Valley REMC, Kankakee Valley REMC, NineStar Connect —
so the true positive rate for res_habit among the unchecked co-ops in this cluster is likely
higher than what's recorded).

## Not individually verified (marked Unknown, candidates for a follow-up pass)

- **res_habit / ci_habit for ~30 co-ops** whose G&T membership is confirmed but whose own rates
  page was not opened this pass: Bartholomew County REMC, Harrison REMC, RushShelby Energy,
  Dubois REC (Hoosier); Kosciusko REMC, Heartland REMC, Boone Power, Carroll White REMC, Parke
  County REMC, Noble REMC (WVPA); all 15 Ohio Buckeye Power members (Licking/Energy Cooperative,
  Consolidated, Buckeye Rural, Holmes-Wayne, Guernsey-Muskingum, Pioneer, Lorain-Medina,
  Paulding-Putnam, Hancock-Wood, Carroll, Butler Rural, Union Rural, Midwest Electric, Washington
  Electric, South Central Power). ci_habit is Unknown/No for essentially the whole file — none of
  the sites I opened advertised a shifting-oriented C&I rate design (demand-charge tariffs don't
  count per schema), so this cell needs a dedicated pass through each utility's commercial tariff.
- **res_dispatch / ci_dispatch for the 7 IMPA municipals and 5 AMP municipals**: IMPA's own
  program pages (impa.com) returned empty/JS-blocked content when fetched directly, so IMPA's
  Interruptible Rate/DR rider is cited via an IURC regulatory filing (Secondary) rather than
  IMPA's own program page — a Primary citation would strengthen these rows. AMP's Smart Thermostat
  page is Primary, but AMP itself says it's subscription-based per member, so each city's actual
  enrollment (Hamilton, Bowling Green, Niles, Painesville, Piqua) is still unconfirmed.
- **ci_dispatch for Buckeye and WVPA members**: no clear C&I curtailable/interruptible rider page
  was found for either G&T within budget (Buckeye's page only says it "assists members with load
  management"); left Unknown rather than guessed.
- **Licking Rural Electric Inc (eia_id 10668)**: Buckeye Power's own 24-member roster lists "The
  Energy Cooperative" as the Licking-County-area member, not "Licking Rural Electric" by that exact
  name. Treated as the same/successor entity (Unverified) — worth confirming directly with Buckeye
  or the coop's own site.
- **Tipmont REMC (eia_id 18940)**: confirmed it exited its all-requirements WVPA contract June 1,
  2025 (stepping down to zero by 2032), so the WVPA PowerShift/dispatch shortcut does not reliably
  apply anymore. Its current wholesale supplier/RTO delivery point and any of its own DR/TOU
  programs were not individually checked (tipmont.org) — flagged Unverified, needs a dedicated look.
- **City of Columbus, OH Division of Power (eia_id 4065)**: large independent municipal (not an
  AMP member); rates/programs not checked this pass — the utility's own site should be visited
  directly.
- **Kingsport Power Co and Wheeling Power Co**: both filed under OH in HIFLD/the targets file but
  actually serve Kingsport, TN and the Wheeling, WV area respectively, as AEP/Appalachian Power
  subsidiaries. Noted in each row; residential/TOU tariff schedules for those specific
  jurisdictions were not opened (only the general Appalachian Power TN tariff PDF and the WV rates
  landing page were used, both cited for ci_dispatch only).
- **rto for the 7 IMPA municipals** (Anderson, Richmond, Logansport, Greenfield, Peru,
  Crawfordsville) is MISO by inference from IMPA's overall MISO-majority footprint, not confirmed
  per-member; Mishawaka was separately confirmed as PJM (AEP Indiana Michigan Power transmission
  territory).

## Search budget

Not exhausted — stopped after establishing G&T/aggregator membership and a representative sample
of individual-site checks per cluster, in the interest of covering all 52 targets within a
reasonable pass. A follow-up pass focused specifically on the ~30 unchecked co-op rate pages would
likely convert a meaningful share of the `res_habit=Unknown` cells to `Yes`, based on the high hit
rate (9 of 9 checked) among Hoosier/WVPA co-ops with a dedicated rates or TOU page.
