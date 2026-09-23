# chunk_CA_iou — gaps, corrections and caveats

Region: California (CAISO). Entities: PG&E, SCE, SDG&E, and a synthetic
`California statewide (CPUC / CEC / GO-Biz administered)` entity.
`last_verified` = 2026-09-16 on every row.

---

## 1. Verdict on each lead in the task brief

### Default residential TOU (TOU-C / TOU-D / TOU-DR) — PARTLY RIGHT, names need correcting

| Utility | What actually exists now | Note |
|---|---|---|
| PG&E | `E-TOU-C` (peak 4-9pm every day), `E-TOU-D` (5-8pm weekdays), `E-ELEC` (Electric Home), `EV2` (EV2-A) | **The current E-TOU-C tariff sheet (Cal. P.U.C. Sheet 61124-E, eff. 2026-03-01) opens with "This *voluntary* schedule is available to residential customers on an *opt-in* basis."** The 2021-22 default-TOU migration is history; the sheet no longer carries default language, and bill protection has been closed to new enrollees since 2022-05-04. I set `enrollment_basis=Opt-in` on the E-TOU-C row to match the tariff. **The region plan's claim that residential customers are on a default TOU rate should be softened for PG&E — I could not find a tariff sheet that designates a current default residential TOU rate.** |
| SCE | `TOU-D-4-9PM`, `TOU-D-5-8PM`, `TOU-D-PRIME`; `TOU-D-A`, `TOU-D-B`, `TOU-D-T` are **discontinued and closed to new enrollment** | SCE's own rate page does not label any option "default". I marked 4-9PM and 5-8PM `Opt-in` and PRIME `Default` (because PRIME is *mandatory* for Solar Billing Plan customers). |
| SDG&E | `TOU-DR1` — SDG&E's page text says explicitly "this is SDG&E's standard schedule for residential customers", so `Default` is verified. Also `TOU-DR2`, `TOU-DR-P` (Time-of-Use Plus), `EV-TOU-5`. | |

So: names were close but not exact. There is no "TOU-C / TOU-D / TOU-DR" triplet; each utility has a family of options.

### "NEM 3.0" / Solar Billing Plan — RIGHT, with the exact naming corrected

- The regime is the **Net Billing Tariff (NBT)**, adopted in **CPUC D.22-12-056** (2022-12-15) and implemented by **Resolution E-5301** (2023-11-30). "NEM 3.0" is not a CPUC term. **All three IOUs brand it the "Solar Billing Plan."**
- Applies to interconnection applications submitted **on or after 2023-04-15**.
- Exports are credited at **CPUC Avoided Cost Calculator hourly values** (8760 values per year per utility), not retail. CPUC's own language: usually below retail but "can rise above the retail rate on late summer evenings."
- **ACC Plus / Energy Export Bonus adder**: residential PG&E and SCE customers interconnecting before the end of 2027 get an elevated export credit for **nine years**, locked at permission-to-operate. **SDG&E residential customers are excluded** (CPUC's stated reason: SDG&E's higher retail rates already produce larger bill savings). Customers required to install solar by building code do not get the adder.
- **Mandatory import rates**: E-ELEC (PG&E), TOU-D-PRIME (SCE), EV-TOU-5 (SDG&E).
- **NBT legacy period is 9 years** for the original interconnecting customer. Customers who *migrate* from a NEM tariff to NBT do **not** get the 9-year NBT legacy period.
- **Grandfathering**: NEM 1.0/2.0 customers keep their tariff for **20 years from interconnection** (D.14-03-041). The legacy runs with the *system*, not the owner — a buyer inherits the remaining years. A NEM 1.0 customer who rolled to NEM 2.0 does **not** get a second 20 years.

### THE HIGH-VALUE QUESTION: does adding a battery to a grandfathered NEM 2.0 system forfeit grandfathering?

**No — adding storage alone does not forfeit NEM legacy status.** The forfeiture trigger is an increase in *renewable generating* nameplate capacity, not the addition of storage.

PG&E's Solar Billing Plan page states the rule directly (this is the cleanest primary-source wording I found):

> "Existing customers who submitted a complete application before April 14, 2023, are **not** affected by this new program. The customers who will be affected are:
> - Existing solar or renewable energy customers who modify or expand their legacy NEM/NEM2 system above the tariff threshold levels.
> - A renewable electrical generation facility that increases 10% of the original renewable electrical generating facility nameplate capacity
> - A facility that increases their system size greater than 1kW."

Source: <https://www.pge.com/en/clean-energy/solar/getting-started-with-solar/solar-billing-plan.html>
Affected customers move to the Solar Billing Plan **at their annual True-Up date**, not immediately.

**Caveats you should know before relying on this commercially:**

1. I did **not** get the sentence out of D.22-12-056 itself. The 250-page decision PDF at
   <https://docs.cpuc.ca.gov/PublishedDocs/Published/G000/M500/K043/500043682.PDF>
   is blocked by a 403 from the workspace's egress proxy and exceeds the fetch tool's size cap.
   The rule as stated above is from **PG&E's own tariff-facing FAQ**, which is a primary utility
   source, and is corroborated by the CPUC's comparison table on the NEM/NBT page. **If a customer
   contract or a marketing claim depends on this, pull the ordering-paragraph language from
   D.22-12-056 and Resolution E-5301 directly before publishing it.**
2. The 1 kW / 10% threshold is phrased in terms of *nameplate generating capacity*. A battery has no
   renewable generating nameplate, so it does not consume the allowance. But storage paired with a
   NEM system is separately governed by **D.14-05-033** (pairing rules), **D.16-04-020** (estimation
   and metering options for small storage), **D.19-01-030** (large storage), and **D.20-06-017**
   (grid charging before PSPS; removal of the large-storage sizing limit). Those decisions set the
   *metering* obligations for a paired battery — that's where the practical friction is, not in
   grandfathering. I have not summarized those metering rules into rows; they belong in the
   interconnection chunk.
3. Inverter/battery *configuration* can change export capability even when the tariff vintage is
   preserved. That is an interconnection question (Rule 21), not a NEM question.

### ELRP — EXISTS, but the residential track described in the brief is GONE

- ELRP is a **5-year pilot**; CPUC's program-at-a-glance table gives **non-residential 2021-2027** and **residential 2022-2025**.
- **Non-residential: $2.00/kWh** of measured voluntary reduction. **Residential (Power Saver Rewards, ELRP A.6): $1.00/kWh** — not $2.
- CPUC states plainly: "The ELRP pilot will continue each year through 2027, **with the exception of residential Power Saver Rewards which will sunset at the conclusion of the 2025 ELRP program year**."
- **SDG&E confirms the sunset operationally**: it stopped accepting Power Saver Rewards applications as of **2025-11-01** and auto-unenrolled participants. PG&E's current residential DR lineup (ART, SmartRate, SmartAC, WatterSaver) no longer lists Power Saver Rewards at all.
- **Batteries absolutely qualify for ELRP.** Group A eligibility explicitly names "customers with distributed energy resources that can generate energy (e.g., behind-the-meter solar plus storage…) that have permission to export," plus "Aggregators of Virtual Power Plants" and V1G/V2G aggregators.
- Events: May-Oct, 7 days/week, 4-9pm, 1-5 hour events, **60 event-hours/year cap**, consecutive days allowed, no penalty for non-performance.
- **Group B** lets customers already in a CAISO market-integrated DR program earn ELRP for *incremental* reduction beyond what is committed to CAISO — that is the stacking path.

### The program checklist

| Lead | Verdict |
|---|---|
| **DRAM** (third-party aggregators) | **DISCONTINUED.** The CPUC's final decision (April 2024) ended DRAM after the **2024 delivery year**. The pilot ran 2016-2024 (D.16-06-029, D.17-10-017, D.19-07-009). Row written with `program_status=Terminated`. Aggregators now reach CAISO through Proxy Demand Resource / DERP registration and through ELRP. **Correct the region plan — it still lists DRAM as live.** |
| **Capacity Bidding Program** | **CONFIRMED, active.** PG&E Schedule E-CBP (PDR-integrated, May 1-Oct 31, day-ahead notice by 5pm, 1 event/day, 4-hr max, **no minimum demand**, net-metered customers eligible). SCE runs **CBP-Elect** and **CBP-E Direct** and offers it to *residential* customers too. |
| **Base Interruptible Program** | **CONFIRMED, active, C&I.** Full PG&E rate table captured. Batteries qualify: the Prohibited Resources policy exempts "energy storage resources not coupled with fossil-fueled generation." |
| **SCE Smart Energy Program** | **CONFIRMED.** $75 one-time sign-up credit + up to $50/yr; smart thermostat + central A/C. |
| **PG&E SmartAC** | **CONFIRMED, active.** Switch-based A/C DLC. |
| **PG&E SmartRate** | **CONFIRMED, active.** Residential CPP with a Bill Protection guarantee. |
| **SDG&E Power Saver Rewards** | **TERMINATED** (see above). |
| **SGIP** | **CONFIRMED but mostly closed** (see below). |

### SGIP — EXISTS, but the picture in the brief is out of date

CPUC's published incentive table (rates current on the CPUC page as of 2026-09-16):

| Budget | Rate | Sector | Status |
|---|---|---|---|
| Residential Solar and Storage Equity (RSSE, AB 209) | Storage **$1,100/kWh**, Solar **$3,100/kW** | low-income residential, **statewide including non-IOU** | the only budget still taking applications — **waitlisted** |
| San Joaquin Valley Residential | $1,100/kWh | PG&E/SCE residential | "available through 2025" |
| Equity Resiliency | $1,000/kWh | IOU res + non-res | "available through 2025" |
| Small Residential Storage (general market) | **$150/kWh** | IOU residential | "available through 2025" |
| SJV Non-Residential | $1,000/kWh | SCE non-res | "available through 2025" |
| Non-Residential Equity | $850/kWh | IOU non-res | "available through 2025" |
| Large-Scale Storage | $250/kWh | IOU non-res | "available through 2025" |
| Generation | $2,000/kW | IOU non-res | "available through 2025" |

- Yes, there are separate **equity** and **resiliency** budgets — that part of the brief is right.
- **But there is effectively no general-market residential storage rebate left.** The general-market
  Small Residential Storage budget was $150/kWh and CPUC labels it available through 2025.
- **RSSE budget: $280 million authorized**, reservations opened **2025-06-02**, established by
  **D.24-03-071** (AB 209), opened by **Resolution E-5362**, IRA tax-credit interaction finalized by
  **Resolution E-5373**.
- **Every SGIP applicant must enroll in a qualified Demand Response program within one year of
  reserving funds.** This is a hard condition and it is the reason SGIP and ELRP/CBP rows are marked
  stackable.
- SGIP is administered by the utilities but the *rates and budgets* are statewide CPUC constructs, so
  I filed all SGIP rows under the `California statewide` entity, as instructed.

**What I could not verify:** the live budget-by-budget open/closed/waitlist state on
<https://www.selfgenca.com/home/program_metrics/>. That dashboard is JavaScript-rendered and did not
return content through the fetch tool. I marked the "through 2025" budgets `Closed to new enrollment`
based on CPUC's own labeling; **confirm against selfgenca.com before quoting a rebate to a customer.**

### Residential battery VPPs distinct from the above — YES, all three have something

| Utility | Program | What it is |
|---|---|---|
| PG&E | **Automated Response Technology (ART)** | Residential battery/DER VPP. Events any time of day, 1-4 hours, day-ahead email. Batteries may export during events. **Incentives are set and paid by the third-party ART provider, not by PG&E** — so `incentive_value_usd` is blank by necessity, not omission. |
| SCE | **Behind-the-Meter Optimization of Load Technology (BOLT) Study** | A pilot/study, not a tariff. **Behind-the-meter batteries up to $400 each**, EVs up to $125, smart thermostats up to $100. No device limit. Enroll via EnergyHub, Octopus, or Uplight/Optiwatt. |
| SDG&E | **ELRP A.4** | A *residential battery-only* ELRP track. Events any day 4-9pm May-Oct, 1-3 hours, triggered by a CAISO Emergency Energy Alert. **Enrollment is only through a participating battery manufacturer, and the manufacturer pays the customer** — SDG&E publishes no $/kWh. Stacks with the TOU-DR-P rate; incompatible with a Rule 32 program. Authority: D.21-12-015. |

Also found and filed, not in the brief:
- **Demand Side Grid Support (DSGS)** — a **CEC** program (not CPUC), AB 205/AB 209, Guidelines Fifth
  Edition adopted 2026, docket 22-RENEW-01, administered via Olivine. Pays an upfront capacity
  commitment plus per-unit net-load reduction, May-Oct. This is a second statewide dispatch revenue
  stream for batteries and it should be added to the region plan.
- **PG&E Schedule B-19 Option S** — a storage-specific C&I demand-charge option that converts monthly
  demand charges into **daily** ones. This is the single most commercially interesting rate in the
  chunk for a peak-shaving battery, and it is subject to an enrollment cap.
- **SCE Charge Smart – SoCal** (WeaveGrid managed EV charging), **SCE SmartShift Rewards**,
  **PG&E WatterSaver**, **PG&E Automated Demand Response** ($200/kW, up to 75% of project cost).

---

## 2. Rows written with `incentive_value_usd` blank, and why

Per the rules, blank beats a guess. Each of these is a real program with a real deep link:

- **PG&E Schedule E-CBP (Capacity Bidding Program)** — capacity and energy payments are in a
  CPUC-approved table inside the tariff PDF. The PDF is 53 KB of extracted text and exceeded the
  fetch tool's return limit; I captured the program mechanics from PG&E's program page but not the
  price table. PG&E's page says only "the capacity payment is a CPUC-approved price that is listed in
  the Capacity Bidding Program tariff" and that **aggregators set what the end customer actually
  receives**, so even the tariff number is not the customer's number.
- **PG&E SmartRate** — the credit and event surcharge live in the underlying rate schedule. The
  tariff-book path I tried (`ELEC_SCHEDS_E-SRTP.pdf`) returned empty; I did not want to cite a
  third-party blog's number against a pge.com URL.
- **PG&E SmartAC** — PG&E's program page describes the mechanism but does not state the bill credit.
- **PG&E Automated Response Technology (ART)** — incentive is provider-set by design.
- **SDG&E ELRP A.4** — compensation is manufacturer-set by design.
- **SCE CBP-Elect** — aggregator-set by design.
- **DSGS** — the capacity and per-unit payment values are in the Guidelines Fifth Edition PDF and on
  the Olivine administration site; neither returned usable text.
- **SCE TOU-GS-3 / TOU-8 demand charges** — SCE's tariff PDFs are served from `library.sce.com` and
  returned empty bodies through the fetch tool. I captured the *structure* (Facilities-Related Demand
  billed on monthly max demand year-round; Time-Related Demand billed on summer On-Peak / winter
  Mid-Peak weekday demand; Option E is FRD-only with no TRD), which is the part that determines how a
  battery should be dispatched, but not the $/kW.
- **SDG&E Schedule AL-TOU** — SDG&E's residential "Total Rates Table" URL pattern
  (`/sites/default/files/regulatory/<date> Schedule <X> Total Rates Table.pdf`) works beautifully and
  gave exact numbers for TOU-DR1 and EV-TOU-5, but the AL-TOU equivalent 404s. The underlying tariff
  sheet is linked instead.

## 3. Things I could not check at all

- **SDG&E's business DR program page** (`/businesses/savings-center/energy-management-programs/
  demand-response`). I hit a session tool limit on the last pass. **SDG&E's BIP, CBP and
  non-residential Critical Peak Pricing rows are therefore missing** — SDG&E almost certainly runs
  all three (they are CPUC-mandated statewide DR programs and SDG&E is named in the CPUC ELRP page as
  a participating IOU), but I will not write rows I did not see. **This is the biggest single hole in
  the chunk and should be a short follow-up run.**
- **SCE's Base Interruptible Program** row — same reason. SCE runs BIP (CPUC statewide program) but I
  did not reach its tariff sheet, so no row.
- **The ACC Plus adder's actual ¢/kWh values by utility and vintage year.** CPUC and the utilities
  describe the adder qualitatively; the numeric schedule is in D.22-12-056 attachments, which I
  could not open (403 + size). **This is the second-most valuable missing number in the chunk** —
  it is the difference between a 9-year NBT pro forma and a guess.
- **The hourly Energy Export Credit values themselves.** These are 8760 values per utility per year
  and cannot be represented in a CSV cell. PG&E publishes them as a ZIP of price sheets
  (`https://www.pge.com/assets/pge/docs/vanities/PGE-EEC-Price-Sheets.zip`, 2023-2026). **That ZIP is
  the actual arbitrage signal for this whole state and belongs in the repo as a data file, not as a
  CSV cell.** Same for SCE and SDG&E equivalents.
- **PG&E Peak Day Pricing credit/surcharge for schedules other than B-19.** I captured B-19's PDP
  numbers ($0.90/kWh event charge; $6.72/kW peak-summer demand credit at secondary voltage) from the
  B-19 tariff; other schedules have their own.
- **PG&E Schedule B-20 / B-10 / A-series** demand-charge rates. Only B-19 was captured.
- **SCE and SDG&E EV commercial rates**, PG&E's commercial EV rate (BEV-1/BEV-2).
- **SGIP Heat Pump Water Heater program** (D.22-04-036, established through 2025) — noted, no row.

## 4. Volatility warning — read this before using any number here

Every California figure in this chunk carries an effective date in the cell because they move fast.
Concretely, within the last twelve months:

- PG&E residential rates changed **2026-03-01** (Advice 7846-E) and again **2026-06-01**
  (Advice 7921-E, D.26-04-036); E-ELEC's applicability sheet changed again **2026-08-28**
  (Advice 7975-E).
- PG&E B-BIP was revised **2026-07-10** (Advice 7942-E, Res. E-5451) on top of a 2025-05-17 rate change.
- SDG&E TOU-DR1 is effective **2026-01-01**; EV-TOU-5 is effective **2026-08-01**; SDG&E TOU-DR was
  re-issued **2026-04-01**. Three different effective dates across three residential schedules.
- PG&E's Business Solar Billing Plan billing only went live in **March 2026**.

**SCE's rate values are the weakest in the chunk**: they come from SCE's own rate-plan page, are
rounded to whole cents, and **SCE publishes no effective date on that page**. I flagged this in the
`peak_offpeak_rates` cell of every SCE rate row. Treat SCE numbers as indicative and re-pull from the
tariff book before using them in a model.

The region plan's closing note — "build the `last_verified` staleness indicator into the map before
loading CA" — is correct and I'd raise it to a blocker for the SCE rows specifically.

## 5. Structural note on the statewide entity

I used `California statewide (CPUC / CEC / GO-Biz administered)` for: the NBT framework, the NEM 2.0
legacy regime, the NEM-forfeiture threshold rule, all SGIP budgets, the ELRP framework, Power Saver
Rewards, DRAM, and DSGS. I *additionally* wrote per-utility ELRP rows, because enrollment,
administration and the implementing tariff differ by utility and a join on `utility_name` would
otherwise return nothing for ELRP. That is deliberate duplication of a framework row plus three
implementation rows, not an accident — collapse it if the loader treats it as double-counting.

The NEM-forfeiture row is a *rule*, not a program, and carries blank `incentive_structure`. It is in
the CSV rather than only in this file because it is the single fact most likely to be queried.
