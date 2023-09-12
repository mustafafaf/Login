from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

def verifyname():
    json

@app.route("/test", methods=["GET"])
def helloworld():
    return "hello world"

@app.route("/", methods=["GET"])
def getdetails():
    return render_template("form.html")

@app.route("/verify", methods=["POST"])
def verify():
    if request.method=="POST":

        formdata=request.form
        with open("users.json","r") as f:
            archive=json.load(f)    

        for i in archive.keys():
            if formdata["username"]==i:
                if formdata["password"]==archive[i]["password"]:
                    return "verified"
                return "wrong password"
            
        return "username not found"

       


#python -m venv .venv
#.venv\Scripts\activate
#flask --app login run