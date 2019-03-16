# -*- coding: utf-8 -*-

# For program args
import sys

# For reading JSON
import json

# Output Table
from texttable import Texttable

# Import my functions
from toolbox import *

# Import my own mail sender
from MailSender import *

# For getting ip address
import socket

# --set
SetSettings(sys.argv)

# --param
DisplaySettings(sys.argv)

# JSON en lecture
with open("settings.json", "r") as read_file:

    	data = json.load(read_file)

# Valeurs max enregistrer dans le fichier config
cpuLoadMax = data["cpuLoadMax"]
diskUsageMax = data["diskUsageMax"]
swapUsageMax = data["swapUsageMax"]
memLoadMax = data["memLoadMax"]
connectedUsersMax = data["connectedUsersMax"]

# Valeurs capter et reçu
currentCpuLoad = 1
currentDiskUsage = 73
currentSwapUsage = 0.4
currentMemLoad = 56.7
currentConnectedUsers = 0

issueCounter = 0
errors = []

# CPU Load Check
if currentCpuLoad >= cpuLoadMax :
	issueCounter += 1
	errors.append("cpu overload")

# Disk Usage Check
if currentDiskUsage >= diskUsageMax :
	issueCounter += 1
	errors.append("disk saturate")

# Swap Usage Check
if currentSwapUsage >= swapUsageMax :
	issueCounter += 1
	errors.append("swap saturate")

# Memory Load Check
if currentMemLoad >= memLoadMax :
	issueCounter += 1
	errors.append("memory saturate")

# Check how much users was connected
if currentConnectedUsers >= connectedUsersMax :
	issueCounter += 1
	errors.append("Too much users was connected")

def ErrorsToString(errors):
	hostname = socket.gethostname()
	string = "hostname : " + hostname + "\nLocal ip address : " + socket.gethostbyname(hostname) + " \n\n"

	string += "Errors : \n\n"

	for i in errors:
		string += i + " \n"

	return string

if issueCounter > 0 :
	SendEmail("A computer have issues", ErrorsToString(errors))