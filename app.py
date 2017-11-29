# Team CYES
# Samantha Ngo, Carol Pan, Eugene Thomas, Yuyang Zhang
# SoftDev1 pd7
# P01 -- ArRESTed Development
# 2017-11-16

from flask import Flask, render_template, request
from flask import session, redirect, flash, url_for
from util import api_calls as api
import os
import datetime

now = datetime.datetime.now()
app = Flask (__name__)
app.secret_key = os.urandom(32)



#home route, takes zipcode and other inputs
@app.route("/")
def hello_world():
    print "**DIAG: has api key been acquired?**"

    '''will figure out how to display keys at later date'''
    return render_template("base.html")

#reach out to apis and acquire info
@app.route("/info")
def display_info():
    #retrieving the name
    session["name"]=request.args["name"]
    #retrieving weather data
    session["zipcode"]=request.args["zipcode"]
    #code for api call have been moved to util/api_calls.py
    session["wform"]= api.weathercall(session["zipcode"])
    #retrieving book data
    age=request.args["age"]
    #code for api call have been moved to util/api_calls.py
    bform = api.bookcall(age)

    return render_template("info.html", name=session["name"], bookdata=bform, weatherdata=session["wform"])

@app.route("/events")
def event_page():
    period = int(request.args["period"])    
    forecast = api.getweather(session["wform"], period)

    #IMPORTANT STUFF HERE::::
    description = forecast[0]
    temperature = forecast[1]
    windspeed = forecast[2]
    zipcode = session["zipcode"]
    year = now.year
    month = now.month
    day = now.day + (period-1)/2
    if day > 30:
        day -= 30
        month += 1
    
    return render_template("events.html", name=session["name"])


if __name__ == "__main__":
    app.debug = True
    app.run()
