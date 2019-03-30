# -*- coding: utf-8 -*-

# python -W ignore CollectData.py

# Computer informations
import psutil

# Output Table
from texttable import Texttable

# Library for getting OS name
import platform

# Bash command
import subprocess

import json

import sys

# Adresse MAC
from uuid import getnode as get_mac

import cpuinfo

import socket

# OS name (Linux/Mac or Windows)
os = platform.system()

def optionDisplay(cpuUsage,diskUsage,memoryUsage,swapUsage,usersCounter,processCounter,coreCounter,treadsCounter,sysExp):

	if len(sys.argv) == 2 and sys.argv[1] == "--display":

		table = Texttable()

		table.add_rows(
			[
				['Info', 'Value'],
				['OS', sysExp],
				['Cpu Load', cpuUsage],
				['Cores', coreCounter],
				['Treads', treadsCounter],
				['Disk Usage', diskUsage],
				['Memory Usage', memoryUsage],
				['Swap Usage', swapUsage],
				['Connected Users', usersCounter],
				['Running Process', processCounter]
			])

		print (table.draw())

		sys.exit(0)

def CollectData():

	# Windows
	if os.lower() == "windows":

		# Operating system
		sysExp = os.lower()

		hostName = socket.gethostname()

		# Utilisation processeur
		# Interval => Précision après la virgule
		cpuUsage = psutil.cpu_percent(interval=1)

		# Nombre de coeurs physique
		coreCounter = psutil.cpu_count(logical=False)

		# Nombre de coeurs logiques
		treadsCounter = psutil.cpu_count(logical=True)

		diskUsage = psutil.disk_usage('/').percent

		disk = psutil.disk_usage('/').total

		memoryUsage = psutil.virtual_memory().percent

		ram = psutil.virtual_memory().total

		swapUsage = psutil.swap_memory().percent

		usersCounter = len(psutil.users())

		processCounter = len(psutil.pids())

		macAdd = str(get_mac())

		cpuModel = cpuinfo.get_cpu_info()['brand']

		# If --display show a table
		optionDisplay(cpuUsage,diskUsage,memoryUsage,swapUsage,usersCounter,processCounter,coreCounter,treadsCounter,sysExp)

		# Else send a JSON response
		data = json.dumps(
		{
			"mac" : str(macAdd),
			"currentCpuLoad" : int(cpuUsage),
			"currentDiskUsage" : int(diskUsage),
			"currentMemLoad" : int(memoryUsage),
			"currentSwapUsage" : int(swapUsage),
			"currentConnectedUsers" : int(usersCounter),
			"processCounter" : int(processCounter),
			"sysExp" : str(sysExp),
			"coreCounter" : int(coreCounter),
			"treadsCounter" : int(treadsCounter),
			"cpuModel" : str(cpuModel),
			"hostName" : str(hostName),
			"ram" : int(ram),
			"disk" : int(disk)
		}
		, indent=4, sort_keys=True)

		data = json.loads(data) # JSON HERE

		return data

	# Linux or Mac
	if os.lower() == "linux" or os.lower() == "darwin":

		# Operating system
		sysExp = os.lower()

		hostName = socket.gethostname()

		# Utilisation processeur
		# Interval => Précision après la virgule
		cpuUsage = psutil.cpu_percent(interval=1)

		# Nombre de coeurs physique
		coreCounter = psutil.cpu_count(logical=False)

		# Nombre de coeurs logiques
		bashCommand  = "cat /proc/cpuinfo | awk '/^processor/{print $3}' | wc -l"
		treadsCounter = subprocess.check_output(['bash','-c', bashCommand])

		diskUsage = psutil.disk_usage('/').percent

		disk = psutil.disk_usage('/').total

		memoryUsage = psutil.virtual_memory().percent

		ram = psutil.virtual_memory().total

		swapUsage = psutil.swap_memory().percent

		bashCommand  = "who | sort --key=1,1 --unique | wc --lines"
		usersCounter = subprocess.check_output(['bash','-c', bashCommand])

		processCounter = len(psutil.pids())

		macAdd = str(get_mac())

		cpuModel = cpuinfo.get_cpu_info()['brand']

		# If --display show a table
		optionDisplay(cpuUsage,diskUsage,memoryUsage,swapUsage,usersCounter,processCounter,coreCounter,treadsCounter,sysExp)

		# Else send a JSON response
		data = json.dumps(
		{
			"mac" : str(macAdd),
			"currentCpuLoad" : int(cpuUsage),
			"currentDiskUsage" : int(diskUsage),
			"currentMemLoad" : int(memoryUsage),
			"currentSwapUsage" : int(swapUsage),
			"currentConnectedUsers" : int(usersCounter),
			"processCounter" : int(processCounter),
			"sysExp" : str(sysExp),
			"coreCounter" : int(coreCounter),
			"treadsCounter" : int(treadsCounter),
			"cpuModel" : str(cpuModel),
			"hostName" : str(hostName),
			"ram" : int(ram),
			"disk" : int(disk)
		}
		, indent=4, sort_keys=True)

		data = json.loads(data) # JSON HERE

		return data

if len(sys.argv) == 2 and sys.argv[1] == "--display":

	CollectData()