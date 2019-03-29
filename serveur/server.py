#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf8

# curl -H "Content-type: application/json" -X POST -d '{ "currentCpuLoad": 95, "currentDiskUsage": 95, "currentSwapUsage" : 99, "currentMemLoad" : 99, "currentConnectedUsers" : 80 }' http://127.0.0.1:5000/
 
from flask import Flask, jsonify, request, render_template, url_for
from IssueDetector import *
from SaveData import *
from datetime import *

from lxml import html
import requests

# Lancement d'UTF-8
reload(sys)  
sys.setdefaultencoding('utf8')

app = Flask(__name__)

# Global functions
@app.context_processor
def utility_processor():
	def ToMacAddresse(mac):

		n = 2
		mac = map(''.join, zip(*[iter(mac)]*2))

		final = ""

		for i in range(len(mac)-1) :

			final += str(mac[i]) + ":"

		final += str(mac[len(mac)-1])

		return str(final)

	def DateToRead(date):

		date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
		newDate = str(date.day) + "/" + str(date.month) + "/" + str(date.year) + " AT " + str(date.hour) + ":" + str(date.minute) + ":" + str(date.second)

		return str(newDate)

	return dict(DateToRead=DateToRead,ToMacAddresse=ToMacAddresse)

def CheckReceivedData(JsonIn):

	allowedElements = [
		"mac",
		"currentCpuLoad",
		"currentDiskUsage",
		"currentMemLoad",
		"currentSwapUsage",
		"processCounter",
		"currentConnectedUsers",
		"sysExp"
	]

	allowedString = ["mac", "sysExp"]

	if len(JsonIn) != len(allowedElements):

		return "Bad request, number of args not allowed ! " + '\n', 501

	for element in JsonIn:

		# Check if key is allowed
		if element not in allowedElements:

			return "Invalid members " + element + "." + '\n', 502

		# Check if they are integers
		if element not in allowedString and type(JsonIn[element]) != type(14):

			return "Invalid type " + element + "." + '\n', 503

		# Check if mac or os is an unicode
		if element in allowedString and type(JsonIn[element]) != type(unicode("test")):

			return "Invalid type " + element + "." + '\n', 504

	return 200

def CalculDate(requete):

	now = datetime.now()
	old = datetime.strptime(requete[0][1], '%Y-%m-%d %H:%M:%S.%f')

	dateEcart = now - old
	s = dateEcart.seconds

	daysEcart = int(dateEcart.days * 24)

	hours, remainder = divmod(s, 3600)
	minutes, seconds = divmod(remainder, 60)

	return str('{:02}H{:02}m{:02}s'.format(int(hours) + daysEcart, int(minutes), int(seconds)))

@app.route('/', methods=['GET'])
def index():

	conn = sqlite3.connect('history.db')

	c = conn.cursor()

	donn = sqlite3.connect('alerts.db')

	d = donn.cursor()

	c.execute("SELECT count(distinct mac), max(receivedDate) from historique")

	requete1 = c.fetchall()

	c.execute("SELECT count(*) from historique where receivedDate > DATE('now', '-1 day')")

	requete2 = c.fetchall()

	d.execute("SELECT count(*) from alerts where receivedDate > DATE('now', '-2 day')")

	requete3 = d.fetchall()

	c.execute("""SELECT COUNT(*) AS 'Requests',
				strftime('%d', receivedDate) AS 'Day',
				strftime('%m', receivedDate) AS 'Month',
				strftime('%Y', receivedDate) AS 'Year'
				FROM historique
				GROUP BY strftime('%d', receivedDate),
				strftime('%m', receivedDate), strftime('%y', receivedDate)
				ORDER BY 'Year', 'Month', 'Day'
				Limit 7;""")

	requete4 = c.fetchall()

	# Fermeture des flux
	conn.close()
	donn.close()

	nbrUsers = requete1[0][0]

	ecartStr = CalculDate(requete1)

	values = []

	for x in range( len(requete4[0]) + 1 ) :

		date = requete4[x][1] + "/" + requete4[x][2] + "/" + requete4[x][3]
		date.encode("utf-8")

		values.append([int(requete4[x][0]), str(date)])

	data = {
		"lastMaj" : ecartStr,
		"distinctComputers" : nbrUsers,
		"countRequest" : str(requete2[0][0]),
		"alerts" : str(requete3[0][0]),
		"value" : values
	}

	return render_template('index.html.j2', data=data)

@app.route('/vulnerabilites', methods=['GET'])
def vulnerabilites():

	page = requests.get('https://www.cert.ssi.gouv.fr/')
	tree = html.fromstring(page.content)

	titre = tree.xpath('//div[@class="item cert-alert open"]/div/span[@class="item-title"]/a/text()')
	date = tree.xpath('//div[@class="item cert-alert open"]/div/span[@class="item-date"]/text()')
	url = tree.xpath('//div[@class="item cert-alert open"]/div/a[@class="item-link"]/@href')
	url = "https://www.cert.ssi.gouv.fr" + unicode(url[0])
	CERT = tree.xpath('//div[@class="item cert-alert open"]/div/span[@class="item-ref"]/a/text()')

	cert = {
		"titre" : titre[0],
		"date" : date[0],
		"url" : url,
		"CERT" : CERT[0]
	}

	return render_template('vulnerabilites.html.j2', cert=cert)

@app.route('/historiqueAlerts', methods=['GET'])
def historiqueAlerts():
	database = getTableAlerts()

	sort = request.args.get('sort')

	return render_template('alarmDatabase.html.j2', DB=database, sort=sort)

@app.route('/historique', methods=['GET'])
def historique():
	database = getTable()

	sort = request.args.get('sort')

	return render_template('database.html.j2', DB=database, sort=sort)

@app.route('/ordinateurs', methods=['GET'])
def ordinateurs():
	return "ordinateurs"

@app.route('/general', methods=['GET'])
def general():
	return "general"

@app.route('/config_exportation', methods=['GET'])
def config_exportation():
	return "config_exportation"

@app.route('/config_theme_ui', methods=['GET'])
def config_theme_ui():
	return "config_theme_ui"

@app.route('/config_data', methods=['GET'])
def config_data():
	return "config_data"

@app.route('/config_customizer', methods=['GET'])
def config_customizer():
	return "config_customizer"

@app.route('/emails', methods=['GET'])
def emails():
	with open("mail.json", "r") as read_file:
		
		data = json.load(read_file)

	return render_template('emails.html.j2', data=data)

@app.route('/emailMaj', methods=['POST'])
def emailMaj():

	# Open the file in Read mode
	bufferData = open("mail.json", "r")
	bufferisedData = json.load(bufferData)

	# Open the file in Write mode
	data = open("mail.json", "w")

	bufferisedData['addresse'] = str(request.form['addresse'])
	bufferisedData['port'] = int(request.form['port'])
	bufferisedData['senderMail'] = str(request.form['senderMail'])

	bufferisedData['password'] = str(request.form['password'])
	bufferisedData['signature'] = str(request.form['signature'])

	newJson = json.dumps(bufferisedData, indent=4, sort_keys=True)

	# Write this JSON in the file
	data.write(newJson)

	# Close flots
	data.close()

	with open("mail.json", "r") as read_file:

		data = json.load(read_file)

	return render_template('emails.html.j2', data=data)

@app.route('/alarmes', methods=['GET'])
def alarmes():

	with open("settings.json", "r") as read_file:

		data = json.load(read_file)

	return render_template('alarmes.html.j2', data=data)

@app.route('/alarmeMaj', methods=['POST'])
def alarmeMaj():

	# Open the file in Read mode
	bufferData = open("settings.json", "r")
	bufferisedData = json.load(bufferData)

	# Open the file in Write mode
	data = open("settings.json", "w")

	bufferisedData['connectedUsersMax'] = int(request.form['connectedUsersMax'])
	bufferisedData['cpuLoadMax'] = int(request.form['cpuLoadMax'])
	bufferisedData['diskUsageMax'] = int(request.form['diskUsageMax'])

	bufferisedData['memLoadMax'] = int(request.form['memLoadMax'])
	bufferisedData['swapUsageMax'] = int(request.form['swapUsageMax'])
	bufferisedData['processCounter'] = int(request.form['processCounter'])

	newJson = json.dumps(bufferisedData, indent=4, sort_keys=True)

	# Write this JSON in the file
	data.write(newJson)

	# Close flots
	data.close()

	with open("settings.json", "r") as read_file:

		data = json.load(read_file)

	return render_template('alarmes.html.j2', data=data)

@app.route('/loginLoad', methods=['POST'])
def loginLoad():

	login = str(request.form['login'])
	password = str(request.form['password'])

	return render_template('index.html.j2')

@app.route('/login', methods=['GET'])
def login():

	return render_template('login.html.j2')

#------------------------#
#   L'API commence ici	 #
#------------------------#
@app.route('/', methods=['POST'])
def api():

	if request.method == 'POST':

		# Json reçu par le client via une requête POST
		JsonIn = request.get_json()

		print str(json.dumps(JsonIn, indent=4, sort_keys=True))

		if CheckReceivedData(JsonIn) != 200:

			return CheckReceivedData(JsonIn)
		
		# Vérifie si les données reçus par le client
		# Envoie un mail si une situation de crise à été détecter
		Program(JsonIn)

		SaveData(JsonIn)

		return "Data received" + '\n', 200

	else :
		return "Only POST is working" + '\n', 405

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')
	# localhost:5000