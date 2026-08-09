# Gaps and unverifiable items — Cluster C (IL, MO, AR, LA, MS, TX/MISO-Entergy Texas)

Written 2026-08-09. These are items flagged `Not independently confirmed` / `Unclear` in the CSVs, or
structural issues worth a human's attention before this data drives design decisions.

## Cross-cutting
- **Storage/grid-charging provisions are the weakest data point across this entire cluster.** Only
  Illinois (via its Level 1-4 application form, which explicitly asks whether the applicant intends
  grid-charging and offers Solar Non-Export / Time-Based Control checkboxes) has clear primary-source
  language. Missouri's rule (20 CSR 4240-20.065) and Mississippi's rule contain **zero** mentions of
  "storage" or "battery" anywhere in the text — these are genuine regulatory gaps, not omissions on my
  part. Arkansas defines "Energy Storage Device" and lists it as an eligible facility type but has no
  grid-charging or non-export language. Louisiana and Texas have no statewide interconnection standard
  at all in the MISO-served territory, so storage treatment is 100% utility-tariff-dependent and
  unverified here for every utility except Illinois.
- **Non-export/limited-export interconnection pathways** are confirmed to exist as a defined option only
  in Illinois. Not confirmed as present or absent for MO, AR, LA, MS, or TX — this needs direct tariff
  review per utility before assuming C&I non-export storage projects have a fast path in this cluster.

## Illinois
- Exact 5% aggregate cap subscription level (how full the cap is) not obtained — needs a live ICC/
  Illinois Shines capacity dashboard pull, not a static document.
- IEEE 1547 version transition (1547-2003 vs 1547-2018/UL 1741-SB) is ambiguous: MidAmerican's own
  Level 1 form text still cites IEEE 1547(2003) even though 466.40 just says "IEEE Standard 1547"
  generically and IREC's adoption tracker suggests IL is mid-transition. Needs a docket-level check
  (ICC Docket 20-0700 amendments) to nail down the current mandatory edition and effective date.
- Whether battery kW/kWh counts toward the 2,000 kW system cap or the 5% aggregate cap: not confirmed.
- ic_timeline_days (day-counts by interconnection Level) not extracted from the rule text this pass.
- ComEd's specific storage $/kWh Smart Inverter Rebate value not found (Ameren Illinois' schedule was
  found and used; ComEd's equivalent number is a gap).

## Missouri
- No statewide application fee schedule found (utilities may pass through metering/upgrade costs but no
  fixed statewide number).
- Storage interconnection, grid-charging, and non-export provisions: entirely unaddressed in the primary
  rule text — flagged, not guessed.
- Ameren Missouri's reported annual-true-up-to-avoided-cost mechanic and specific ¢/kWh figures came
  from secondary/summary sources, not a verified current tariff sheet — confidence marked Low.

## Arkansas
- No specific IEEE 1547/UL 1741 edition cited in the rules (only generic "IEEE...UL..." language).
- No fixed statewide application fee dollar amount — rules authorize a "standard one-time fee" but leave
  the number to utility tariffs.
- No insurance dollar minimum found in the rules (only general indemnification language) — this differs
  from Missouri's explicit $100,000/>10kW threshold and is worth double-checking against utility-specific
  tariffs.
- Non-Legacy avoided-cost figures for Entergy Arkansas and SWEPCO are both reported from
  secondary/news sources, not live tariff sheets — confidence Low, needs a direct pull of each utility's
  current Non-Legacy Net-Metering rate schedule.
- North Little Rock Electric Department's dual-meter avoided-cost billing structure was found via a
  single secondary source; the actual ordinance (linked) should be read directly to confirm since this
  materially changes storage economics versus single-meter netting.

## Louisiana
- **Louisiana has no statewide interconnection standard/procedures document** (confirmed via IREC/Vote
  Solar's Freeing the Grid project). This means IEEE standard version, fast-track/simplified kW tiers,
  application fees, study triggers, external disconnect policy, insurance requirements, and timeline days
  are all unconfirmed at the state level and are utility-tariff-specific across the board — this is the
  single largest data gap in the entire cluster.
- Entergy New Orleans / New Orleans City Council: confirmed the separate jurisdiction and the 2007 rule
  adoption, but **could not confirm current 2026 status** — whether the City Council has since followed
  the LPSC's 2019 move to avoided-cost net billing for new customers, or whether New Orleans still offers
  retail net metering to new solar customers today. This is high-value and should be resolved directly
  against a current Entergy New Orleans / City Council Utilities Committee tariff or docket.
- Exact current-year Avoided Cost ¢/kWh figures per utility were not extracted from LPSC's annual
  "Avoided Cost Rate by Electric Utility" documents (2023-2026 editions exist and are linked in the state
  row's source) — only DEMCO's rate was pulled through to a specific number.

## Mississippi
- Confirmed via H.B. 1139 (2016) that MPSC **cannot set compensation levels for cooperatives**, and that
  roughly 57% of Mississippi ratepayers (co-ops + munis) are not bound by the state Net Metering Rule's
  caps/adders described in the state row — this is a major applicability caveat, not just a Coast
  Electric-specific note.
- Mississippi Power's low-to-moderate-income adder dollar value (distinct from the 2.5¢ base adder) not
  independently confirmed.
- Standby/backup/exit fees are explicitly PROHIBITED by rule (Ch. 03 Sec. 111) — high confidence, primary
  source read directly.

## Texas
- This is the thinnest state row in the cluster by design — Entergy Texas/PUCT-specific interconnection
  mechanics (16 TAC 25.211 fast-track/simplified kW tiers, application fees, study-trigger screens,
  external disconnect policy, insurance, and timeline days) were not extracted from the full rule text in
  this pass; only the top-level applicability structure (50kW renewable / 100kW non-renewable net
  metering cap under 16 TAC 25.242, avoided-cost billing under Schedule SQF) is well-sourced.
  16 TAC 25.211's 10 MW ceiling for IOU interconnection generally is confirmed, but the internal review
  tiers within that ceiling are not.
- Current Entergy Texas avoided-cost ¢/kWh figure (on-peak/off-peak) not pulled from a live PUCT filing.
- Confirm whether any ERCOT-area municipal or cooperative utility bordering the Entergy Texas MISO
  footprint independently offers a comparable program — out of scope for this cluster (Entergy Texas is
  the only MISO-served TX utility in the requested list) but worth flagging if the design tool later adds
  ERCOT utilities, since the "no statewide mandate" framing does NOT mean "no export compensation
  anywhere in ERCOT" — competitive retail solar buyback plans exist there on a voluntary basis.
