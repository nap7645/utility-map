# CAISO wholesale (CAISO-market) — gaps and corrections

Last updated 2026-09-23. Rows 1-8 were written by an earlier agent that was cut off. Rows 9-12 (DRAM, RA pathway, Ancillary Services, WEIM/EDAM) were added in the continuation run. 12 rows total.

## Leads that were wrong or needed correcting
- **"RA value via DRAM" (plans/rto_caiso.md)** — outdated. CPUC D.24-04-006 (Apr 18 2024) ended DRAM at PG&E, SCE and SDG&E by Dec 31 2024. It is in the file as `Terminated`. Third-party RA value now comes from bilateral RA contracts with IOUs or CCAs, CBP / CBP Elect, and CEC DSGS.
- **"DERP aggregation earns RA"** — wrong. CAISO's PDR-DERP-NGR-LFA comparison matrix says the DERP model is ineligible to provide RA. Only PDR (and PDR-LSR on the curtailment side) and RDRR can be shown on Supply Plans.
- **"Ancillary services incl. Reg Up/Down reachable by BTM aggregations"** — partly wrong. PDR and DERA/HDERA can provide Spin and Non-Spin only. The matrix lists Regulation only under the NGR model, which needs ISO interconnection or NRI and wholesale (ISO or SC) metering of the device. RDRR and the PDR-LSR Consumption ID can't provide any AS.
- **DERA minimum size** — the matrix still says 0.5 MW in its "ISO Contract Requirements" cell. That text is stale: since the Order 2222 changes the tariff minimum has been 100 kW. Rows 1-2 correctly use 100 kW.
- **Third-party aggregation restriction** — there is none. California has not opted out. This is covered in the existing row "Small utility opt-in gate and state aggregation rules", which states it explicitly. I did not add a separate row, to avoid duplication. The only gate is the small-utility (4 million MWh or less) RERRA opt-in.
- **WEIM/EDAM for LADWP / SMUD / TID customer batteries** — there's no direct path. PDR/DERA are models for the CAISO balancing area only. In WEIM, DR enters only as the BA's Load Forecast Adjustment, with no settlement to a DR provider. EDAM entry for these BAs is planned for 2027 (IID 2028).

## Unverified or partly verified
- **Flexible RA MOO window for DR**: the matrix text reads "May-September 7:00 am-12:00 pm / October-April 3:00-8:00 pm". The summer morning window looks unusual. Check it against the current BPM for Reliability Requirements Section 7.1.2 before relying on it. The only Reliability Requirements BPM I could fetch in full was v37 (2018), so the current section numbers come from the matrix footnotes, not the BPM itself.
- **CPUC DR counting after 2025**: the Slice-of-Day guide I cited is the 2025 guide. I did not check the 2026 or 2027 guides for changes to DR showing hours, the 8.3% DR MCC bucket, or the planning reserve margin.
- **RA contract prices for DR**: not published, so the cell is blank. DMM 2025 reports monthly RA from LSE-scheduled DR averaging 820 MW and third-party DR RA averaging about 102 MW. These are quantities, not prices.
- **WEIM membership of LADWP and BANC**: stated from general knowledge and the EDAM participant page, which lists them as EDAM signatories. The WEIM start dates for LADWP and BANC were not confirmed from a primary page. TID's WEIM start (2021) is confirmed by a CAISO news release.
- **EDAM tariff Section 33 treatment of DER/DR** was not read. The "day-ahead LFA option pending EDAM tariff approval" claim comes from the Nov 2023 comparison matrix and may have changed since EDAM went live on May 1 2026.
- **DERA eligibility for Regulation** under Tariff 4.17: the claim that DERA doesn't provide Regulation rests on the matrix listing and on the Order 2222 BRS modeling DERA as NON-REM generic NGR. I did not confirm it in the tariff text.
- **AS prices** are DMM quantity-weighted averages for 2024 and 2025 (DMM 2025 Annual Report, Figures 12.4 and 12.5). They are not monthly or peak values, and 2026 Q1 values were not pulled.
- The existing PDR row's DMM DR revenue figures are for 2024. The 2025 Annual Report section 16.10 figures were not extracted to update them.

## Not covered (out of scope or no CAISO product)
- ELRP (CPUC) and DSGS (CEC) are state programs, not CAISO products. They belong in the CA utility/state program chunks.
- Capacity Procurement Mechanism: CAISO backstop procurement, not reachable by BTM aggregations. No row.
