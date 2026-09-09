import sys
sys.path.insert(0, "/sessions/wizardly-vibrant-davinci/mnt/utility-map")
from scan_writer import append_rows

LV = "2026-09-09"
POWERFLEX = "https://energyright.com/business-industry/demand-response/powerflex/"
THERM_LIST = "https://www.thermostatrewards.com/tvalpc/faq/"
NO_HABIT_NOTE = "TVA distributor — flat/seasonal residential rate, no TOU/CPP/EV-TOU found; see TVA EnergyRight programs"

rows = [
["6641","4-COUNTY ELECTRIC POWER ASSN","4-County Electric Power Association","MS","TVA","Cooperative",
 "No","","No",THERM_LIST,"Unknown","","Yes",POWERFLEX,
 "TVA distributor; not on TVA Smart Thermostat Rewards LPC list; enrolled in TVA PowerFlex C&I demand response",LV,"Medium"],

["19007","TOMBIGBEE ELECTRIC POWER ASSN","Tombigbee Electric Power Association","MS","TVA","Cooperative",
 "No","","No",THERM_LIST,"Unknown","","Yes",POWERFLEX,
 "TVA distributor; not on TVA Smart Thermostat Rewards LPC list; enrolled in TVA PowerFlex",LV,"Medium"],

["2849","CENTRAL ELECTRIC POWER ASSN - (MS)","Central Electric Power Association","MS","TVA","Cooperative",
 "No","","Yes",THERM_LIST,"Unknown","","Yes",POWERFLEX,
 "TVA distributor (confirmed via TVA LPC page, not Cooperative Energy despite similar-sounding name); on Smart Thermostat Rewards + PowerFlex",LV,"High"],

["13735","NORTHCENTRAL MISSISSIPPI E P A","Northcentral Electric Cooperative (Northcentral EPA)","MS","TVA","Cooperative",
 "No","","Yes",THERM_LIST,"Unknown","","Yes",POWERFLEX,
 "TVA distributor; on Smart Thermostat Rewards + PowerFlex LPC lists",LV,"High"],

["40302","NORTH EAST MISSISSIPPI EPA","North East Mississippi Electric Power Association","MS","TVA","Cooperative",
 "No","","No",THERM_LIST,"Unknown","","Yes",POWERFLEX,
 "TVA distributor; not on Smart Thermostat Rewards LPC list; enrolled in PowerFlex",LV,"Medium"],

["18447","TALLAHATCHIE VALLEY E P A","Tallahatchie Valley Electric Power Association","MS","TVA","Cooperative",
 "No","","Yes",THERM_LIST,"Unknown","","Yes",POWERFLEX,
 "TVA distributor; on Smart Thermostat Rewards + PowerFlex LPC lists",LV,"High"],

["15211","PONTOTOC ELECTRIC POWER ASSN","Pontotoc Electric Power Association","MS","TVA","Cooperative",
 "No","","No",THERM_LIST,"Unknown","","Yes",POWERFLEX,
 "TVA distributor; not on Smart Thermostat Rewards LPC list; enrolled in PowerFlex",LV,"Medium"],

["276","ALCORN COUNTY ELEC POWER ASSN","Alcorn County Electric Power Association","MS","TVA","Cooperative",
 "No","","Yes",THERM_LIST,"Unknown","","Yes",POWERFLEX,
 "TVA distributor; on Smart Thermostat Rewards + PowerFlex LPC lists",LV,"High"],

["13227","NATCHEZ TRACE ELEC POWER ASSN","Natchez Trace Electric Power Association","MS","TVA","Cooperative",
 "No","","No",THERM_LIST,"Unknown","","Yes",POWERFLEX,
 "TVA distributor; not on Smart Thermostat Rewards LPC list; enrolled in PowerFlex",LV,"Medium"],

["18943","TIPPAH ELECTRIC POWER ASSN","Tippah Electric Power Association","MS","TVA","Cooperative",
 "No","","No",THERM_LIST,"Unknown","","Yes",POWERFLEX,
 "TVA distributor; not on Smart Thermostat Rewards LPC list; enrolled in PowerFlex",LV,"Medium"],

["19273","CITY OF TUPELO - (MS)","Tupelo Water & Light Department","MS","TVA","Municipal",
 "No","","No",THERM_LIST,"Unknown","","Yes",POWERFLEX,
 "TVA distributor; not on Smart Thermostat Rewards LPC list; enrolled in PowerFlex",LV,"Medium"],

["18006","CITY OF STARKVILLE","Starkville Electric Department (Starkville Utilities)","MS","TVA","Municipal",
 "No","","No",THERM_LIST,"Unknown","","Yes",POWERFLEX,
 "TVA distributor; not on Smart Thermostat Rewards LPC list; enrolled in PowerFlex",LV,"Medium"],

["15334","PRENTISS COUNTY ELEC PWR ASSN","Prentiss County Electric Power Association","MS","TVA","Cooperative",
 "No","","No",THERM_LIST,"Unknown","","Yes",POWERFLEX,
 "TVA distributor; not on Smart Thermostat Rewards LPC list; enrolled in PowerFlex",LV,"Medium"],

["18951","TISHOMINGO COUNTY E P A","Tishomingo County Electric Power Association","MS","TVA","Cooperative",
 "No","","Yes",THERM_LIST,"Unknown","","Yes",POWERFLEX,
 "TVA distributor; on Smart Thermostat Rewards + PowerFlex LPC lists",LV,"High"],

["5578","EAST MISSISSIPPI ELEC PWR ASSN","East Mississippi Electric Power Association","MS","TVA","Cooperative",
 "No","","No",THERM_LIST,"Unknown","","Yes",POWERFLEX,
 "TVA distributor; not on Smart Thermostat Rewards LPC list; enrolled in PowerFlex",LV,"Medium"],

["4068","CITY OF COLUMBUS - (MS)","Columbus Light and Water Department","MS","TVA","Municipal",
 "No","","Yes",THERM_LIST,"Unknown","","Yes",POWERFLEX,
 "TVA distributor; on Smart Thermostat Rewards + PowerFlex LPC lists",LV,"High"],

["8748","CITY OF HOLLY SPRINGS","Holly Springs Utility Department","MS","TVA","Municipal",
 "No","","No",THERM_LIST,"Unknown","","Yes",POWERFLEX,
 "TVA distributor; not on Smart Thermostat Rewards LPC list; enrolled in PowerFlex",LV,"Medium"],

["13412","CITY OF NEW ALBANY - (MS)","New Albany Light, Gas & Water","MS","TVA","Municipal",
 "No","","Yes",THERM_LIST,"Unknown","","Yes",POWERFLEX,
 "TVA distributor; on Smart Thermostat Rewards + PowerFlex LPC lists",LV,"High"],

["14275","CITY OF OXFORD - (MS)","Oxford Utilities","MS","TVA","Municipal",
 "No","","No",THERM_LIST,"Unknown","","Yes",POWERFLEX,
 "TVA distributor; not on Smart Thermostat Rewards LPC list; enrolled in PowerFlex (as Oxford Utilities)",LV,"Medium"],

["40303","MONROE COUNTY ELEC POWER ASSN","Monroe County Electric Power Association","MS","TVA","Cooperative",
 "No","","No",THERM_LIST,"Unknown","","Yes",POWERFLEX,
 "TVA distributor; not on Smart Thermostat Rewards LPC list; enrolled in PowerFlex",LV,"Medium"],
]

append_rows(rows)
print(f"appended {len(rows)} rows")
