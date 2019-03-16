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

# OS name (Linux/Mac or Windows)
os = os.uname()[0]

def makeRestResult(cpuUsage,diskUsage,memoryUsage,swapUsage,usersCounter,processCounter):

	return json.dumps({ "cpuUsage" : cpuUsage, "diskUsage" : diskUsage, "memoryUsage" : memoryUsage, "swapUsage" : swapUsage, "usersCounter" : usersCounter, "processCounter" : processCounter })

def optionDisplay(cpuUsage,diskUsage,memoryUsage,swapUsage,usersCounter,processCounter):

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

	# If --display show a table
	optionDisplay(cpuUsage,diskUsage,memoryUsage,swapUsage,usersCounter,processCounter)

	# Else send a JSON response
	makeRestResult(cpuUsage,diskUsage,memoryUsage,swapUsage,usersCounter,processCounter)