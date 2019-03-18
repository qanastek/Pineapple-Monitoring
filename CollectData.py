# -*- coding: utf-8 -*-

# python -W ignore CollectData.py

# Computer informations
import psutil

# Output Table
from texttable import Texttable

# Library for getting OS name
import os

# Bash command
import subprocess

import json

import sys

# Adresse MAC
from uuid import getnode as get_mac

# OS name (Linux/Mac or Windows)
os = os.uname()[0]

def optionDisplay(cpuUsage,diskUsage,memoryUsage,swapUsage,usersCounter,processCounter,coreCounter,treadsCounter):

	if len(sys.argv) == 2 and sys.argv[1] == "--display":

		table = Texttable()

		table.add_rows(
			[
				['Info', 'Value'],
				['Cpu Load', cpuUsage],
				['Cores', coreCounter],
				['Treads', treadsCounter],
				['Disk Usage', diskUsage],
				['Memory Usage', memoryUsage],
				['Swap Usage', swapUsage],
				['Connected Users', usersCounter],
				['Running Process', processCounter]
			])

		print table.draw()

		sys.exit(0)

def CollectData():

	if os == "Linux":

		# Utilisation processeur
		# Interval => Précision après la virgule
		cpuUsage = psutil.cpu_percent(interval=1)

		# Nombre de coeurs physique
		coreCounter = psutil.cpu_count(logical=False)

		# Nombre de coeurs logiques
		bashCommand  = "cat /proc/cpuinfo | awk '/^processor/{print $3}' | wc -l"
		treadsCounter = subprocess.check_output(['bash','-c', bashCommand])

		diskUsage = psutil.disk_usage('/').percent

		memoryUsage = psutil.virtual_memory().percent

		swapUsage = psutil.swap_memory().percent

		usersCounter = len(psutil.users())

		processCounter = len(psutil.pids())

		macAdd = str(get_mac())

		# If --display show a table
		optionDisplay(cpuUsage,diskUsage,memoryUsage,swapUsage,usersCounter,processCounter,coreCounter,treadsCounter)

		# Else send a JSON response
		data = json.dumps(
		{
			"mac" : macAdd,
			"currentCpuLoad" : cpuUsage,
			"currentDiskUsage" : diskUsage,
			"currentMemLoad" : memoryUsage,
			"currentSwapUsage" : swapUsage,
			"currentConnectedUsers" : usersCounter,
			"processCounter" : processCounter
		}
		, indent=4, sort_keys=True)

		data = json.loads(data) # JSON HERE

		return data

if len(sys.argv) == 2 and sys.argv[1] == "--display":
	CollectData()