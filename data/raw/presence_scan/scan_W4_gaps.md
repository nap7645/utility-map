# Gaps — scan_W4 (Nevada, Arizona, New Mexico + El Paso Electric)

30/30 targets have a row; validator passes clean (30 rows x 17 fields). Cells left `Unknown`
below are gaps worth a follow-up pass, roughly in priority order (customer count).

## High-value follow-ups

- **El Paso Electric Co (5701, NM jurisdiction)** — ci_habit/ci_dispatch Unknown. Only found a
  reference to an "Alternative Time-of-Day option" for loads >300kW under Schedule 24 and a
  Demand Adjustment Rider for DCFC EV charging; never confirmed the actual NM Schedule 24 tariff
  text. Read the NM rate tariff PDFs at epelectric.com/customer-service/rates-and-regulations
  directly.
- **Mohave Electric Cooperative (21538)** — ci_habit/ci_dispatch/res_dispatch Unknown. Rates page
  mentions "demand/TOU optimization" and SunWatts/DGS but the actual commercial rate PDFs weren't
  opened. Check mohaveelectric.com's full rate schedule list (parallel to the RTOU residential
  tariff already found).
- **Navajo Tribal Utility Authority (13314)** — all four cells Unknown. Rate info on ntua.com is
  published only as image files (JPGs), which this pass could not OCR/parse. Worth a dedicated
  image-read pass or a direct ask to NTUA for the PDF tariff.
- **City of Gallup (6930)** — all four cells Unknown. gallupnm.gov's rate-schedule pages returned
  empty on fetch (likely JS-rendered or an ADID/archive viewer). Try the direct PDF links under
  gallupnm.gov/ArchiveCenter or contact Customer Care.
- **City of Farmington / FEUS (6204)** — all four cells Unknown. PDF fetches
  (farmingtonnm.gov/DocumentCenter/View/24045 and .../24058) returned empty content in this
  session's fetch tool; likely a binary-PDF handling issue rather than true absence. Retry with a
  PDF-capable fetch or download+read tool.
- **Mora-San Miguel Electric Cooperative (12901)** — all four cells Unknown. Only found the
  "Charges & Rules" fee page; the actual rate-schedule PDFs (Residential/Commercial/Power Service)
  weren't located/linked from the site pages crawled. Search NMPRC's cooperative filing directory
  directly.
- **Overton Power District No. 5 (14245)** — all four cells Unknown. The 2026 rate schedule is
  published as an image-based PDF (2026-Rate-Schedule-UPDATED.pdf) that couldn't be parsed in this
  pass.

## Medium-priority gaps (one or two cells missing on an otherwise-sourced row)

- **SRP (16572)**, **ED3 (30518)**, and **Overton (14245)** are special districts/political
  subdivisions with no clean fit in IOU/Cooperative/Municipal/Federal/State — flagged inline in
  notes as classed "Federal/State" for lack of a better bucket; may need a vocabulary update
  (e.g. a "Special District" ownership_type) or reclassification as Municipal.
- SSVEC (18280), Trico (19189), Navopache (13318), Mohave (21538), ED3 (30518), Mesa (12351) —
  res_dispatch and/or ci_dispatch Unknown where only the rate tariff (not the program pages) was
  reviewed.
- Kit Carson (10378) — res_dispatch Unknown (no BYOT/thermostat program found alongside its
  strong TOU/interruptible tariff lineup).
- Continental Divide (4265) — ci_habit Unknown (unclear whether the TOU rate's "<50kVA" scope
  includes the Commercial General Service class or residential only).
- Socorro Electric (17492) — res_habit/res_dispatch/ci_habit Unknown; Rate 6 (Residential) and
  Rate 9 (General Service w/ ETS) tariffs were referenced but not opened.
- Valley Electric Association (19840) — res_dispatch/ci_dispatch Unknown.
- Lea County Electric (10817), Central Valley Electric (3287), Farmers Electric NM (6198) — all
  SPP-member co-ops; res_dispatch left Unknown across all three (no DR/thermostat program page
  found, only the rate-schedule lists).

## Search budget

Used roughly 25 WebSearch calls + ~20 direct page fetches out of the ~200-call budget — well
within budget. The gaps above are from PDF/JS-fetch failures and pages not yet crawled, not
budget exhaustion.

## fill3b pass (2026-10-02)
- Overton (14245): res_dispatch=No - OPD5 smart-meter FAQ states it offers no opt-in thermostat/peak demand programs and has no plans. Habit/C&I cells unresolved (rate PDF unreadable).
- Farmington, NTUA, Mora-San Miguel, Gallup: rate pages image/PDF-only, robots-blocked, or search returned nothing; Unknown remain.
