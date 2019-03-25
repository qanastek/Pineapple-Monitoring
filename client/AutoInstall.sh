#!/bin/bash 
apt install python &&
apt install python-pip &&
pip install -r requirements.txt &&

mkdir /usr/lib/pineapple	#réaliser le test si existant ou non
chmod 777 /usr/lib/pineapple
cp CollectData.py /usr/lib/pineapple/CollectData.py &&
cp AutoCheckUser.py /usr/lib/pineapple/AutoCheckUser.py &&
touch /usr/lib/pineapple/POSTcode.txt
chmod 755 /usr/lib/pineapple/POSTcode.txt &&
cp pineapple /usr/bin/pineapple &&
chmod +x /usr/bin/pineapple &&

crontab crontab.txt
 
#TODO add pineapple to crontab
#créer un alias doc.ubuntu-fr.org/alias
