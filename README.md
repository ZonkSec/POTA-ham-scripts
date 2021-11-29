# POTA-ham-scripts
these are some ham radio scripts i wrote for POTA purposes. converting logs, checking for various things, etc

they are quick and dirty, room for improvments everywhere, but they help me see if ive reached my goals!

### callsign2usstate.py
this script takes a file path to an ADIF file and then converts all QSO callsigns to state using lookup on hamqth.com. script will need to be updated to use your hamqth.com. credentials. if callsign doesnt exist on hamqth. take the states it outputs and put into a file called "states.txt". I usually keep a running "states.txt" file and update it to add states after doing an activation. if callsign doesnt exist on hamqth, it says not found and i manually look it up (qrz.com seems to be more complete these days, that would be a nice upgrade for this script). 

### usstateCompleteCheck.py
this script takes the "states.txt" file created in the previous step and checks what states have not been contacted. outputs results to screen

### parksTODOgps.py
manually create a file called "parksCompleted.txt" that contains all the parks you have done. (K-XXXX format, each park on its own line). this script takes that file, pulls the latest park listing from POTA for your state (you will have to update this script to be for your state), and then outputs to screen a CSV of parkname|description, lat, and long. This CSV can then be imported to mymaps.google.com to give you a custom map of what parks left to activate!

### potalog2adif.py
takes a session from pota.app, then will parse all hunted park QSOs in your account's log. it then converts those QSOs into ADIF for use in importing into other log programs or for mapping or etc.
