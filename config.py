
import bson
import json 
import pymongo 
from flask import Flask,make_response,flash,request,render_template,url_for,redirect,send_file,jsonify
import os
import sys


app=Flask(__name__)
app.secret_key='mezlinikfdshqlkfh'

@app.route("/rendertemp")
def jsontohtml():
	# la recherche dans la base de donn_ee de site dont son _id est essai
	site=[x for x in pymongo.MongoClient().site.site.find({"_id":"essai"})]#liste de site 
	site=site[0]# site[0] est un dictionnaire (json de site)

	return render_template("render_temp.html",site=site)



if __name__ == '__main__':
    app.run(debug='true')