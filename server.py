# -*- coding: utf-8 -*-
# encoding=utf8 

# curl -H "Content-type: application/json" -X POST -d '{ "currentCpuLoad": 95, "currentDiskUsage": 95, "currentSwapUsage" : 99, "currentMemLoad" : 99, "currentConnectedUsers" : 80 }' http://127.0.0.1:5000/
 
from flask import Flask, jsonify, request, render_template
from IssueDetector import *

# Lancement d'UTF-8
reload(sys)  
sys.setdefaultencoding('utf8')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    infos = {
    	"titleFun" : "🍍 Pineapple Monitoring 🍍",
    	"title" : "Pineapple Monitoring",
    	"author" : "Labrak Yanis",
    	"connected" : "Labrak Yanis",
    	"url_profile_pic" : "https://community-cdn-digitalocean-com.global.ssl.fastly.net/assets/tutorials/images/large/nodejs_ubuntu_install.png?1530879921",
    	"description" : "Network monitoring for small business"
    }
    return render_template('index.html', infos=infos)

@app.route('/', methods=['POST'])
def api():
	if request.method == 'POST':

		# Json reçu par le client via une requête POST
		JsonIn = request.get_json()

		# Vérifie si les données reçus par le client
		# Envoie un mail si une situation de crise à été détecter
		Program(JsonIn)

		return "Data received", 200

	else :
		return "Only POST is working" + '\n', 405

if __name__ == '__main__':
	app.run(debug=True)