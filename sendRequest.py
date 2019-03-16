# -*- coding: utf-8 -*-

import requests, os

data = os.system('python CollectData.py')
r = requests.post("http://127.0.0.1:5000/", data = data)