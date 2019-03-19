# -*- coding: utf-8 -*-
# encoding=utf8 

# curl -H "Content-type: application/json" -X POST -d '{ "currentCpuLoad": 95, "currentDiskUsage": 95, "currentSwapUsage" : 99, "currentMemLoad" : 99, "currentConnectedUsers" : 80 }' http://127.0.0.1:5000/
 
from flask import Flask, jsonify, request, render_template, url_for
from IssueDetector import *
from SaveData import *

# Lancement d'UTF-8
reload(sys)  
sys.setdefaultencoding('utf8')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html.j2')

@app.route('/vulnerabilites', methods=['GET'])
def vulnerabilites():
    return render_template('vulnerabilites.html.j2')

@app.route('/historique', methods=['GET'])
def historique():
	database = getTable()
	return render_template('database.html.j2', DB=database)

@app.route('/ordinateurs', methods=['GET'])
def ordinateurs():
	return "ordinateurs"

@app.route('/config_smtp', methods=['GET'])
def config_smtp():
	return "config_smtp"

@app.route('/config_mail_data', methods=['GET'])
def config_mail_data():
	return "config_mail_data"

@app.route('/config_mail_template', methods=['GET'])
def config_mail_template():
	return "config_mail_template"

@app.route('/config_mail_signature', methods=['GET'])
def config_mail_signature():
	return "config_mail_signature"

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

@app.route('/alarmes', methods=['GET'])
def alarmes():
	return "alarmes"

@app.route('/config_alarm_maj', methods=['GET'])
def config_alarm_maj():
	return "config_alarm_maj"

@app.route('/config_alarm_quotas', methods=['GET'])
def config_alarm_quotas():
	return "config_alarm_quotas"

@app.route('/config_alarm_other', methods=['GET'])
def config_alarm_other():
	return "config_alarm_other"

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