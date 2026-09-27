# chunk_NE_wholesale gaps (ISO-NE-market) — run of 2026-09-26

Run stopped early: search tool hit session limit after 8 rows. Relaunch with the same prompt to resume (skill section 2).

## Rows written (8)
ADCR (FCM), FCA 18 price, FCA 17 price, Pay-for-Performance PPR, CAR-PD / FCA 19 delay, CAR-SA, Order 2222 DERA energy/AS models, IMM 2025 energy prices.

## Products still missing (no row yet)
- Order 2222 capacity participation (Distributed Energy Capacity Resource, DECR) — search snippet says implementation Feb 1 2027 for CCP 2028/29; NOT verified on an ISO page.
- Net-metered / BTM eligibility restrictions for DERs in DERAs (FERC ER22-983 orders on metering, 182 FERC ¶ 61,137) — not researched.
- Demand Response Resource energy market participation (Order 745 Net Benefits Offer Price Threshold, Market Rule 1 III.8B baselines) — own row not yet written; DRR 100 kW / DRA 10 kW / 5-min telemetry facts verified (NECPUC Oct 2024 ISO presentation).
- Real-time reserves (TMSR/TMNSR/TMOR) DRR eligibility and prices — not researched.
- Day-Ahead Ancillary Services (DASI/DAAS, live Mar 1 2025): products FRS (10/30-min) and EIR (60-min) plus Forecast Energy Requirement confirmed in IMM 2025 AMR; costs $137M (4 reserve products) and FER $529M Mar-Dec 2025. Per-product $/MWh averages and DRR/battery eligibility not verified. ISO planned FERC filing of DAAS changes summer 2026 — status unverified.
- Regulation market (ATRR; min 0.1 MW under Order 2222 model) — clearing prices not found; IMM says regulation prices "fell significantly" and battery revenues just under $10/kW-month in 2025 (no numeric regulation price captured).
- Passive On-Peak / Seasonal Peak Demand Capacity Resources (>=100 kW, Manual M-MVDR) — facts found but row not written.
- Small-utility opt-in / state opt-out: region file says "no state opt-outs"; not verified.
- Manual section numbers (M-20, M-27, M-11, M-MVDR) not verified section-by-section; tariff cites in rows are to Section III.13 / III.8B / III.13.7 at the section level only.

## Soft spots in written rows
- ADCR row cites an ISO presentation hosted on necpuc.org, not the manual itself.
- FCA 16 value (~$2.59/kW-month) is the IMM's CCP-16 figure, not the FCA 16 results notice.
- FCA 17 value is the preliminary press-release price.
- CAR-SA source URL taken from ISO key-project page link; PDF not opened.

## Resume run 2026-09-26 — 14 rows appended (file now 22 data rows)
Added: DRR energy participation; Demand Reduction Threshold Price (Order 745 floor); Passive On-Peak; Passive Seasonal Peak; Order 2222 DECR capacity effective date; Order 2222 BTM metering/retail-program restrictions; Order 2222 small-utility opt-in; DER equivalent CNRC (ER26-1956); DA A/S FRS (TMSR/TMNSR/TMOR); DA A/S EIR/FERP; DA A/S 2026 changes; real-time reserves; regulation (ATRR); RERRA/Order 719 DR aggregation opt-out.

### Still unverified / blank
- Demand Reduction Threshold Price monthly $/MWh values: ISO Express report is JS-only; not retrieved. Section III.1.10.1A(f) cite comes from Tariff Section I.2.2 definition (search snippet); Market Rule 1 PDF (mr1_sec_1_12.pdf) returned no text.
- Market Rule 1 III.8B baseline text not opened; baseline description (10-weekday average + 15-minute pre-dispatch adjustment) is from ISO Newswire FAQ (Jan 2025).
- DA A/S per-product monthly clearing prices are only in charts (IMM DA A/S assessment Fig 3-3); only seasonal FRS ranges and Fall 2025 TMOR monthly averages captured. Battery/DRR share of DA A/S awards not reported.
- DA A/S 2026 changes: FERC Sep 14 2026 acceptance (ER26-3176-000, effective Oct 22 2026, ~$23M/yr savings) is from a trade-press search snippet only (Troutman page returned empty) — marked Secondary. ISO readiness page (Aug 13 2026) still said "TBA".
- Regulation: average $/MW-hr capacity and mileage prices not captured (IMM AMR section 8.3 / Table 8-2 beyond fetched text). A secondary source (Modo) claims $31/MW-hr (2022) to $14/MW-hr (2025) — not used.
- Real-time reserve tariff section number not verified.
- Order 2222 capacity (DECR): ISO says effective for CCP 2028-29 (CCP 19); the Feb 1 2027 implementation date from the prior run's search snippet was NOT confirmed and was not used. How CAR-PD/CAR-SA filings will restate DECR rules is pending.
- BTM metering: the ISO 2024/2025 decks say BTM DER meters sit at the Retail Delivery Point, with submetering only if the Host Utility can support it. FERC's Mar 2023 order had faulted that proposal; I did not open the later FERC orders to confirm it was finally accepted. Whether net-metered customers may join is left to retail program terms (the utility checks "not in a retail program that prohibits wholesale participation"). The rules in each state were not researched.
- Small-utility (<= 4 million MWh) opt-in: no list of opted-in utilities/RERRAs found.
- State opt-outs: mechanism confirmed (ISO service-territory notification form), but no state-by-state positions published; region file's "no state opt-outs" remains unverified.
