#!/usr/bin/env python3
"""Build data/processed/lmp_zone_map.csv: default LMP zone per target territory (Rank 1 layer 2).

Territories = data/raw/hifld_over10k.csv eia_id whose docs/data/presence.json "rto" is one of the 7 markets.
Rules are ordered; first match wins. Blank zone = no defensible default (never guess).
method: iso_table (ISO/TO-to-zone table, utility named), name_match (utility/co-op geography or name),
state_default (state-level default only), manual (hand assignment, see notes).
HIFLD state is often HQ state (e.g. Ameren Illinois = MO), so IOUs are matched by name first.
"""
import json, os, re
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = pd.read_csv(os.path.join(ROOT, "data/raw/hifld_over10k.csv"), dtype={"eia_id": str})
P = json.load(open(os.path.join(ROOT, "docs/data/presence.json")))
SUMM = os.path.join(ROOT, "data/processed/lmp_summary.csv")
MKTS = ["PJM", "MISO", "CAISO", "ERCOT", "NYISO", "ISO-NE", "SPP"]

URL = {
    "PJM": "https://www.pjm.com/markets-and-operations/energy",
    "MISO": "https://www.misoenergy.org/markets-and-operations/ (hub/zone definitions; site blocks scripted access)",
    "CAISO": "https://oasis.caiso.com/ (DLAP = default load aggregation point per IOU area)",
    "ERCOT": "https://www.ercot.com/mktinfo/prices",
    "NYISO": "https://mis.nyiso.com/public/ (zones A-K by TO service area)",
    "ISO-NE": "https://www.iso-ne.com/about/key-stats/maps-and-diagrams",
    "SPP": "https://www.spp.org/markets-operations/",
}

# (regex on upper-case hifld_name, zone, method, confidence, note) ; first match wins
R = {
 "PJM": [
  (r"COMMONWEALTH EDISON", "COMED", "iso_table", "high", ""),
  (r"VIRGINIA ELECTRIC", "DOM", "iso_table", "high", ""),
  (r"PUBLIC SERVICE ELEC", "PSEG", "iso_table", "high", ""),
  (r"PECO ENERGY", "PECO", "iso_table", "high", ""),
  (r"OHIO POWER|APPALACHIAN POWER|KINGSPORT POWER|WHEELING POWER", "AEP", "iso_table", "high", "AEP zone"),
  (r"KENTUCKY POWER", "AEP", "iso_table", "high", "AEP zone"),
  (r"PPL ELECTRIC", "PPL", "iso_table", "high", ""),
  (r"BALTIMORE GAS", "BGE", "iso_table", "high", ""),
  (r"JERSEY CENTRAL", "JCPLC", "iso_table", "high", ""),
  (r"OHIO EDISON|CLEVELAND ELECTRIC ILLUM|TOLEDO EDISON|PENNSYLVANIA POWER CO", "ATSI", "iso_table", "high", "FirstEnergy Ohio/Penn Power = ATSI zone"),
  (r"CITY OF CLEVELAND", "ATSI", "name_match", "medium", "Cleveland Public Power inside ATSI footprint"),
  (r"POTOMAC ELECTRIC POWER", "PEPCO", "iso_table", "high", ""),
  (r"DUKE ENERGY OHIO|DUKE ENERGY KENTUCKY", "DEOK", "iso_table", "high", ""),
  (r"WEST PENN POWER|THE POTOMAC EDISON|MONONGAHELA POWER", "APS", "iso_table", "high", "Allegheny Power zone"),
  (r"DUQUESNE LIGHT", "DUQ", "iso_table", "high", ""),
  (r"PENNSYLVANIA ELECTRIC CO|METROPOLITAN EDISON", None, None, None, ""),  # handled below
  (r"ATLANTIC CITY ELECTRIC", "AECO", "iso_table", "high", ""),
  (r"DELMARVA|DELAWARE ELECTRIC COOP|CITY OF DOVER|CITY OF NEWARK \(DE\)", "DPL", "name_match", "medium", "Delaware peninsula = DPL zone"),
  (r"DAYTON POWER", "DAY", "iso_table", "high", ""),
  (r"OWEN ELECTRIC|BLUE GRASS ENERGY|SOUTH KENTUCKY RURAL|JACKSON ENERGY|NOLIN RURAL|SALT RIVER ELECTRIC|TAYLOR COUNTY RURAL|INTER COUNTY ENERGY|CLARK ENERGY|FARMERS RURAL ELECTRIC COOP CORP - \(KY\)|FLEMING-MASON|LICKING VALLEY|SHELBY ENERGY|GRAYSON RURAL|BIG SANDY RURAL|CUMBERLAND VALLEY ELECTRIC", "EKPC", "name_match", "medium", "East Kentucky Power Coop member system"),
  (r"NORTHERN VIRGINIA ELEC|RAPPAHANNOCK|SHENANDOAH VALLEY|SOUTHSIDE ELECTRIC|CENTRAL VIRGINIA ELECTRIC|BARC ELECTRIC|MECKLENBURG ELECTRIC|NORTHERN NECK|A & N ELECTRIC|PRINCE GEORGE ELECTRIC|COMMUNITY ELECTRIC COOP", "DOM", "name_match", "medium", "Virginia co-op inside Dominion zone footprint"),
  (r"CITY OF MANASSAS", "DOM", "name_match", "medium", ""),
  (r"CITY OF NAPERVILLE|CITY OF ST CHARLES|CITY OF BATAVIA|CITY OF GENEVA", "COMED", "name_match", "medium", "Chicago-area municipal inside ComEd zone"),
  (r"NORTHEASTERN RURAL E M C|CITY OF MISHAWAKA", "AEP", "name_match", "low", "NE Indiana inside I&M (AEP zone)"),
 ],
 "CAISO": [
  (r"PACIFIC GAS & ELECTRIC", "DLAP_PGAE-APND", "iso_table", "high", "PG&E DLAP"),
  (r"SOUTHERN CALIFORNIA EDISON", "DLAP_SCE-APND", "iso_table", "high", "SCE DLAP"),
  (r"SAN DIEGO GAS", "DLAP_SDGE-APND", "iso_table", "high", "SDG&E DLAP"),
  (r"CENTRAL COAST COMMUNITY", "DLAP_PGAE-APND", "manual", "medium", "CCA load settles in PG&E area"),
  (r"ANAHEIM|RIVERSIDE|PASADENA|AZUSA|BANNING|COLTON", "DLAP_SCE-APND", "manual", "low", "Municipal inside SCE area; own settlement point/sub-LAP may differ"),
  (r"ALAMEDA|PALO ALTO|SANTA CLARA|LODI|LASSEN|LOMPOC", "DLAP_PGAE-APND", "manual", "low", "Municipal inside PG&E area; own settlement point may differ"),
 ],
 "NYISO": [
  (r"CONSOLIDATED EDISON", "J (N.Y.C.)", "iso_table", "medium", "Westchester is zone I; NYC zone J dominant"),
  (r"LONG ISLAND POWER|FREEPORT|ROCKVILLE CENTRE", "K (LONGIL)", "iso_table", "high", ""),
  (r"NIAGARA MOHAWK", "C (CENTRL)", "iso_table", "low", "Spans A-F; Central dominant"),
  (r"NEW YORK STATE ELEC", "C (CENTRL)", "iso_table", "low", "Spans B-G; Central dominant"),
  (r"ROCHESTER GAS", "B (GENESE)", "iso_table", "high", ""),
  (r"CENTRAL HUDSON|ORANGE & ROCKLAND", "G (HUD VL)", "iso_table", "medium", ""),
  (r"JAMESTOWN", "A (WEST)", "name_match", "high", ""),
  (r"FAIRPORT", "B (GENESE)", "name_match", "high", ""),
  (r"PLATTSBURGH", "D (NORTH)", "name_match", "high", ""),
 ],
 "ISO-NE": [
  (r"NSTAR", ".Z.NEMASSBOST", "iso_table", "low", "Eversource East; also SEMA/Cape area"),
  (r"MASSACHUSETTS ELECTRIC|NARRAGANSETT", None, None, None, ""),
  (r"CONNECTICUT LIGHT|UNITED ILLUMINATING|TOWN OF WALLINGFORD|CITY OF NORWICH|GROTON DEPT", ".Z.CONNECTICUT", "iso_table", "high", ""),
  (r"CENTRAL MAINE POWER|VERSANT", ".Z.MAINE", "iso_table", "high", ""),
  (r"PUBLIC SERVICE CO OF NH|NEW HAMPSHIRE ELEC|UNITIL ENERGY|GRANITE STATE", ".Z.NEWHAMPSHIRE", "iso_table", "high", ""),
  (r"GREEN MOUNTAIN POWER|VERMONT ELECTRIC COOP|BURLINGTON ELECTRIC|WASHINGTON ELECTRIC COOP - \(VT\)", ".Z.VERMONT", "iso_table", "high", ""),
  (r"FITCHBURG", ".Z.WCMASS", "name_match", "medium", ""),
  (r"CITY OF TAUNTON|MIDDLEBOROUGH|NANTUCKET", ".Z.SEMASS", "name_match", "medium", ""),
  (r"CHICOPEE|HOLYOKE|WESTFIELD|SHREWSBURY", ".Z.WCMASS", "name_match", "medium", ""),
  (r"TOWN OF READING|PEABODY|TOWN OF DANVERS|WAKEFIELD|MARBLEHEAD", ".Z.NEMASSBOST", "name_match", "medium", "North Shore / Middlesex; NEMA/Boston zone"),
 ],
 "ERCOT": [
  (r"ONCOR", "LZ_NORTH", "iso_table", "medium", "Oncor spans North and West zones; North dominant"),
  (r"CENTERPOINT", "LZ_HOUSTON", "iso_table", "high", ""),
  (r"AEP TEXAS CENTRAL", "LZ_SOUTH", "iso_table", "high", ""),
  (r"AEP TEXAS NORTH", "LZ_WEST", "iso_table", "medium", ""),
  (r"CITY OF SAN ANTONIO", "LZ_CPS", "iso_table", "high", "CPS Energy"),
  (r"AUSTIN ENERGY", "LZ_AEN", "iso_table", "high", ""),
  (r"CITY OF LUBBOCK", "LZ_WEST", "name_match", "medium", "Lubbock P&L joined ERCOT 2021"),
  (r"DENTON COUNTY ELEC|CITY OF DENTON|CITY OF GARLAND|GRAYSON-COLLIN|COOKE COUNTY|FANNIN COUNTY|WISE ELECTRIC|WEATHERFORD|CITY OF GREENVILLE|TRINITY VALLEY|NAVARRO COUNTY|COMANCHE COUNTY|HAMILTON COUNTY|BARTLETT ELECTRIC|LAMAR COUNTY", "LZ_NORTH", "name_match", "medium", "North/north-central Texas co-op or municipal"),
  (r"BROWNSVILLE|MAGIC VALLEY|NUECES ELECTRIC|SAN PATRICIO|KARNES|RIO GRANDE ELECTRIC", "LZ_SOUTH", "name_match", "medium", "South Texas"),
  (r"SAN BERNARD|NAVASOTA VALLEY|HOUSTON COUNTY ELEC|CHEROKEE COUNTY", None, None, None, ""),
 ],
 "SPP": [
  (r"EVERGY|CITY OF KANSAS CITY - \(KS\)|MIDWEST ENERGY|WHEATLAND|OMAHA PUBLIC|LINCOLN ELECTRIC|NEBRASKA PUBLIC|SOUTHERN PUBLIC POWER|SIOUX VALLEY", "SPPNORTH_HUB", "name_match", "low", "Northern SPP footprint; hub is context, not settlement point"),
  (r"OKLAHOMA GAS|PUBLIC SERVICE CO OF OKLAHOMA|SOUTHWESTERN ELECTRIC POWER|OKLAHOMA ELECTRIC COOP|CITY OF EDMOND|SOUTHWESTERN PUBLIC SERVICE|TRI-COUNTY ELECTRIC COOP, INC \(OK\)", "SPPSOUTH_HUB", "name_match", "low", "Southern SPP footprint; hub is context, not settlement point"),
 ],
 "MISO": [
  (r"AMEREN ILLINOIS", "ILLINOIS.HUB", "iso_table", "medium", "Illinois Hub is in the Ameren Illinois area"),
  (r"ENTERGY ARKANSAS", "ARKANSAS.HUB", "iso_table", "high", ""),
  (r"ENTERGY LOUISIANA|ENTERGY NEW ORLEANS|CLECO", "LOUISIANA.HUB", "iso_table", "medium", ""),
  (r"ENTERGY MISSISSIPPI", "MS.HUB", "iso_table", "high", ""),
  (r"ENTERGY TEXAS", "TEXAS.HUB", "iso_table", "high", ""),
  (r"DTE ELECTRIC|CONSUMERS ENERGY", "MICHIGAN.HUB", "iso_table", "high", ""),
  (r"NORTHERN STATES POWER|OTTER TAIL|ALLETE|CONNEXUS|MONTANA-DAKOTA|MIDAMERICAN|INTERSTATE POWER", "MINN.HUB", "name_match", "medium", "Minnesota Hub is the nearest hub, not a zone price"),
  (r"DUKE ENERGY INDIANA|INDIANAPOLIS POWER|NORTHERN INDIANA PUB|SOUTHERN INDIANA GAS", "INDIANA.HUB", "name_match", "medium", ""),
  (r"INDIANA MICHIGAN POWER", None, None, None, "presence rto=MISO but I&M is PJM (AEP zone); verify rto field"),
  (r"MISSISSIPPI POWER", None, None, None, "Southern Co subsidiary; presence rto=MISO looks wrong; verify"),
  (r"UNION ELECTRIC", None, None, None, "Ameren Missouri (AMMO) no hub; blank"),
 ],
}
STATE_DEFAULT = {
 "ISO-NE": {"CT": ".Z.CONNECTICUT", "ME": ".Z.MAINE", "NH": ".Z.NEWHAMPSHIRE", "VT": ".Z.VERMONT", "RI": ".Z.RHODEISLAND"},
 "SPP": {"KS": "SPPNORTH_HUB", "NE": "SPPNORTH_HUB", "SD": "SPPNORTH_HUB",
         "OK": "SPPSOUTH_HUB", "AR": "SPPSOUTH_HUB", "TX": "SPPSOUTH_HUB", "NM": "SPPSOUTH_HUB", "LA": "SPPSOUTH_HUB"},
 "MISO": {"MI": "MICHIGAN.HUB", "IN": "INDIANA.HUB", "MN": "MINN.HUB", "ND": "MINN.HUB", "SD": "MINN.HUB", "IA": "MINN.HUB",
          "AR": "ARKANSAS.HUB", "LA": "LOUISIANA.HUB", "MS": "MS.HUB", "TX": "TEXAS.HUB", "IL": "ILLINOIS.HUB"},
 "PJM": {"VA": "DOM"},
}
SD_CONF = {"ISO-NE": "medium", "SPP": "low", "MISO": "low", "PJM": "low"}
SD_NOTE = {"ISO-NE": "single-zone state", "SPP": "state default to nearest SPP hub (context only)",
           "MISO": "state default to nearest MISO hub; MISO zonal LMP not in public DA file", "PJM": "Virginia default"}


def main():
    have = set()
    if os.path.exists(SUMM):
        s = pd.read_csv(SUMM)
        have = set(zip(s["market"], s["zone"]))
    rows = []
    for _, r in H.iterrows():
        rto = P[r.eia_id]["rto"]
        if rto not in MKTS:
            continue
        nm = r.hifld_name.upper()
        zone, method, conf, note, hit = "", "", "", "", False
        for pat, z, m, c, n in R.get(rto, []):
            if re.search(pat, nm):
                hit = True
                if z:
                    zone, method, conf, note = z, m, c, n
                else:
                    note = n or "multi-zone or unverified territory; left blank"
                break
        if not hit:
            z = STATE_DEFAULT.get(rto, {}).get(r.hifld_state)
            if z:
                zone, method, conf, note = z, "state_default", SD_CONF[rto], SD_NOTE[rto]
        rows.append(dict(eia_id=r.eia_id, hifld_name=r.hifld_name, hifld_state=r.hifld_state, market=rto,
                         zone=zone, method=method, confidence=conf, source_url=URL[rto] if zone else "",
                         has_price_data=("Yes" if (rto, zone) in have else "No") if zone else "",
                         notes=note))
    out = pd.DataFrame(rows)
    out.to_csv(os.path.join(ROOT, "data/processed/lmp_zone_map.csv"), index=False)
    print(len(out), "territories;", (out.zone != "").sum(), "mapped")
    print(out.groupby("market").apply(lambda g: f"{(g.zone!='').sum()}/{len(g)}").to_dict())


if __name__ == "__main__":
    main()
