# -*- coding: utf-8 -*-

# python -W ignore AutoCheckUser.py

from CollectData import *
import requests, json

URL = 'http://127.0.0.1:5000/api'
data = CollectData()
data = json.dumps(data, indent=4, sort_keys=True)

Header = {'Content-type': 'application/json', 'Accept': 'text/plain'}

resultPOST = requests.post(URL, data=data, headers=Header)

print ("---| POST Code : " + str(resultPOST.status_code) + " |---")