# -*- coding: utf-8 -*-

import json

from texttable import Texttable

import sys

yesList = ["y", "yes", "yeap", "oui", "o"]
noList = ["n", "no", "nope", "non"]

def DisplaySettings(argv):
	
	if len(argv) == 2 and argv[1] == "--param":

		# JSON en lecture
		with open("settings.json", "r") as read_file:

			data = json.load(read_file)

		table = Texttable()
		table.add_rows(
			[
				['Parameters', 'Max Value'],
				['Max cpu load', str(data["cpuLoadMax"]) + " %"],
				['Max disk usage', str(data["diskUsageMax"]) + " %"],
				['Max swap usage', str(data["swapUsageMax"]) + " %"],
				['Max memory load', str(data["memLoadMax"]) + " %"],
				['Max connected users', str(data["connectedUsersMax"])]
			])
		print(table.draw())

		sys.exit() # Sort du programme

def SetSettings(argv):

	# Changer les paramètres
	if len(argv) == 2 and argv[1] == "--set":

		# Open the file in Read mode
		bufferData = open("settings.json", "r")
		bufferisedData = json.load(bufferData)

		# Open the file in Write mode
		data = open("settings.json", "w")

		# Nombre maximum d'utilisateur en ligne
		champValidation = str(raw_input("Voulez vous modifié le nombre max d'utilisateur connecté ? "))

		if champValidation.lower() in yesList:

			champValue = input("Quelle valeur voulez-vous assigné : ")

			bufferisedData['connectedUsersMax'] = champValue

		# Charge maximum du CPU
		champValidation = str(raw_input("Voulez vous modifié la charge maximum du CPU ? "))

		if champValidation.lower() in yesList:

			champValue = input("Quelle valeur voulez-vous assigné : ")

			bufferisedData['cpuLoadMax'] = champValue


		# Transform string to JSON format
		newJson = json.dumps(bufferisedData, indent=4, sort_keys=True)

		# Write this JSON in the file
		data.write(newJson)

		# Close flots
		data.close()

		# Sort du programme
		sys.exit()