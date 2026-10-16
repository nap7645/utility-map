# Tariff schema (Rank 1, bill structure)

Two files in `data/processed/`, keyed on `eia_id` + `rate_schedule`. Scope (Nathan default 2026-10-16): residential + small C&I default rate and optional TOU / EV / demand rates. Large C&I deferred.

## tariffs.csv (one row per rate schedule)
eia_id, utility_name, sector (Residential | C&I), rate_schedule, is_default (Yes/blank), rate_type (Flat | TOU | Demand | EV-TOU | EV-Flat | EV-Demand; TOU wins if both), effective_date (YYYY-MM-DD), fixed_monthly_usd, fixed_units, min_bill, demand_flat_usd_per_kw, demand_tou_usd_per_kw_p0, demand_seasonal (text "Jun-Sep 9.28; Oct-May 3.83 ($/kW)" when the demand charge varies by season), peak_kw_min, peak_kw_max (eligibility, blank = none), source_url, urdb_label (blank for agent rows), method (URDB | Agent), tier (Primary | Secondary), last_verified, note.

## tariff_periods.csv (energy charges)
urdb_label or blank, eia_id, rate_schedule, day_type (weekday | weekend), months (e.g. "Jun-Sep" or "Jan-May,Oct-Dec"), hours (local, end-exclusive, e.g. "14-19,21-24"), period (int, same id = same price), tier (0 = first block), tier_max_kwh (blank = unlimited), energy_usd_per_kwh (base + per-kWh adjustments/riders stated on the tariff; say which in a note on the tariff row).
Rule: for each schedule and day_type, the months x hours blocks cover all 12 x 24 cells exactly once.

## Rules
- Agent rows (Phase B) come from the utility's own tariff/rate page or the state PUC filing: tier Primary. URDB rows are tier Secondary.
- Retail-choice delivery-only utilities (ERCOT TDUs, unbundled IOUs like ComEd delivery classes): record the delivery tariff and say "delivery only; supply is competitive/separate" in rate_schedule or a note; supply price is a later step.
- A blank beats a guess. No computed or estimated rates.
