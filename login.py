from flask import Flask, render_template, request, redirect
import requests
import json

app = Flask(__name__)

#renders login page
@app.route("/", methods=["GET"])
def getdetails():
    return render_template("form.html")

#verifies details
@app.route("/verify", methods=["POST"])
def verify():
    if request.method=="POST":

        formdata=request.form
        #opens json file
        with open("users.json","r") as f:
            archive=json.load(f)    

        
        for i in archive.keys():
            if formdata["username"]==i:
                if formdata["password"]==archive[i]["password"]:
                    return "verified"
                return "wrong password"
            
        return "username not found"
    
#renders signup page
@app.route("/signup", methods=["GET"])
def signup():
    return render_template("signup.html")

#adds user data to json
@app.route("/register", methods=["POST"])
def register():
    if request.method=="POST":
        formdata=request.form

        with open("users.json","r+") as f:  
            #loads json file into object
            archive=json.load(f)
            #checks details aren't already in use
            for i in archive.keys():
                if formdata["username"]==i:
                    return render_template("signup.html",error="username already in use")
                if formdata["email"]==archive[i]["email"]:
                    return render_template("signup.html",error="email already in use")
            #adds new details to object
            archive[formdata["username"]]={
                "password":formdata["password"],
                "email":formdata["email"],
                "name":formdata["name"]
            }
            f.seek(0)
            #writes data to json
            json.dump(archive,f,indent=4)


        return redirect("/")
       


#python -m venv .venv
#.venv\Scripts\activate
#flask --app login run