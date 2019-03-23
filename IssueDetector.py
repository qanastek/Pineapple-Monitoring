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

from SaveData import *

# For getting ip address
import socket

# Date
import datetime

# --set
SetSettings(sys.argv)

# --param
DisplaySettings(sys.argv)

# JSON en lecture
with open("settings.json", "r") as read_file:

    	data = json.load(read_file)

def GetInfo(JsonIn):

	jsonOut = {
		'mac' : JsonIn['mac'],
		'currentCpuLoad': JsonIn['currentCpuLoad'],
		'currentDiskUsage': JsonIn['currentDiskUsage'],
		'currentSwapUsage' : JsonIn['currentSwapUsage'],
		'currentMemLoad' : JsonIn['currentMemLoad'],
		'currentConnectedUsers' : JsonIn['currentConnectedUsers'],
		"processCounter" : JsonIn['processCounter']
	}

	return jsonOut

def ErrorsToString(errors, ComputerInfos):

	hostname = socket.gethostname()
	string = "Computer Hostname : " + hostname + "\nLocal ip address : " + socket.gethostbyname(hostname) + "\nMAC : " + str(ComputerInfos['mac']) + " \n\n"

	string += "Errors : \n\n"

	for i in errors:

		string += i + " \n"

	return string

def Program(JsonIn):

	ComputerInfos = GetInfo(JsonIn)

	issueCounter = 0
	errors = []

	# CPU Load Check
	if ComputerInfos['currentCpuLoad'] >= data["cpuLoadMax"] :
		issueCounter += 1
		errors.append("cpu overload")

	# Disk Usage Check
	if ComputerInfos['currentDiskUsage'] >= data["diskUsageMax"] :
		issueCounter += 1
		errors.append("disk saturate")

	# Swap Usage Check
	if ComputerInfos['currentSwapUsage'] >= data["swapUsageMax"] :
		issueCounter += 1
		errors.append("swap saturate")

	# Memory Load Check
	if ComputerInfos['currentMemLoad'] >= data["memLoadMax"] :
		issueCounter += 1
		errors.append("memory saturate")

	# Check how much users was connected
	if ComputerInfos['currentConnectedUsers'] >= data["connectedUsersMax"] :
		issueCounter += 1
		errors.append("Too much users was connected")

	if ComputerInfos['processCounter'] >= data["processCounter"] :
		issueCounter += 1
		errors.append("Too much process are running")

	if issueCounter > 0 :
		date = datetime.datetime.now()
		dateFR = str(date.day) + "/" + str(date.month) + "/" + str(date.year) + " à " + str(date.hour) + "H" + str(date.minute)

		SendEmail("A computer have some issues", ErrorsToString(errors, ComputerInfos) + "\nDate : " + dateFR )
		SaveDataAlerts(JsonIn)