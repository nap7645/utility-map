import sys
sys.path.insert(0, "/sessions/wizardly-vibrant-davinci/mnt/utility-map")
from scan_writer import append_rows

LV = "2026-09-09"

rows = [
["3841","COAST ELECTRIC POWER ASSN","Coast Electric Power Association","MS","MISO","Cooperative",
 "Yes","https://coastelectric.coop/my-home/time-of-use-rates/","Unknown","","Yes","https://coastelectric.coop/my-business/business-time-of-use-rates/","Unknown","",
 "Cooperative Energy (MISO South) member; residential + business TOU rates confirmed; no dispatch program confirmed on site",LV,"High"],

["17252","SINGING RIVER ELEC COOPERATIVE","Singing River Electric Cooperative","MS","MISO","Cooperative",
 "No","https://singingriver.com/my-home/","Unknown","","Unknown","","Unknown","",
 "Cooperative Energy (MISO South) member; only flat RS-23 residential rate listed, no TOU; business rate page not checked; Comfort Advantage is efficiency-only, not dispatch",LV,"Medium"],

["17647","SOUTHERN PINE ELECTRIC COOPERATIVE","Southern Pine Electric","MS","MISO","Cooperative",
 "Yes","https://southernpine.coop/documents/residential-community-and-general-farm-servicetime-of-userate-schedule-a-tou-billing-code-108/","Unknown","","Unknown","","Unknown","",
 "Cooperative Energy (MISO South) member; residential Schedule A-TOU confirmed; C&I rate and dispatch programs not checked",LV,"High"],

["14563","PEARL RIVER VALLEY EL PWR ASSN","Pearl River Valley Electric Power Association","MS","MISO","Cooperative",
 "No","https://help.prvepa.com/article/33-rates-for-services","Unknown","","No","https://help.prvepa.com/article/33-rates-for-services","Unknown","",
 "Cooperative Energy (MISO South) member; only flat General/Large General/Large Power/Extra Large Power/Bulk Power schedules listed, no TOU found; dispatch programs not checked",LV,"Medium"],

["5175","DIXIE ELECTRIC POWER ASSN","Dixie Electric Power Association","MS","MISO","Cooperative",
 "No","https://www.dixieepa.com/your-account/rates-fees/","Unknown","","Unknown","","Unknown","",
 "Cooperative Energy (MISO South) member; standard flat rate schedule (R-15 residential), no TOU found; C&I rate and dispatch not checked",LV,"Medium"],

["11519","MAGNOLIA ELECTRIC POWER ASSN","Magnolia Electric Power Association","MS","MISO","Cooperative",
 "Unknown","","Unknown","","Unknown","","Unknown","",
 "Cooperative Energy (MISO South) member; site (mepcoop.com) not directly reviewed for rate/program detail",LV,"Low"],

["22815","DELTA ELECTRIC POWER ASSN","Delta Electric Power Association","MS","MISO","Cooperative",
 "Unknown","","Unknown","","Unknown","","Unknown","",
 "Cooperative Energy (MISO South) member; site (deltaepa.com) not directly reviewed for rate/program detail",LV,"Low"],

["17683","SOUTHWEST MISSISSIPPI E P A","Southwest Mississippi Electric Power Association","MS","MISO","Cooperative",
 "No","https://southwestelectric.coop/residential-rates/","Unknown","","Unknown","","Unknown","",
 "Cooperative Energy (MISO South) member; only flat Rate 1/13/101/113/201/213 residential schedules, no TOU found; C&I rate and dispatch not checked",LV,"Medium"],

["18961","TWIN COUNTY ELECTRIC PWR ASSN","Twin County Electric Power Association","MS","MISO","Cooperative",
 "No","https://www.twincoepa.com/member-services/basic-rates-fees/","Unknown","","No","https://www.twincoepa.com/member-services/basic-rates-fees/","Unknown","",
 "Cooperative Energy (MISO South) member; only flat per-kWh residential rates listed, no TOU or dispatch program found",LV,"Medium"],

["21114","YAZOO VALLEY ELEC POWER ASSN","Yazoo Valley Electric Power Association","MS","MISO","Cooperative",
 "Yes","https://www.yazoovalley.com/index.php/your-bill/","Unknown","","Unknown","","Unknown","",
 "Cooperative Energy (MISO South) member; residential 'Smart Saver' plan requires usage cuts on flagged peak days (peak-time-rebate style); C&I rate and dispatch not checked",LV,"Medium"],
]

append_rows(rows)
print(f"appended {len(rows)} rows")
