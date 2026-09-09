import sys
sys.path.insert(0, "/sessions/wizardly-vibrant-davinci/mnt/utility-map")
from scan_writer import append_rows

LV = "2026-09-09"

rows = [
["3093","CARROLL ELECTRIC COOP CORP - (AR)","Carroll Electric Cooperative Corporation","AR","SPP","Cooperative",
 "No","https://www.carrollecc.com/rates","Unknown","","No","https://www.carrollecc.com/rates","Unknown","",
 "AECC member, NW Arkansas (SPP side); rate schedule is flat/demand-only (Rate 1-4, 14), no TOU; note - do not confuse with unrelated Ohio co-op of same name (cecpower.coop)",LV,"Medium"],

["6342","FIRST ELECTRIC COOP CORP","First Electric Cooperative Corporation","AR","MISO","Cooperative",
 "Unknown","","Unknown","","Unknown","","Unknown","",
 "AECC member, central Arkansas (Jacksonville/Benton/Heber Springs/Perryville/Stuttgart) - MISO side; site (firstelectric.coop) did not return readable content for rates/programs check",LV,"Low"],

["14289","OZARKS ELECTRIC COOP CORP - (AR)","Ozarks Electric Cooperative","AR","SPP","Cooperative",
 "Yes","https://www.ozarksecc.com/service/rates","Unknown","","Unknown","","Unknown","",
 "AECC member, NW Arkansas (SPP side); residential EV Charging Rate is time-differentiated (off-peak 10pm-5am); C&I rate and dispatch programs not confirmed",LV,"High"],

["817","ARKANSAS VALLEY ELEC COOP CORP","Arkansas Valley Electric Cooperative Corporation","AR","SPP","Cooperative",
 "Unknown","","Unknown","","Unknown","","Unknown","",
 "AECC member, west-central Arkansas (Ozark/Waldron/Van Buren) - SPP side; site not checked for rate/program detail",LV,"Low"],

["13676","NORTH ARKANSAS ELEC COOP, INC","North Arkansas Electric Cooperative","AR","MISO","Cooperative",
 "Unknown","","Yes","https://www.naeci.com/load-management","Unknown","","Unknown","",
 "AECC member, north-central AR (Salem/Ash Flat/Mountain Home); RTO side genuinely ambiguous near MISO/SPP seam, treated as MISO (eastern two-thirds) with low confidence; confirmed residential AC/water-heater radio-switch load management program on own site",LV,"Medium"],

["4509","CRAIGHEAD ELECTRIC COOP CORP","Craighead Electric Cooperative Corporation","AR","MISO","Cooperative",
 "Unknown","","Unknown","","Unknown","","Unknown","",
 "AECC member, Jonesboro/NE Arkansas - MISO side; site not checked for rate/program detail",LV,"Low"],

["17671","SOUTHWEST ARKANSAS E C C","Southwest Arkansas Electric Cooperative","AR","SPP","Cooperative",
 "Unknown","","Yes","https://swrea.com/about-us","Unknown","","Unknown","",
 "AECC member, Texarkana/SW Arkansas - SPP side; cooperative's own service rules reference a load management program members must participate in",LV,"Medium"],

["2678","C & L ELECTRIC COOP CORP","C&L Electric Cooperative Corporation","AR","MISO","Cooperative",
 "Unknown","","Unknown","","Unknown","","Yes","https://www.clelectric.com/",
 "AECC member, Star City/SE Arkansas - MISO side; site references an Irrigation Rate Selection/Load Control Program (agricultural/C&I load control); residential dispatch and TOU rates not confirmed",LV,"Medium"],

["14864","PETIT JEAN ELECTRIC COOP CORP","Petit Jean Electric Cooperative","AR","SPP","Cooperative",
 "Unknown","","Yes","https://www.pjecc.com/","Unknown","","Unknown","",
 "AECC member, Clinton/Marshall AR; confirmed on SPP side of RTO seam; own site lists load management among member services, though program mechanics not detailed",LV,"Medium"],

["20963","WOODRUFF ELECTRIC COOP CORP","Woodruff Electric Cooperative","AR","MISO","Cooperative",
 "Unknown","","Yes","https://www.woodruffelectric.coop/member-services/payment-billing/","Unknown","","Unknown","",
 "AECC member, Forrest City/E Arkansas - MISO side; own site lists a Load Control Program among member services",LV,"Medium"],

["3712","CLAY COUNTY ELECTRIC COOP CORP","Clay County Electric Cooperative","AR","MISO","Cooperative",
 "Unknown","","Unknown","","Unknown","","Unknown","",
 "AECC member, Corning/NE Arkansas - MISO side; site not checked for rate/program detail",LV,"Low"],

["17540","SOUTH CENTRAL ARK EL COOP, INC","South Central Arkansas Electric Cooperative","AR","MISO","Cooperative",
 "Unknown","","Unknown","","Unknown","","Unknown","",
 "AECC member, Arkadelphia area; RTO side ambiguous (near MISO/SPP seam), tentatively MISO; site not checked for rate/program detail",LV,"Low"],
]

append_rows(rows)
print(f"appended {len(rows)} rows")
