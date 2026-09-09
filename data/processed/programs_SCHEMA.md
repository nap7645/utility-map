# Shared CSV schema — MISO/PJM utility DR / TOU / BESS revenue program inventory

Output a CSV with EXACTLY these 22 columns, in this order, with this header row:

rto,state,utility_name,ownership_type,program_name,program_category,customer_segment,eligible_assets,enrollment_basis,incentive_structure,incentive_value_usd,event_limits,tariff_schedule,on_peak_window,peak_offpeak_rates,export_compensation,storage_eligible,stackable_with,program_status,source_url,last_verified,confidence

## Column definitions

- **rto**: `MISO` | `PJM` | `MISO/PJM` (utility spans both) | `PJM-market` | `MISO-market` (for RTO-level wholesale products)
- **state**: two-letter USPS. Use `multi` for RTO-level products.
- **utility_name**: legal operating-company name (e.g. `Northern States Power Co - Minnesota (Xcel Energy)`, not `Xcel`). One row per program per operating company; do NOT collapse holding-company subsidiaries.
- **ownership_type**: `IOU` | `Municipal` | `Cooperative` | `Federal/State` | `RTO` | `Third-party CSP`
- **program_name**: exact program/tariff name as the utility publishes it.
- **program_category**: one of
  - `DR-DLC` (direct load control / switch-based)
  - `DR-Curtailment` (C&I interruptible / curtailable / firm-load)
  - `DR-BYOT` (bring-your-own-thermostat)
  - `DR-BYOD` (bring-your-own-device, incl. battery/water heater/EV)
  - `VPP` (aggregated dispatchable fleet program)
  - `TOU-Rate` (time-of-use retail rate)
  - `RTP-Rate` (real-time / hourly / market-indexed retail rate)
  - `CPP-PTR` (critical peak pricing or peak-time rebate)
  - `Demand-Charge` (demand-charge-based C&I rate relevant to BESS peak shaving)
  - `EV-Rate` (EV-specific rate or managed charging program)
  - `Storage-Incentive` (upfront rebate / capacity payment for BESS)
  - `Export-Comp` (net metering, net billing, buy-all-sell-all, avoided-cost export)
  - `Wholesale-Market` (RTO product: capacity, energy, ancillary)
  - `Interconnection` (rule that gates BESS export — only if materially revenue-relevant)
- **customer_segment**: `Residential` | `SmallC&I` | `LargeC&I` | `All` | semicolon-joined combo
- **eligible_assets**: semicolon-joined from: `Thermostat/AC`, `ElectricWaterHeater`, `HeatPump`, `SpaceHeat`, `Battery`, `EV/EVSE`, `V2G`, `Solar+Storage`, `Generator`, `PoolPump`, `IrrigationPump`, `GeneralLoad`, `Any`
- **enrollment_basis**: `Opt-in` | `Opt-out` | `Default` | `Closed to new` | `Pilot` | `Waitlist`
- **incentive_structure**: short phrase — e.g. `$/kW-yr capacity payment`, `$/event bill credit`, `flat annual bill credit`, `upfront $/kWh rebate`, `rate discount`, `$/kWh performance`
- **incentive_value_usd**: the number(s) with units, e.g. `$8.00/kW-month summer`, `$100 enroll + $50/yr`, `$300/kW up to $5,000`. Blank if not published.
- **event_limits**: e.g. `max 15 events/yr, 4 hr max, Jun-Sep 2-7pm, 100 hr/yr cap`
- **tariff_schedule**: rate/rider code, e.g. `Rider A-6`, `Sched. RSTOU`, `Rate 32`
- **on_peak_window**: e.g. `Weekdays 3-8pm Jun-Sep; 6-10am & 5-9pm Oct-May`
- **peak_offpeak_rates**: e.g. `on 28.4c / mid 14.1c / off 8.2c per kWh`
- **export_compensation**: e.g. `1:1 net metering to 20kW`, `avoided cost 3.1c/kWh`, `net billing at LMP+`, `no export allowed`
- **storage_eligible**: `Yes` | `No` | `Yes-restricted` | `Unclear` — can a customer-sited battery participate / capture this value?
- **stackable_with**: other program names at the same utility this can be combined with; `Unknown` if not stated.
- **program_status**: `Active` | `Closed to new enrollment` | `Pilot` | `Proposed/pending` | `Terminated`
- **source_url**: DIRECT deep link to the tariff sheet, program page, or regulatory filing. NOT a homepage. REQUIRED.
- **last_verified**: `2026-08-08`
- **confidence** — write ONE of these (the column name is kept for compatibility, the meaning is the evidence tier):
  - `Primary` — the `source_url` IS the source: the utility's own tariff sheet or program page, a regulator order/rule, an RTO manual, or a statute. Clicking it shows the claim.
  - `Secondary` — the `source_url` reports on the source: news, DSIRE/OpenEI, trade press, a G&T page describing a member's program, a PUC summary of a tariff.
  - `Unverified` — no usable link, or the link does not actually show the claim. Inferred from a state pattern or G&T membership.
  Older files use High/Medium/Low; `scripts/source_tier.py` maps those and the URL domain to the tier above. Prefer the new vocabulary.

## Hard rules

1. **Never invent a row.** If a utility has no findable program in a category, do not emit a row for it. Emit a row in the `_gaps` file instead (see below).
2. **Never invent a value.** Leave a cell blank rather than guessing. Blank is a valid, expected answer for many cells.
3. **source_url is mandatory on every row.** A row without a working deep link should be marked `confidence=Low` and the best available URL given.
4. Quote any field containing a comma. Use UTF-8. No newlines inside fields.
5. Prefer the utility's own tariff PDF or program page over third-party aggregators.
6. For holding companies (AEP, FirstEnergy, Exelon, Entergy, Duke, Ameren, Evergy, AES), enumerate EACH operating company separately — programs differ by state jurisdiction.
7. Include closed/terminated programs only if they closed after 2024 (useful signal), and mark status accordingly.

## Output files

Write TWO files to the outputs directory:
- `chunk_<N>_<label>.csv` — the data, with header row.
- `chunk_<N>_<label>_gaps.md` — a short bullet list of utilities you checked but found nothing for, and utilities you could not check. This is as valuable as the data; be honest and complete.
