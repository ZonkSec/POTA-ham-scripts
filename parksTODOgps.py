import requests
import json


f = open("..\\parksCompleted.txt", "r")
completedParks = f.read().splitlines()

r = requests.get('https://api.pota.us/locations/US-NE')
jsonParks = json.loads(r.text)
allParks = []
parknamelookup = {}

for park in jsonParks["parks"]:
    allParks.append(park["reference"])
    parknamelookup[str(park["reference"])] = str(park["name"])
        
TODOparks = [i for i in allParks + completedParks if i not in allParks or i not in completedParks]

print("All Parks in NE: " + str(len(allParks)))
print("Completed Parks: "+ str(len(completedParks)))
print("Parks left TODO: "+ str(len(TODOparks)))
print()
print("TODO park's GPS coordinates:")
print("park name,latitude,longitude")
for park in TODOparks:
    r = requests.get('https://api.pota.us/park/'+str(park))
    jsonPark = json.loads(r.text)
    if jsonPark[0]["latitude"] == None:
        print("ERROR: "+ str(jsonPark[0]["reference"]))
    else:
        print(str(park)+" | "+ str(parknamelookup[str(park)])  + "," + str(jsonPark[0]["latitude"])+","+str(jsonPark[0]["longitude"]))