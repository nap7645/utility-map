import sys
sys.path.insert(0, "/sessions/wizardly-vibrant-davinci/mnt/utility-map")
from scan_writer import append_rows

LV = "2026-09-09"

rows = [
# Louisiana cooperatives
["17684","SOUTHWEST LOUISIANA E M C","Southwest Louisiana Electric Membership Corporation","LA","MISO","Cooperative",
 "Unknown","","Unknown","","Unknown","","Unknown","",
 "MISO South territory (SW Louisiana, Lake Charles/Jennings area); site not checked for rate/program detail within scan budget",LV,"Low"],

["21567","WASHINGTON-ST TAMMANY E C, INC","Washington-St Tammany Electric Cooperative","LA","MISO","Cooperative",
 "Unknown","","Unknown","","Unknown","","Unknown","",
 "MISO South territory (SE Louisiana); site not checked for rate/program detail within scan budget",LV,"Low"],

["1458","BEAUREGARD ELECTRIC COOP, INC","Beauregard Electric Cooperative","LA","MISO","Cooperative",
 "Unknown","","Unknown","","Unknown","","Unknown","",
 "MISO South territory (DeRidder, SW Louisiana); site not checked for rate/program detail within scan budget",LV,"Low"],

["3641","CLAIBORNE ELECTRIC COOP, INC","Claiborne Electric Cooperative","LA","SPP","Cooperative",
 "Unknown","","Unknown","","Unknown","","Unknown","",
 "Far northwest Louisiana (Homer, near AR/TX border) - tentatively SPP per regional pattern of NW Louisiana co-ops; site not checked for rate/program detail within scan budget",LV,"Low"],

["17565","SOUTH LOUISIANA ELEC COOP ASSN","South Louisiana Electric Cooperative Association (SLECA)","LA","MISO","Cooperative",
 "Unknown","","Unknown","","Unknown","","Unknown","",
 "MISO South territory (Houma/Thibodaux area, SE Louisiana); site (sleca.com) did not return readable content within scan budget",LV,"Low"],

["13783","NORTHEAST LOUISIANA POWER COOP INC.","Northeast Louisiana Power Cooperative","LA","MISO","Cooperative",
 "Unknown","","Unknown","","Unknown","","Unknown","",
 "MISO South territory (Monroe area, NE Louisiana); site not checked for rate/program detail within scan budget",LV,"Low"],

["4153","CONCORDIA ELECTRIC COOP, INC","Concordia Electric Cooperative","LA","MISO","Cooperative",
 "Unknown","","Unknown","","Unknown","","Unknown","",
 "MISO South territory (Ferriday, east-central Louisiana); site not checked for rate/program detail within scan budget",LV,"Low"],

["15175","POINTE COUPEE ELEC MEMBER CORP","Pointe Coupee Electric Membership Corporation","LA","MISO","Cooperative",
 "Unknown","","Unknown","","Unknown","","Unknown","",
 "MISO South territory (New Roads, central Louisiana); site not checked for rate/program detail within scan budget",LV,"Low"],

["9682","JEFFERSON DAVIS ELEC COOP, INC","Jefferson Davis Electric Cooperative","LA","MISO","Cooperative",
 "Unknown","","Unknown","","Unknown","","Unknown","",
 "MISO South territory (Jennings, SW Louisiana); site not checked for rate/program detail within scan budget",LV,"Low"],

# Louisiana municipals
["9096","CITY OF LAFAYETTE - (LA)","Lafayette Utilities System (LUS)","LA","MISO","Municipal",
 "No","https://lus.org/rates/electric-rates/","Unknown","","No","https://lus.org/rates/electric-rates/","Unknown","",
 "LUS confirmed MISO member since 2013 (own site); electric rate schedules are flat (in-city/non-city residential, small/large commercial, schools/churches) with fuel-adjustment and net-metering riders only, no TOU/CPP found; no dispatch/DR program found in site navigation",LV,"High"],

["298","CITY OF ALEXANDRIA - (LA)","Alexandria Municipal Utilities / LEPA","LA","MISO","Municipal",
 "Unknown","","Unknown","","Unknown","","Unknown","",
 "Louisiana municipal, MISO South territory via Louisiana Energy and Power Authority (LEPA); site not checked for rate/program detail within scan budget",LV,"Low"],

["8884","TERREBONNE PARISH CONSOL GOV'T","Terrebonne Parish Consolidated Government - Electric Dept","LA","MISO","Municipal",
 "Unknown","","Unknown","","Unknown","","Unknown","",
 "Louisiana municipal (Houma), MISO South territory; site not checked for rate/program detail within scan budget",LV,"Low"],

["16463","CITY OF RUSTON - (LA)","Ruston Utilities / LEPA","LA","MISO","Municipal",
 "Unknown","","Unknown","","Unknown","","Unknown","",
 "Louisiana municipal (Ruston, N Louisiana), MISO South territory via LEPA; site not checked for rate/program detail within scan budget",LV,"Low"],

# Arkansas municipals
["13718","CITY OF NORTH LITTLE ROCK - (AR)","North Little Rock Electric Department","AR","MISO","Municipal",
 "Unknown","","Unknown","","Unknown","","Unknown","",
 "Central Arkansas municipal, MISO territory; site not checked for rate/program detail within scan budget",LV,"Low"],

["9879","CITY WATER AND LIGHT PLANT","City Water & Light (Jonesboro)","AR","MISO","Municipal",
 "Unknown","","Unknown","","Unknown","","Unknown","",
 "Jonesboro, NE Arkansas municipal, MISO territory; site not checked for rate/program detail within scan budget",LV,"Low"],

["4280","CONWAY CORPORATION","Conway Corporation","AR","MISO","Municipal",
 "Unknown","","Unknown","","Unknown","","Unknown","",
 "Central Arkansas municipal, MISO territory; electric-rates page (conwaycorp.com) did not return readable content within scan budget",LV,"Low"],

["1586","CITY OF BENTONVILLE - (AR)","Bentonville Municipal Utilities","AR","SPP","Municipal",
 "Unknown","","Unknown","","Unknown","","Unknown","",
 "NW Arkansas municipal, SPP territory; site not checked for rate/program detail within scan budget",LV,"Low"],

["1581","CITY OF BENTON - (AR)","City of Benton Utilities","AR","MISO","Municipal",
 "Unknown","","Unknown","","Unknown","","Unknown","",
 "Central Arkansas municipal, MISO territory; site not checked for rate/program detail within scan budget",LV,"Low"],

["14446","PARAGOULD LIGHT & WATER COMM","Paragould Light, Water & Cable","AR","MISO","Municipal",
 "Unknown","","Unknown","","Unknown","","Unknown","",
 "NE Arkansas municipal, MISO territory; site not checked for rate/program detail within scan budget",LV,"Low"],

["20382","CITY OF WEST MEMPHIS - (AR)","West Memphis Utility Commission","AR","MISO","Municipal",
 "Unknown","","Unknown","","Unknown","","Unknown","",
 "East Arkansas municipal, MISO territory; site not checked for rate/program detail within scan budget",LV,"Low"],
]

append_rows(rows)
print(f"appended {len(rows)} rows")
