#!/bin/bash 
apt get-install python
apt get-install pip
pip install -r requirements.txt

mkdir /usr/lib/pineapple	#réaliser le test si existant ou non
cp CollectData.py usr/lib/pineapple/CollectData.py
cp AutoCheckUser.py /usr/lib/pineapple/AutoCheckUser.py

cp pineapple /usr/bin/pineapple
chmod -x /usr/bin/pineapple
 
#TODO add pineapple to crontab
#créer un alias doc.ubuntu-fr.org/alias
