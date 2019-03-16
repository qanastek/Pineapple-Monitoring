# -*- coding: utf-8 -*-

# curl -H "Content-type: application/json" -X POST -d '{ "currentCpuLoad": 95, "currentDiskUsage": 95, "currentSwapUsage" : 99, "currentMemLoad" : 99, "currentConnectedUsers" : 80 }' http://127.0.0.1:5000/
 
from flask import Flask, jsonify, request
from IssueDetector import *

app = Flask(__name__)

# request.get_json()

@app.route('/', methods=['POST'])
def hello():
	if request.method == 'POST':

		# Json reçu par le client via une requête POST
		JsonIn = request.get_json()

		# Vérifie si les données reçus par le client
		# Envoie un mail si une situation de crise à été détecter
		Program(JsonIn)

		return "Data received", 200

	else :
		return "Only POST is working" + '\n', 405

@app.route("/voiture")
def car():
	return jsonify({"brand" : "renault"})

if __name__ == '__main__':
	app.run(debug=True)