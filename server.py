# -*- coding: utf-8 -*-
# encoding=utf8 

# curl -H "Content-type: application/json" -X POST -d '{ "currentCpuLoad": 95, "currentDiskUsage": 95, "currentSwapUsage" : 99, "currentMemLoad" : 99, "currentConnectedUsers" : 80 }' http://127.0.0.1:5000/
 
from flask import Flask, jsonify, request, render_template, url_for
from IssueDetector import *
from SaveData import *
from datetime import *

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

def CalculDate(requete):

	now = datetime.now()
	old = datetime.strptime(requete[0][1], '%Y-%m-%d %H:%M:%S.%f')
	dateEcart = now - old
	dateEcart = dateEcart.seconds

	ecart = {
		"hours" : str(dateEcart / 3600),
		"minutes" : str((dateEcart / 60) % 60),
		"seconds" : str(dateEcart % 60)
	}

	return ecart['hours'] + " H " + ecart['minutes'] + " m " + ecart['seconds'] + " s"

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

	# Fermeture des flux
	conn.close()
	donn.close()

	nbrUsers = requete1[0][0]

	ecartStr = CalculDate(requete1)

	data = {
		"lastMaj" : ecartStr,
		"distinctComputers" : nbrUsers,
		"countRequest" : str(requete2[0][0]),
		"alerts" : str(requete3[0][0])
	}

	return render_template('index.html.j2', data=data)

@app.route('/vulnerabilites', methods=['GET'])
def vulnerabilites():
    return render_template('vulnerabilites.html.j2')

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

#------------------------#
#   L'API commence ici	 #
#------------------------#
@app.route('/', methods=['POST'])
def api():
	if request.method == 'POST':

		# Json reçu par le client via une requête POST
		JsonIn = request.get_json()

		# Vérifie si les données reçus par le client
		# Envoie un mail si une situation de crise à été détecter
		Program(JsonIn)

		SaveData(JsonIn)

		return "Data received", 200

	else :
		return "Only POST is working" + '\n', 405

if __name__ == '__main__':
	app.run(debug=True)