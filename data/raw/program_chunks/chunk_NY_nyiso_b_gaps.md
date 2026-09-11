# chunk_NY_nyiso_b — gaps and unverified items

Top-up file for the five thinly covered NY utilities. 45 rows, 9 per utility.
All rows `rto=NYISO`, `state=NY`, `last_verified=2026-09-10`.
Companion to `chunk_NY_nyiso.csv` (Con Edison, National Grid NY, NYSERDA) — no duplicates with it.

## Rows written with a blank `incentive_value_usd` (program confirmed, dollar figure not published)

- **NYSEG / RG&E Term-DLM and Auto-DLM** — value cell carries the published *Incentive Rate cap*
  ($26.25/kW in the Jan 2025 RFP, $25.50/kW in the Dec 2023 RFP). Actual payments are set by
  accepted bid and are not public.
- **O&R Term-DLM and Auto-DLM** — no Incentive Rate cap found in the public O&R RFP materials.
  Structure (4-hr weekday call windows / 21-hr notice for Term; 10-min notice, 18 hr/day, 7 days
  for Auto; 3-year minimum contract) is confirmed; the $/kW is not.
- **Standby rates at all five utilities** (O&R SC 25, NYSEG SC 11, RG&E SC 14, Central Hudson
  SC 14, LIPA SC 12) — the *structure* is confirmed (contract demand $/kW + as-used daily demand)
  but the actual $/kW figures live in tariff leaves that are not exposed as HTML and were not
  opened. LIPA SC 12 is the exception in structure detail: TOU periods, phase-in schedule and the
  1.25:1 peak/off-peak and 2.25 summer/winter ratios are all confirmed from the LIPA board memo,
  but the numeric $/kW is still not captured.
- **RG&E SC-4 Residential TOU** — peak window (M-F 7am-9pm) and the 24,750 kWh/yr Schedule I/II
  split are confirmed. A "$0.00341/kWh peak delivery charge" figure appeared in a search summary
  but looks like a single rate component, not the delivery rate; deliberately **not** written.
- **Central Hudson EV Whole Home TOU, Central Hudson TOU Service (post-Dec-2017), Legacy TOU** —
  on-peak windows confirmed, cents/kWh not published on the customer pages.
- **NYSEG / RG&E OptimizEV** — $25 enrollment incentive confirmed; the per-kWh off-peak reward
  rate is not published in the program FAQ (program says rewards scale with off-peak share above
  80%). Off-peak window 11:30pm-7am EST / 12:30am-8am EDT is confirmed for NYSEG only; RG&E's
  exact window was not separately confirmed and the cell says "overnight" instead.
- **LIPA/PSEG LI System Peak Relief Program (CSRP/DLRP)** — PSEG LI publishes *no* $/kW or $/kWh.
  The FAQ states rates are derived from PSEG Long Island's Marginal Cost of Service (MCOS) Study.
  This is the single biggest missing number in this file.
- **LIPA/PSEG LI Battery Storage Rewards** — annual payment is set by the third-party aggregator,
  not by PSEG LI. A "$250/kWh upfront, $6,250 cap" figure circulates on vendor sites (Enphase);
  it is a vendor/NYSERDA-routed number, not a PSEG LI published rate, so it was **not** written.
- **LIPA TOD Off-Peak and Super Off-Peak rates** — peak window (weekdays 3-7pm) confirmed;
  cents/kWh not on the page. "Up to 40% off the Rate 180 flat rate" for the overnight super
  off-peak period is the only published number and is recorded.
- **NYSEG Hourly Pricing / RG&E Hourly Pricing / O&R Hourly Energy Pricing** — indexed to
  day-ahead NYISO LBMP, so there is no fixed figure by design. NYSEG's 300 kW mandatory threshold
  is confirmed; RG&E's and O&R's exact thresholds were not confirmed and are left descriptive.

## Rows marked `Secondary` (claim not read directly off the utility's own page)

- **NYSEG DLRP and RG&E DLRP** — the "$0.00/kW-month, held indefinitely, zero 2025 enrollments"
  claim comes from the NYSEG/RG&E 2025 Demand Response Annual Report (DPS Case 14-E-0423). The
  DPS ViewDoc link is cited but the PDF was not opened page-by-page; the claim came from a search
  index of that document. Worth one confirmation pass. Note this makes DLRP effectively dormant
  at both utilities even though it is still on the books.
- **NYSEG SC 11 / RG&E SC 14 standby** — service-classification numbers and the PSC standby-rate
  exemption counts (Central Hudson 100, NYSEG 250, RG&E 150 non-NEM-eligible customers) come from
  a PSC filing, not the utilities' own rate pages.

## Checked and found nothing (deliberate non-rows)

- **Central Hudson DLRP** — Central Hudson's C&I demand response page lists only CSRP and the
  Targeted Demand Response (TDR) program. No Distribution Load Relief Program was found. Do not
  assume parity with the other five IOUs here.
- **Central Hudson Term-DLM / Auto-DLM** — no Central Hudson DLM RFP surfaced. Con Ed, O&R,
  NYSEG and RG&E all run one; Central Hudson appears not to.
- **O&R residential real-time / hourly rate** — O&R publishes hourly pricing for *businesses*
  only. No residential RTP rate found; the residential option is the TOU rate.
- **O&R Bring Your Own Battery** — already captured in `chunk_NY_nyiso.csv` (row 30); not
  duplicated here.
- **LIPA/PSEG LI thermostat program for business** — only the residential Smart Savers program
  was found.

## Not checked / out of scope

- **LIPA "EV Phase-In Rate"** — referenced in the December 2025 LIPA board tariff deck and in an
  April 2025 EV Rates Tariff Memo (https://www.lipower.org/wp-content/uploads/2025/04/EV-Rates-Tariff-Memo-4.14.2025.pdf).
  Appears to be a demand-charge phase-in rate for public EV charging aligned with the IOU EV
  rates. Not written — the memo was not opened and I would have had to guess the structure.
- **Commercial EV managed-charging and make-ready programs** (O&R POWERREADY, NYSEG/RG&E
  Commercial Load Management and Rates, Central Hudson commercial EV, PSEG LI EV Make Ready).
  These are capital/make-ready incentives rather than BESS-revenue-relevant rates, so they were
  deprioritized. Each utility has one.
- **Gas demand response** (O&R has a BYOT Gas DR pilot targeting 4,000 customers by 2029) — out
  of scope for an electric BESS dataset.
- **O&R electric tariff PSC schedule number** — I could not confirm whether O&R's NY electric
  tariff is P.S.C. No. 3 or No. 10 (one O&R page title says "Public Service Commission Number
  10", which is also Con Edison's number). `tariff_schedule` on the O&R rows deliberately omits
  the PSC number rather than guessing. NYSEG PSC No. 120, RG&E PSC No. 19 and Central Hudson
  PSC No. 15 are used and are standard.

## Notes that matter for the model

- **NYSEG/RG&E DLRP pays $0.00/kW-month.** Any model that treats "utility has a DLRP" as a
  revenue stream will over-credit NYSEG and RG&E.
- **Central Hudson TDR and CSRP are mutually exclusive.** TDR pays far more ($6.82/kW-month
  Jun-Sep vs $1.23-$1.54/kW-month CSRP) but is geographically restricted.
- **Central Hudson CSRP performance rates are an order of magnitude below the Avangrid
  utilities** ($0.11-$0.35/kWh vs $0.50/kWh at NYSEG/RG&E and $0.50-$1.00/kWh at O&R).
- **LIPA is not PSC rate-regulated** and its DER economics differ materially from the IOUs:
  mass-market NEM cannot opt into VDER, export is compensated under SC 11 Buyback Service with a
  new contract demand charge on injections, and stand-alone storage reaching SGIP Step 3 before
  Dec 31 2030 gets a 15-year exemption from that charge. That exemption is a real, dated
  economic cliff worth surfacing in the tool.
- **LIPA SC 12 Super Off-Peak (10pm-8am, every day, both seasons) carries no as-used daily demand
  charge** — a direct, explicit charging-window signal for behind-the-meter storage.
