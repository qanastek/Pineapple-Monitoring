#!/bin/bash
#mkdir -f /usr/lib/pineapple	#réaliser le test si existant ou non
cp CollectData.py /usr/lib/pineapple/CollectData.py
cp AutoCheckUser.py /usr/lib/pineapple/AutoCheckUser.py

cp pineapple /usr/bin/pineapple
chmod +x /usr/bin/pineapple