# Tariff pilot log (Phase B, 2026-10-16)
Files: pilot_tariffs.csv (17 schedules), pilot_periods.csv (122 rows). Validation: all 17 schedules x weekday/weekend cover 12x24 exactly once; tier>0 rows mirror a tier-0 block (script output "ALL OK").
Counts below are approximate WebFetch/WebSearch calls.

## 17609 Southern California Edison (~16 fetches, ~4 searches)
Captured: TOU-D-4-9PM, TOU-D-PRIME, Tiered (Schedule D), all residential, from sce.com rate-plan pages. Prices are published rounded to whole cents, bundled delivery+generation as SCE shows them; base services charge $0.79/day (fixed_units $/day).
Not captured:
- Small commercial (GS-1 / TOU-GS-1 and TOU options): no price or customer charge on any sce.com page or fact sheet reachable; tariff PDFs sit behind sharepoint links, and a guessed PDF URL failed. Zero C&I rows.
- Effective date for the two TOU plans: page states none (blank). Tiered says "Current rates as of 10/1/26", used as its date.
- Default status: no page says which plan is default (is_default blank for all three).
- TOU-D-4-9PM baseline credit ($0.09/kWh up to baseline) not coded as a tier; baseline kWh is region-specific. Winter super-off-peak 8am-4pm is read from the page's period listing (end time implied, also matches the older comparison page).
- Page values are not tariff-sheet values; Phase C should check against the CPUC tariff.

## 3046 Duke Energy Progress NC (~13 fetches, ~4 searches): NOTHING CAPTURED
Every duke-energy.com tariff PDF (RES, R-TOU-CPP; both www and p-cd hosts), duke-energy.com/rates and the NCUC filing returned fetch errors. The one page that loaded (new-rates-nc, 2023) has no prices; it only says residential basic customer charge is $14/month and R-TOU/R-TOUD/R-TOU-CPP exist. Third-party sites (tou.tools etc.) list schedule names and an Oct 1, 2025 date but no prices, and are not a primary source. Zero rows written; no numbers estimated. Needs a different fetch route (browser tool) or the NCUC docket.

## 16534 SMUD (~7 fetches, 1 search): good
Captured: R-TOD 5-8pm (default), R-TOD Low Use, R Fixed Rate, CITS-0 (C&I TOD Secondary 0-20 kW, with demand $2.389/kW). Prices are the Jan 1 2026 column of the schedule (sheet dated 2025-06-20). One bundled energy price.
Not captured / caveats:
- Critical Peak Pricing (RTC1): schedule gives discount and event price only on smud.org; not read.
- GFN (unmetered small nondemand) and CITS-1 (21-299 kW) not coded.
- Holidays are off-peak per schedule; not coded. EV credit (-$0.015/kWh midnight-6am) is in notes only.
- A May 2026 news item suggested a summer price change; I did not verify, the page and schedule I read show the 2026 values above. CITS-0 flagged default because it is the only metered <=20 kW schedule in the source.

## 19436 Ameren Missouri (~6 fetches, 2 searches): good
Captured residential: 1(M) Anytime (default), Evening/Morning Saver, Smart Saver Option A, Overnight Saver Option A, Ultimate Saver (demand). C&I: 2(M) Small General Service Standard (default), Overnight Saver.
Caveats:
- Riders FAC, EEIC, RESRAM are not in the energy prices (sheets do not state amounts). Low-income charge ($0.19 res, $0.26 SGS per month) and $1.50 non-AMI meter charge are in notes, not in fixed.
- Evening/Morning Saver peak price = base + stated on-peak adder, summed by me.
- Ultimate Saver seasonal demand ($9.28 summer / $3.83 winter per kW) is in note only; the schema has one flat demand field.
- Smart Saver / Overnight Option B (summer-only TOU) not coded. SGS Winter "Seasonal Use" block (5.81c, customer-specific threshold), three-phase customer charge ($25.73), and Legacy TOD (hours in Rider I, not fetched) not coded.
- Sheets carry different effective dates (2025-06-01 vs 2026-06-01); each schedule uses its own. Holidays not coded.

## 14626 Pedernales Electric Coop (~6 fetches, 1 search)
Captured: Residential flat (default), Residential Time-of-Use, Small Power three-phase flat. Bundled co-op: energy = delivery + transmission + base power, summed by me from the page's line items (page says the bill is the sum).
Not captured / caveats:
- Source never distinguishes weekday vs weekend for TOU; same hours coded for both day types (note on row). TOU fixed charge assumed equal to flat ($32.50), not stated on TOU page.
- No separate EV or demand rate listed for residential. Small Power TOU option exists but hours/prices not on its page. Small Power single-phase not coded: page figures conflict (base $0.06, delivery $0.02, plus an unlabeled second table). Small Power effective date not stated; set to 2026-03-01 (base-power change) by assumption, flagged in note.
- The residential flat page gives no effective date; 2026-03-01 is from the 2026 rate update page (base power). Delivery/service charges were last adjusted March 2025 per that page.
- Franchise fees and credits (autopay, paperless) excluded.

## General
- WebFetch summaries are model-extracted from the page; values were read from the extracted text, none computed except the stated sums (PEC components, Ameren peak adder). Phase C should spot-check against source PDFs.
- Schema gaps seen: seasonal demand charge, baseline-relative tiers (tier_max_kwh is blank = ambiguous with "unlimited" for SCE tiered tier 0), fixed charge per day.
