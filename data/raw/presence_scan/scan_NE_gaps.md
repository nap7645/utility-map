# Gaps — New England presence scan (scan_NE.csv)

Run date: 2026-09-26. 40/40 targets have rows; validator passes (17 fields, all eia_ids present).
Many small munis and co-ops came back `Unknown` on `res_habit`/`ci_habit`/`ci_dispatch` because
their own sites don't publish a clear tariff-design page — that's a real gap, not laziness; see
notes below on how to close it.

## RTO note verified
- Confirmed rate/program pages for all 40 targets sit under ISO-NE except Eastern Maine Electric
  Coop, tagged `Other-nonRTO` per the region-plan lead. **This was not independently confirmed
  against an ISO-NE or NERC membership list** — EMEC's own site gave no RTO/BA information, so
  the tag rests on the region-plan's unverified lead alone. Flag for a follow-up check against
  ISO-NE's participant list or FERC Form 861 balancing-authority data.
- Versant Power (eia 1179) is tagged `ISO-NE` for the whole utility because its larger Bangor
  Hydro District is ISO-NE and HIFLD gives one combined record, but its Maine Public District
  (northern Maine) is flagged in the notes column as NOT ISO-NE (Northern Maine Independent
  System Administrator / New Brunswick interconnection) per the region-plan lead — also not
  independently re-verified this pass, just carried forward and flagged.

## Cells left `Unknown` and why
- **MA municipal light plants** (Belmont, Danvers, Hingham, Mansfield, Marblehead, Norwood,
  Shrewsbury, Wakefield, Wellesley, and MMWEC/NextZero members generally): confirmed via
  NextZero's own published municipality list and/or the muni's own rebate page that
  `res_dispatch` = Yes (Connected Homes battery/thermostat/EV dispatch), but could not confirm
  `res_habit` (TOU rate design), `ci_habit`, or `ci_dispatch` because none of these towns publish
  a clear commercial rate-design or C&I DR page that surfaced in search. A follow-up pass reading
  each town's actual rate schedule PDF (not just program pages) would close this — reasonable
  next step, ~15 munis, one search each.
- **Taunton, Middleborough, Braintree, North Attleborough, Norwich, Wallingford, Groton**:
  checked each utility's own site; found no thermostat/battery/DR program and no C&I DR program,
  written `No`. Their `res_habit`/`ci_habit` (TOU rate design) could not be confirmed either way
  and are `Unknown` rather than `No` — none of these sites has a rate-schedule page that
  surfaced in search results.
- **Hudson Light & Power** — general secondary sources describe MMWEC's NextZero program as
  serving ~21-24 municipal utilities but hudsonlight.com itself did not surface a Connected
  Homes-specific page in search; written `Unknown` rather than `Yes` because the claim isn't
  directly evidenced on the utility's own domain. Confidence tier: Unverified.
- **Westfield Gas & Electric** — could not confirm or rule out NextZero/Connected Homes
  participation; wgeld.org's own pages didn't surface a demand-response page, and it's not
  explicitly on the partial NextZero municipality list found. Unverified.
- **National Grid MA (Massachusetts Electric Co / Nantucket Electric Co)** — `res_habit` written
  `Unknown`: secondary sources (electricrates.org, tou.tools) assert National Grid MA has filed
  residential TOU/EV-TOU tariffs with the DPU, but no live public enrollment page on
  nationalgridus.com surfaced to confirm it's actually available today, so it was not marked Yes.
- **Eversource CT** — `ci_dispatch` `Unknown`: no utility-run C&I interruptible/curtailable
  tariff or DR program found on eversource.com's CT business pages (unlike MA/NH where
  ConnectedSolutions C&I and Large Business DR are explicit). Worth a direct check of the CT
  business rate-schedule PDFs.
- **Liberty Utilities NH (Granite State Electric)** — no direct tariff URL found for its TOU rate
  or C&I curtailment program; both cells rest on secondary sources (WattBuy, a general utility
  description) rather than libertyutilities.com pages that show the claim. Confidence:
  Secondary.

## Search budget
Used roughly 45 WebSearch calls plus a couple of page-summary passes (well under the ~200-call
budget), spent mostly confirming the ~15 load-bearing IOUs precisely and doing one targeted pass
per muni/co-op. No target was skipped for budget reasons.

## Recommended follow-up (not done this pass)
1. Verify EMEC's and Versant Maine Public District's actual RTO/BA membership against ISO-NE or
   FERC Form 861 data rather than carrying forward the region-plan's unverified lead.
2. Pull each MA muni's actual rate-schedule PDF (not just its rebate/program page) to fill the
   `res_habit`/`ci_habit`/`ci_dispatch` `Unknown` cells — most MMWEC munis likely have simple
   flat-rate tariffs (would resolve to `No`) but this wasn't independently confirmed.
3. Confirm Hudson Light & Power's and Westfield G&E's NextZero/Connected Homes status directly
   against MMWEC's or NextZero's current municipality list (the list seen in search results was
   partial/inconsistent across queries — different searches surfaced different subsets of the
   ~21-24 member municipalities).
