# Gaps — scan_W3 (Colorado + Utah, WECC-nonRTO Mountain cluster)

Scan completed 2026-09-26, 40/40 targets, all rows validated (17 fields, no duplicate eia_ids).

## ci_dispatch is nearly all Unknown (38/40)
C&I curtailable/interruptible/aggregator-facing DR was the hardest cell to confirm from public
utility-facing pages — most co-ops and munis don't publish a C&I-specific curtailment tariff
online even when one exists in their rate book. Confirmed Yes only for Xcel Energy Colorado
(Peak Partner Rewards / ISOC) and Fort Collins (Peak Partners covers small C&I). Worth a targeted
follow-up pass reading full PSC/PUC tariff filings (not just utility marketing pages) for the
larger co-ops (CORE, United Power, Holy Cross, La Plata, Poudre Valley) which likely have
C&I riders buried in tariff schedules not surfaced by web search.

## Tri-State's 2025 Demand Response Program — opt-in, not yet attributable member-by-member
Tri-State G&T launched a FERC-approved DR Program in summer 2025 with four tracks (Irrigation DR,
C&I DR, Smart Thermostat DR, Member DR), but Tri-State's own press release says it is "actively
engaged with several members to work toward program enrollment" — i.e. opt-in per member co-op,
not a blanket rollout. I did NOT mark all ~15 Tri-State members in this scan as Yes on the
strength of the G&T program alone (unlike TVA or Basin Electric, where G&T-run programs are
uniformly deployed). Only marked Yes where a member's own site confirmed a live program
(San Isabel's Shift to Save, Highline's Load Control, SECPA's HH rate, La Plata's WattWatcher,
etc.). Re-verify in ~6-12 months whether more Tri-State members have since enrolled in the DR
Program tracks — this is a good candidate for a scheduled re-scan.

## Rows needing direct re-verification (own-site confirmation was thin or blocked)
- **Murray City Power (UT, eia 13137)** — rates page returned no readable content (likely
  JS-rendered); everything Unknown. Needs a fresh fetch or phone/tariff-PDF lookup.
- **Kaysville City Corporation (UT, eia 10063)** — city's own Power page has no rate detail (rates
  live in a Consolidated Fee Schedule PDF not reviewed this session); news coverage suggests a
  peak-pricing rate change was proposed but adoption status is unconfirmed.
- **City of Bountiful (UT, eia 2010)** — found a time-varying value only in the net-metering EXPORT
  credit context; unclear if there's a separate consumption-side TOU rate. Full rate PDF (bountifulutah.gov)
  needs a line-by-line read.
- **Poudre Valley REA (CO, eia 15257)** — TOU/Power Peak Rewards/Battery Rewards info came from a
  third-party aggregator (Nectar) rather than pvrea.coop directly; re-confirm on the co-op's own site.
- **Moon Lake Electric (UT, eia 12866)** — TOU option confirmed only via a PSC tariff filing; unclear
  whether it's available to residential accounts or only demand-metered irrigation/industrial.

## Shortcuts taken
- Munis with confirmed flat/tiered-only rates on their own rate pages (Lehi, Logan, Springville,
  Spanish Fork, St. George, Washington City, Fountain) were marked `No` for res_habit and
  ci_habit per the "checked absence is a valid No" rule in the region plan — these are small
  UAMPS/UMPA or independent munis with no TOU infrastructure evident.
- Where a Tri-State-member co-op's own site clearly described a TOU/demand rate but not a
  dispatch program, I left res_dispatch/ci_dispatch as Unknown rather than inferring from the
  Tri-State G&T program (see above).

## Confidence tier note
32/40 rows are Primary (utility's own site/tariff is the source URL). 5 Secondary (aggregator or
news reporting on the utility's own program). 3 Unverified (Murray, Kaysville, Bountiful — see above).

## fill3b pass (2026-10-02)
- Murray (13137): res_habit=No (rate schedule eff 2023-07-18: seasonal tiers only). Fetch summarizer described 'time-of-use'; the quoted content is seasonal (Peak Season/Off-Peak Season), so treated as non-TOU - worth a human glance. ci_habit left Unknown.
- Bountiful: rate PDFs on bountifulutah.gov redirect to homepage; Kaysville: annual report shows no DR/TOU but no tariff read. Unknown remain.
