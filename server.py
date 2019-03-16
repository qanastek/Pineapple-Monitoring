#!/usr/bin/python

# curl -H "Content-type: application/json" -X POST -d '{"name":"Labrak Yanis"}' http://127.0.0.1:5000/
 
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello():
	if request.method == 'POST':
		return jsonify(request.get_json()), 201
	else :
		return "no result" + '\n'

@app.route("/voiture")
def car():
	return jsonify({"brand" : "ferrari"})

if __name__ == '__main__':
	app.run(debug=True)