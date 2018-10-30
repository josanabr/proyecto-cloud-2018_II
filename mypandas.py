#!/usr/bin/python
from flask import Flask, jsonify, abort, make_response, request
import pandas as pd

app = Flask(__name__)
df = None
url = None

@app.route('/')
def saludo():
	global df
	print("hola")
	return str(df.shape)

@app.route('/calcularmedia', methods = ['POST'])
def calcularmedia():
	global df
	campo = request.json.get("campo","")
	return str(df[campo].mean())

@app.route("/encabezado", methods = [ 'GET' ])
def encabezado():
	global df
	return str(df.columns)

@app.route("/imprimirtipos", methods = ['GET'])
def imprimirtipos():
	global df
	return str(df.dtypes)

@app.route('/seturl', methods = ['POST'])
def seturl():
	global url
	global df
	url = request.json.get('url',"")
	c = request.json.get('sep',"\t")
	print("Nuevo url %s separador %s\n"%(url,c))
	df = pd.read_csv(url,sep=c)
	return "OK"

if __name__ == '__main__':
    df = pd.read_csv('/myhome/gapminder.tsv', sep='\t')
    app.run(host='0.0.0.0',debug=True)

