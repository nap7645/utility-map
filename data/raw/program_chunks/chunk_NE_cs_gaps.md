# chunk_NE_cs gaps (ISO-NE ConnectedSolutions utilities + GMP), last_verified 2026-09-26

## Checked, nothing found (or confirmed not offered)
- **Fitchburg Gas & Electric Light Co (Unitil MA): residential ConnectedSolutions battery.** Mass Save / NG MA program materials (dated 2026-03-13) say Unitil customers "are not able to participate currently". No row emitted. Unitil MA *does* take part in C&I Daily/Targeted Dispatch and in thermostats (rows emitted).
- **Unitil Energy Systems (NH): battery DR / ConnectedSolutions.** Found no Unitil NH battery DR program. Checked unitil.com TOU and rate pages. No row.
- **MA residential winter ConnectedSolutions season.** Current MA materials list summer only (Jun-Sep). The NG FAQ text about a "winter incentive" looks like leftover wording. No winter $/kW row for MA. CT ESS has about 5 winter events (captured). RI residential has summer only.
- **Rhode Island Energy TOU rate.** Found no residential TOU or off-peak EV rebate on RIE pages or RIPUC search results. Treat as not found, not as a confirmed "No".

## Could not verify / values missing
- **MA Clean Peak Standard ACP for 2026.** The row quotes the ACP schedule in the original 2020 225 CMR 21.00 ($41.92/MWh for 2026). A search snippet claimed "$65/MWh 2026-2032" (possibly from 2024 climate legislation). Not verified. The 2024 emergency amendments changed the Minimum Standard for 2024-2028 (new values are only in a chart) and added the NTRM. Pull the current consolidated 225 CMR 21.00 before relying on the ACP or the minimum standard.
- **SMART 3.0 Energy Storage Adder $ value.** DOER lists "Energy Storage Multiplier $0.04" for PY2026. The actual adder comes from a formula (storage kW/kWh vs PV kW). The calculator workbook was not opened.
- **SMART 1.0/2.0 storage adder values**: not pulled. Row is marked Closed.
- **Eversource CT Rate 7 and Eversource NH R-OTOD-2 c/kWh.** Eversource tariff and summary PDFs came back empty. Only the TOU windows are captured (NH window is from tou.tools, so Secondary).
- **Energize CT C&I Daily/Targeted Curtailment base $/kW** (CL&P, UI): not published on the EnergizeCT page. Only the $10/kW weekend bonus and $1,500 meter bonus are captured.
- **NG MA ConnectedSolutions+ (locational)** enhanced $ amounts: not published on the pages checked.
- **Eversource NH Small Business Battery Storage**: page exists, but incentive values were not pulled (Unverified row).
- **RI Commerce REF storage adder $**: existence confirmed only through the OER ESR FAQ (mutually exclusive). Value not pulled (Unverified row).
- **RI net metering 20% credit reduction for projects after 2023-04-15.** Taken from the OER summary of RIGL 39-26.4-2. Scope (which project types, 275 MW limit) not confirmed in the statute text.
- **RI Energy EVDR ($50 + $20/yr)** and **Cape Light CVEO**: taken from search result or aggregator text. Program guides not opened (Secondary).
- **CT RRES rates for UI**: the Eversource help-center page says the rates apply to CT RRES. UI's own page was not opened (UI RRES rows Secondary).
- **CT ESS performance $/kW**: the page gives $/kW by years 1-5 and 6-10 but does not say whether it is per year or split summer/winter. The ~50 summer + ~5 winter events are stated. Check the Program Manual (rev. 2026-01-27) for the seasonal split.
- **GMP ESS lease and BYOD tariffs** both say "available until September 30, 2026 unless otherwise ordered", which is 4 days after last_verified. Recheck in October 2026 for extension or replacement. The GMP lease/warranty PDF (2026-04) returned empty.
- **GMP net metering** uses the statewide blended residential rate ($0.2071 from 2026-08-01). The order notes some utilities differ. GMP's own compliance tariff was not opened.
- **MA 2025-2027 three-year plan changes to C&I Daily Dispatch ($200/kW-summer)**: the latest offering materials linked by Mass Save are dated 2023-06-08. No newer C&I rate sheet was found.
- **NH NEM successor (DE 22-060 / Order 27,074)**: NEM 2.0 terms captured from the NH DOE overview. The status of any post-2025 successor tariff was not confirmed.

## Staleness flags (program-year sensitive)
- RI ConnectedSolutions rates are set for 2024-2026. The 2027-2029 rates are "TBD" in the next 3-year plan.
- CT ESS was redesigned for applications on or after 2026-04-01. The legacy design is closed.
- MA heat pump rate is under further DPU review (D.P.U. 25-08).
- SMART 3.0 PY2027 draft report is due 2026-10-01.
