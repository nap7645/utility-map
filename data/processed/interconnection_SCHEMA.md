# Schema — interconnection & export rules

Two files. **State rules set the floor; the utility file carries only deltas.** Do not duplicate a
state rule across 40 utilities.

Purpose: this data answers "is this design legal and can it export" *before* the economics engine
asks "is it profitable". It renders in the map's address-lookup drawer.

---

## FILE 1 — `interconnection_state.csv` (one row per state per rule-set)

Header, exactly, in this order:

```
state,jurisdiction_body,rule_citation,applies_to,nem_status,nem_successor,nem_cap_res_kw,nem_cap_nonres_kw,nem_aggregate_cap,nem_sizing_rule,export_credit_basis,export_credit_value,credit_rollover,annual_true_up,ic_standard,ic_fast_track_kw,ic_simplified_kw,ic_application_fee,ic_study_trigger_kw,external_disconnect,insurance_required,ic_timeline_days,storage_allowed,grid_charging_allowed,non_export_option,storage_counts_toward_cap,standby_charge,standby_threshold_kw,source_url,last_verified,confidence
```

### Columns

- **state** — two-letter USPS.
- **jurisdiction_body** — e.g. `Michigan Public Service Commission`. Who sets the rule.
- **rule_citation** — statute/rule/order number, e.g. `52 Pa. Code Ch. 75`, `MCL 460.1173`, `SEA 309`.
- **applies_to** — `IOU only` | `IOU + co-op` | `All utilities` | `IOU + muni` etc. **Critical**: in most states munis and co-ops are exempt from PUC interconnection rules and set their own. Say so.
- **nem_status** — `Full retail NEM` | `Net billing` | `Buy-all-sell-all` | `Closed to new` | `No statewide rule` | `Instantaneous netting`
- **nem_successor** — if NEM closed, what replaced it and when (e.g. `EDG rate at 125% of avoided cost, SEA 309, legacy customers grandfathered to 2047`)
- **nem_cap_res_kw** / **nem_cap_nonres_kw** — max system size eligible, kW AC. Note if AC vs DC.
- **nem_aggregate_cap** — program-wide cap, e.g. `5% of utility peak load`. Include current subscription level if published — a nearly-full cap is a deal-killer.
- **nem_sizing_rule** — e.g. `<=100% of prior 12-month consumption`, `<=110%`, `no sizing limit`
- **export_credit_basis** — `1:1 retail` | `avoided cost` | `LMP-based` | `unbundled generation rate` | `value-of-DER stack`
- **export_credit_value** — actual ¢/kWh where published, with effective date.
- **credit_rollover** — `indefinite` | `monthly` | `annual expiry` | `cash-out at avoided cost`
- **annual_true_up** — month and treatment of excess.
- **ic_standard** — `IEEE 1547-2018 + UL 1741-SB` | `IEEE 1547-2003 + UL 1741-SA` | etc. Note the transition date if pending.
- **ic_fast_track_kw** / **ic_simplified_kw** — size thresholds for expedited review tiers.
- **ic_application_fee** — statewide fee schedule if set.
- **ic_study_trigger_kw** — where impact/facilities studies become required.
- **external_disconnect** — `Required` | `Waived for inverter-based` | `Utility discretion`. Real cost and a common surprise.
- **insurance_required** — liability insurance requirement, if any.
- **ic_timeline_days** — statutory/rule review timeline.
- **storage_allowed** — may storage interconnect under this rule at all: `Yes` | `Yes-with-conditions` | `Unclear` | `No`
- **grid_charging_allowed** — **the single most important cell for arbitrage.** Can the battery charge from the grid and still export/receive credit? `Yes` | `No` | `Yes-but-not-credited` | `Requires non-export` | `Unclear`
- **non_export_option** — is there a defined non-export / limited-export interconnection path (relay/control-based)? These skip most studies and are how large C&I storage gets built fast.
- **storage_counts_toward_cap** — does battery kW count against the NEM system size cap? Changes achievable PV size.
- **standby_charge** — description if the state authorizes one.
- **standby_threshold_kw** — kW above which standby charges apply.
- **source_url** — deep link to rule/order/tariff. Required.
- **last_verified** — `2026-08-09`
- **confidence** — write ONE of these (the column name is kept for compatibility, the meaning is the evidence tier):
  - `Primary` — the `source_url` IS the source: the utility's own tariff sheet or program page, a regulator order/rule, an RTO manual, or a statute. Clicking it shows the claim.
  - `Secondary` — the `source_url` reports on the source: news, DSIRE/OpenEI, trade press, a G&T page describing a member's program, a PUC summary of a tariff.
  - `Unverified` — no usable link, or the link does not actually show the claim. Inferred from a state pattern or G&T membership.
  Older files use High/Medium/Low; `scripts/source_tier.py` maps those and the URL domain to the tier above. Prefer the new vocabulary.

---

## FILE 2 — `interconnection_utility.csv` (deltas only)

```
utility_name,state,rto,deviates_on,rule_summary,nem_cap_res_kw,nem_cap_nonres_kw,nem_aggregate_cap,aggregate_cap_status,export_credit_value,ic_application_fee,ic_study_trigger_kw,external_disconnect,non_export_option,grid_charging_allowed,standby_charge,standby_threshold_kw,storage_specific_notes,source_url,last_verified,confidence
```

- **utility_name** — must match `data/processed/programs.csv` exactly so it joins. Copy the string.
- **deviates_on** — semicolon list of which state defaults this utility departs from, e.g. `nem_cap_res_kw;standby_charge`. If a utility follows state rules with no deviation, **do not emit a row** — absence means "state default applies".
- **aggregate_cap_status** — how full is the queue, e.g. `4.1% of 5% cap used as of Q1 2026`. High value, often published in PUC annual reports.
- **storage_specific_notes** — anything storage-specific: whether a battery may be added to a legacy-NEM system without losing grandfathering (**very** high value — often the deciding factor on retrofits), AC- vs DC-coupling treatment, metering configuration required.

Municipals and cooperatives that set their own rules **belong in this file**, with `deviates_on=all` and a full rule summary, since no state rule governs them.

---

## Hard rules

1. Never invent a value. Blank beats a guess.
2. `source_url` mandatory, deep link, not a homepage.
3. Prefer the rule/order/tariff text over a summary site. DSIRE is a good index but a lagging source — use it to find the citation, then read the citation.
4. Flag anything mid-transition. Several of these states have live dockets that will change these numbers within a year; say so in the relevant cell.
5. Quote fields containing commas. No newlines inside fields. UTF-8.
