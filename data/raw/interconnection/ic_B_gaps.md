# Cluster B (MI, IN, OH, KY) — research gaps and unverified items

## Michigan
- DTE Rider 18 sheet used (D-111 to D-116) is the ORIGINAL 2019 tariff (Case U-20162), predating PA 235 (2023). Cap %, 150kW Category 2 threshold, and 100% (vs 110%) sizing figures on that sheet have NOT been reconciled against DTE's current post-PA235 revised tariff sheets. Flagged with Medium confidence.
- DTE, Consumers Energy, UMERC: exact current outflow ¢/kWh not directly observed (DTE's is LMP-based/floating, not a fixed rate, so no static number exists; Consumers Energy's specific credit methodology was not retrieved from a primary tariff document).
- UPPCO Rate Book #8, DG Rider sheets D-72.83 and D-72.84 (Generator Interconnection Requirements, Metering Requirements) were referenced but not retrieved in full text — could contain UPPCO-specific grid-charging/non-export/storage detail not captured here.
- external_disconnect requirement at the Michigan state level (MIXDG rules) could not be confirmed as a blanket statewide mandate vs. utility discretion from the sections of R 460.901a-1026 retrieved. Left as "Utility discretion" with Medium confidence — verify against R 460.960-ish technical-requirements sections not fetched.
- Whether battery/storage kW counts toward the Michigan 550kW system-size cap or the 10% aggregate program cap was not confirmed in any source reviewed (storage_counts_toward_cap left "Unclear" statewide).
- Great Lakes Energy Cooperative, Cloverland: current published outflow/NEG rate expressed in ¢/kWh not found (Cloverland's is "full retail rate," a qualitative description, not a numeric rate).
- Holland BPW's "Distributed Energy Value" — actual ¢/kWh rate not found in the page reviewed; would require the linked DG program rate schedule/tariff PDF.
- Traverse City Light & Power's new "net billing" system (approved late 2024, effective ~March 2025) — the actual replacement outflow rate was not found; only the legacy 760kW systemwide cap and the fact of the policy change were confirmed.

## Indiana
- Duke Energy Indiana and Indiana Michigan Power EDG rates (4.2917 cents/kWh and 9.0476 cents/kWh respectively) were sourced from secondary/summary pages, not the primary IURC tariff sheet — effective dates and whether these are the CURRENT (2026) rates were not independently confirmed. Both utilities' rates update annually via March 1 compliance filings, so these figures may be stale.
- CenterPoint Energy Indiana South (formerly Vectren): no specific numeric EDG rate was found in this pass; only the existence of an IURC-approved EDG tariff and a note about a solar-advocate legal challenge to CenterPoint's methodology. Current rate is a genuine gap.
- Whether battery/storage nameplate capacity counts toward the EDG "generator nameplate capacity" cap (1MW or average annual consumption) was not confirmed in IC 8-1-40 or Rider 16 text for any Indiana utility — left "Unclear" throughout.
- IEEE 1547-2018 transition status in 170 IAC 4-4.3 (the rule reviewed cites IEEE 1547 generally without confirming which edition/date is currently in force vs. proposed) — flagged Medium confidence.
- Fixed statewide interconnection application fee schedule (equivalent to MI's or OH's fee caps) was not found for Indiana; appears to be utility-specific/tariff-specific rather than set in 170 IAC 4-4.3.
- NIPSCO's current (non-legacy) EDG-equivalent numeric rate was not independently confirmed — only the existence/structure of its "Distributed Generation Tariff Program" at 125% of market price.

## Ohio
- Ohio Edison / Illuminating Company (CEI) residential net metering cap reported as 10 kW AC in one secondary source, which conflicts with the 25 kW state-default Level-1 threshold confirmed directly from OAC 4901:1-22-06. This 10kW vs 25kW discrepancy is NOT resolved — it may reflect a legacy/pre-rule-update cap, a misreport, or a genuine utility-specific narrower cap under Schedule NEM. Needs verification against FirstEnergy's actual Schedule NEM tariff sheet.
- FirstEnergy utilities' "Rider GEN" (SSO generation charge) vs. a separately-cited "3.8-5.3 cents/kWh avoided cost" figure were not reconciled — it's unclear whether net metering credits in FirstEnergy territory use Rider GEN (the SSO generation charge, ~10-11 cents/kWh) or a lower avoided-cost figure; OAC 4901:1-10-28 text says "energy component of the SSO," which should mean Rider GEN, but the avoided-cost figure appearing in secondary sources was not explained.
- A defined statewide non-export/limited-export interconnection path (equivalent to MI's R 460.980 relay-based options) was not confirmed for Ohio in the sections of OAC 4901:1-22 reviewed — Level 1/2/3 review criteria were found, but no explicit non-export track/tariff was located.
- Whether storage/battery kW is included in the 120% sizing calculation under OAC 4901:1-10-28 was not confirmed.
- Standby charges and insurance requirements: no statewide provisions were located for Ohio in the rule sections reviewed.

## Kentucky
- Kentucky Power (AEP)'s current NMS-2 rate in cents/kWh was NOT found — only the existence of the PSC order (Case No. 2020-00349, order 5/14/2021) establishing the tariff structure. This is a genuine gap; flagged Low confidence.
- Duke Energy Kentucky: a later PSC docket (Case No. 2025-00258, order dated 6/1/2026) was referenced in search results, suggesting the NM II rate may have been revised again after the 1/1/2025 figures reported here ($0.062924 / $0.063255 per kWh) — the 2026 update was not retrieved or reconciled.
- LG&E and KU's NMS-2 rates (6.924 and 7.366 cents/kWh) are from the original 2021 PSC order; Kentucky utilities' rates are periodically revisited and the current 2026 figures were not independently confirmed.
- No statewide interconnection application fee schedule, external disconnect requirement, insurance requirement, or defined non-export/limited-export path was confirmed for Kentucky from the PSC Interconnection and Net Metering Guidelines summary reviewed — the full guidelines PDF (2008-00169 order and updates) was not fetched in full text.
- Whether storage/battery kW counts toward Kentucky's 45kW SB 100 system-size cap was not confirmed in statute or PSC guidance reviewed.
- 807 KAR citation for interconnection standards could not be pinned to a specific numbered regulation in this pass (Kentucky's interconnection rules appear to live primarily in PSC orders/guidelines rather than a single codified KAR section); rule_citation for the state row uses the SB 100/KRS/PSC-order citations rather than a KAR interconnection rule number.

## General / cross-cutting
- No source in this cluster explicitly and unambiguously answered "does adding a battery to a legacy-NEM PV system forfeit grandfathering" with a plain yes/no for every utility — Michigan is the one state with an affirmative rule-based answer (no forfeiture, per R 460.920(5)(m), provided the addition is processed per utility procedure and is not a "material modification"). Indiana, Ohio, and Kentucky did not yield a clear statutory/regulatory answer to this question in the sources reviewed; this is the single highest-value follow-up item for a future research pass, per the task's stated priority.
