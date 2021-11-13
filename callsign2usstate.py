import adif_io
import requests
from xml.etree import ElementTree
import sys
import os
from bs4 import BeautifulSoup

fpath = sys.argv[-1]

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}
abbrev_us_state = dict(map(reversed, us_state_abbrev.items()))

r = requests.get('https://www.hamqth.com/xml.php?u=hamqth_username,e&p=hamqth_pw')
tree = ElementTree.fromstring(r.content)
session = tree[0][0].text
try:
    qsos_raw, adif_header = adif_io.read_from_file(fpath)
except:
    print("send adif file as command line arg")
    exit()

for qso in qsos_raw:
    r = requests.get('https://www.hamqth.com/xml.php?id='+session+'&callsign='+qso["CALL"]+'&prg=callsign2ussate')
    tree = ElementTree.fromstring(r.content)
    notfound = True
    for child in tree[0]:
        if child.tag == "{https://www.hamqth.com}us_state":
            try:
                print(abbrev_us_state[child.text])
                notfound = False
            except:
                continue
    if notfound:
        print(qso["CALL"] + " not found")