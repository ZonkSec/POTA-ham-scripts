import requests
import json
import math
from datetime import datetime

pota_key = "session from pota.app"



def getHuntedQSOs():
    print()
    print("**PROCESSING HUNTED QSOs**")
    headers = {'authorization': pota_key}
    r = requests.get('https://api.pota.app/user/logbook?hunterOnly=1&page=1&size=100',headers=headers)
    if r.status_code == 403:
        print("POTA auth is expired")
        exit()
    jsonParks = json.loads(r.text)
    #print(json.dumps(jsonParks, indent=4, sort_keys=True))

    totalQSOs = jsonParks["count"]
    pages = math.ceil(totalQSOs / 100)
    print("[+] totalHuntedQSOs: " + str(totalQSOs))

    all_entries = []

    page_count = 1
    while page_count < pages+1:
        headers = {'authorization': pota_key}
        r = requests.get('https://api.pota.app/user/logbook?hunterOnly=1&page='+str(page_count)+'&size=100',headers=headers)
        jsonParks = json.loads(r.text)

        entries = jsonParks["entries"]
        for entry in entries:
            all_entries.append(entry)
        page_count = page_count + 1

    return all_entries
    
blah = getHuntedQSOs()

headers = {'authorization': pota_key}
for entry in blah:
    d = datetime.strptime(entry["qsoDateTime"],"%Y-%m-%dT%H:%M:%S")
    date = d.strftime("%Y%m%d")
    time = d.strftime("%H%M")
    
    r = requests.get('https://api.pota.app/park/'+entry["reference"],headers=headers)
    jsonParksRef = json.loads(r.text)
    grid4 = jsonParksRef["grid4"]
    print("<QSO_DATE:8>"+date+" <TIME_ON:4>"+time+" <TIME_OFF:4>"+time+" <CALL:"+str(len(entry["station_callsign"]))+">"+entry["station_callsign"]+" <BAND:3>"+entry["band"]+ " <MODE:3>SSB <MY_GRIDSQUARE:4>EN11 <OPERATOR:6>KE0MME <STATION_CALLSIGN:6>KE0MME <GRIDSQUARE:4>"+grid4+"<EOR>")