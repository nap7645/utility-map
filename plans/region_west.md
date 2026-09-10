# Region plan — West (non-RTO WECC, outside CAISO)

Read `plans/PLAYBOOK.md` first. Deltas only. *Verify regional facts before relying.*

## Shape of the market

No RTO, but not one region either. Three sub-markets with different economics:

1. **Pacific Northwest** (WA, OR, ID, MT-west): hydro-dominant, low prices, winter-peaking.
   Bonneville Power Administration sells wholesale to ~130 public utilities (PUDs, munis, co-ops —
   Seattle City Light, Tacoma Power, Snohomish PUD, Clark PUD…); IOUs are Puget Sound Energy,
   Portland General Electric, PacifiCorp (Pacific Power), Avista, Idaho Power, NorthWestern MT.
   Winter peaks mean water-heater and space-heat DR, not AC. PGE's Smart Grid Test Bed and its
   residential battery VPP are the reference cases.
2. **Desert Southwest** (AZ, NM, NV, UT): summer-peaking, high solar penetration, the most
   contentious net-metering history in the country. APS, SRP (Arizona's public power giant),
   Tucson Electric, NV Energy, PNM, El Paso Electric, Rocky Mountain Power (PacifiCorp), plus
   Navajo Tribal Utility Authority.
3. **Mountain** (CO, WY, MT-east): Xcel Colorado (the region's most program-rich IOU — Colorado
   is effectively a DR/storage policy leader), Black Hills, Colorado Springs Utilities, Platte
   River / Fort Collins, Tri-State's ~40 co-ops, Holy Cross.

**Wholesale**: two real-time-only markets a BTM asset can't really reach — CAISO's WEIM (Western
Energy Imbalance Market) and SPP's WEIS. The day-ahead successors (EDAM, Markets+) are launching
2026–27 and may create DR products; capture status, expect nothing bindable yet. Model like the
Southeast: `rto = WECC-nonRTO` (or `BPA`), one explanatory row per balancing authority.

## Denominator

States: WA, OR, ID, MT, WY, CO, UT, NV, AZ, NM. Ten pulls, ≈180 records >10k. MT/WY/NM also have
SPP slivers (already handled in the SPP plan — tag by utility). PacifiCorp files under one HIFLD
record for six states; Xcel Colorado is "Public Service Co of Colorado".

## Load-bearing utilities (≈30)

PNW: PSE, PGE, Pacific Power, Avista, Idaho Power, NorthWestern, Seattle City Light, Tacoma
Power, Snohomish PUD, Clark PUD, Eugene Water & Electric, Chelan PUD, BPA (as program provider).
SW: APS, SRP, TEP, UniSource, NV Energy (north + south are separate tariffs), PNM, El Paso
Electric, Rocky Mountain Power, Navajo TUA.
Mountain: Xcel Colorado, Black Hills CO, Colorado Springs Utilities, Fort Collins, Platte River
members, Holy Cross, Tri-State (as G&T), United Power, Intermountain REA (CORE).

## Program families

- **Habit**: Xcel CO's default residential TOU (2021–22 rollout); APS's default TOU and its
  demand-charge residential rate (Saver Choice Max — the residential demand charge everyone
  cites); SRP's TOU and its mandatory demand rate for new solar customers (E-27); TEP's TOU; NV
  Energy's TOU; PGE's TOU and Peak Time Rebates; PSE's TOU pilot; Idaho Power's TOU.
- **Dispatch**: Xcel CO's AC Rewards, Peak Partners (BYOT), and Renewable Battery Connect (a
  real residential battery VPP with upfront $/kW + annual payments — capture in detail);
  APS Cool Rewards (thermostat, ~100k) and its residential battery pilot; SRP's Bring Your Own
  Battery; PGE's Smart Battery pilot / Smart Thermostat; PSE Flex; Idaho Power's A/C Cool
  Credit; NV Energy PowerShift; BPA's demand-response programs via PUDs; Portland's "Flex 2.0".
- **Storage incentives**: Colorado's state storage rebate (2024–); Xcel CO Renewable Battery
  Connect upfront; APS/SRP battery incentives; Oregon Solar + Storage Rebate; WA's programs.
- **Export**: this is where the region is hard. AZ ended retail NEM in 2017 (RCP/"export rate"
  stepping down annually; SRP's own separate regime); NV's 2017 restoration with tiers stepping
  down to 75% of retail; NM full NEM; UT's 2017 transition to export credit (RMP); CO full NEM
  with the 2024 Xcel changes; WA/OR/ID/MT net metering with Idaho Power's 2023–24 successor
  ("net billing" at export credit rate — capture the PUC decision). Each is a different regime;
  ten state rows will each be substantial.

## Interconnection

Ten PUCs (and BPA/PUD self-rules). Split as three Opus agents: {WA, OR, ID, MT}, {AZ, NM, NV, UT},
{CO, WY}. AZ (ACC) and NV (PUCN) have the most storage-specific rules; CO has the "Community Solar
Gardens" and the 2023 storage interconnection rewrite.

## Cluster split

- Presence: three Sonnet agents by sub-market (≈60 each).
- Programs: Xcel CO + APS + SRP + PGE (Opus — these four are the region's reference cases and
  the rate structures are complex); the rest in two Sonnet agents (PNW; SW+Mountain).
- Interconnection: three Opus agents.
- Wholesale: one Sonnet agent — mostly documenting absence and EDAM/Markets+ status.

## Hard problem to flag

Arizona (APS/SRP) is the national test case for "TOU plus residential demand charge plus
low export rate" — the exact combination where a battery's self-consumption value dominates and
the arbitrage story is weak. The presence layer will show green in both habit and dispatch;
the *economics* are unlike anywhere else. Worth a dedicated worked example in the app.
