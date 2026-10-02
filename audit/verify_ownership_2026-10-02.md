# Verify: ownerOf presence-scan fallback (2026-10-02)
Method: Playwright/Chromium, Leaflet routed to local 1.9.4; new (working tree, :8767) vs `git show HEAD:docs/index.html` (:8768, same data dir). ownerOf evaluated in-page for all 2,914 features.

| # | Check | Result |
|---|---|---|
| 1a | Unknown among 993 target territories | PASS: 56 -> 0 |
| 1b | Non-target polygons unchanged | FAIL (minor): 2 changed, both from JOIN_EXCLUDE (earlier diff), not `ow` (see below) |
| 1c | Same feature set old/new | PASS (2,914) |
| 2 | 8 drawer spot-checks (header shows new owner) | PASS 8/8 shown correctly; 1 plausibility flag (Modern Electric Water Co) |
| 3 | Municipal -> Federal/State | 13 territories; FLAG, inconsistent (see below) |
| 4 | OWNER_COLORS render | N/A/FAIL: no ownership color-by view exists (radios: util/rto/count/type); OWNER_COLORS is defined but unused. Every new label has a color key (0 missing). Cycling rto/count/type/util views: no pageerrors; only console noise is blocked external hosts (ERR_FAILED) and the existing "Unmatched payload" warning, identical to old build |

## Changes: 73 features
| old -> new | n | HIFLD TYPE |
|---|---|---|
| Unknown -> Cooperative | 35 | NOT AVAILABLE |
| Unknown -> Municipal | 19 | NOT AVAILABLE |
| Municipal -> Federal/State | 13 | POLITICAL SUBDIVISION |
| Unknown -> Municipal | 1 | COMMUNITY CHOICE AGGREGATOR (3CE) |
| Unknown -> Federal/State | 1 | NOT AVAILABLE (Custer PPD, NE) |
| Municipal -> Cooperative | 1 | MUNICIPAL (3075 Carroll County TN) |
| Cooperative -> Municipal | 1 | COOPERATIVE (12744 Modern Electric Water Co, WA) |
| IOU -> Cooperative | 1 | COOPERATIVE (11788 Consumers Energy, IA; JOIN_EXCLUDE) |
| Cooperative -> Unknown | 1 | NOT AVAILABLE (3726 Clay Electric Coop, IL; JOIN_EXCLUDE) |

Totals new vs old: Unknown 1684 -> 1629; Cooperative 554 -> 589; Municipal 508 -> 515; IOU 154 -> 153; Federal/State 14 -> 28.

## Flags
1. Non-target changes (2): 11788 now Cooperative (correct, IA co-op; previously mis-joined to MI IOU). 3726 Clay Electric Coop (IL) now Unknown; it is a co-op, HIFLD TYPE is NOT AVAILABLE and it has no presence row, so label regressed from (wrongly joined) Cooperative to Unknown. Consider an `ow` override.
2. 3075 Carroll County (TN): HIFLD Municipal -> Cooperative from scan ("Carroll County Electric Cooperative"). Possibly a scan misidentification (TN county electric departments are usually municipal); verify. Confidence low-medium.
3. 12744 Modern Electric Water Co (WA): HIFLD Cooperative -> Municipal. Scan overrides HIFLD without a clear basis; verify (confidence low).
4. Federal/State taxonomy: 13 Municipal -> Federal/State are public power / people's utility / electrical districts (Northern Wasco, Tillamook PUD, Central Lincoln, Emerald, Columbia River, Overton NV, Pinal AZ ED3, Loup River, Norris, Southern, Cornhusker, Dawson, Elkhorn NE) plus Custer PPD from Unknown. Legal status is political subdivision; HIFLD maps that to Municipal (40 POLITICAL SUBDIVISION polygons remain Municipal, e.g. WA PUDs: Klickitat, Lewis, Okanogan, Grant, Pend Oreille, Mason). Existing Federal/State members are TVA, BPA, WAPA, BIA, tribal, state authorities (LIPA, SC PSA, GRDA, CRC NV). SPEC.md says only "federal-state" with no definition. Result: same legal form now splits across Municipal (WA PUDs) and Federal/State (NE/OR districts). Recommend: map the scan to Municipal (or add a "Public power district" bucket), reserve Federal/State for federal/state/tribal entities. SRP not found by name in the polygons.
5. Plausible: Unknown->Cooperative/Municipal samples (EMCs, REMCs, Clearwater Power, SDCEA, GCEA, Heber L&P, Truckee Donner PUD, Tahlequah PWA, 3CE) all consistent with names. All 56 target Unknowns resolved. No Municipal-labeled co-op seen among those besides flag 2/3.
6. OWNER_COLORS has no UI hook; SPEC lists ownership as "present where researched" so confirm whether a view is intended.
