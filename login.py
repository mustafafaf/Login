from flask import Flask, render_template, request, redirect
import requests
import csv
import pandas as pd
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
        #opens csv file and copies to archive
        with open("users.csv","r") as f:
            archive=pd.read_csv(f,index_col=0)   
 
        #this code checks that username and password are in the system
        #formdata["username"] is entered username
        #formdata["password"] is entered password
        if formdata["username"] in archive.index:
            if archive.loc[formdata["username"]].loc['password']==formdata["password"]:
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
        
        with open("users.csv","r+") as f:  
            #loads csv file into object
            archive=pd.read_csv(f,index_col=0) 
        #checks details aren't already in use
        if formdata["username"] in archive.index:
            return render_template("signup.html",error="username already in use")
        if formdata["email"] in set(archive["email"]):
            return render_template("signup.html",error="email already in use")

        #writes data to csv
        with open("users.csv","a") as f:
            details=[formdata["username"],formdata["name"],formdata["password"],formdata["email"]]
            writer=csv.writer(f)
            writer.writerow(details)

            #writes data to csv
            


        return redirect("/")
       


#python -m venv .venv
#.venv\Scripts\activate
#flask --app login run