# -*- coding: utf-8 -*-

# Computer informations
import psutil

# Output Table
from texttable import Texttable

# Library for getting OS name
import os

# Bash command
import subprocess

# OS name (Linux/Mac or Windows)
os = os.uname()[0]

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

# Print part
table = Texttable()
table.add_rows(
	[
		['Info', 'Value'],
		['Cpu Usage', cpuUsage],
		['Cores', coreCounter],
		['Treads', treadsCounter],
		['Disk Usage', diskUsage],
		['Memory Usage', memoryUsage],
		['Swap Usage', swapUsage],
		['Connected Users', usersCounter],
		['Running Process', processCounter]
	])
print table.draw()