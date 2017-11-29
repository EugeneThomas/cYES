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
    
    weather_call= api.weathercall(session["zipcode"])
    if not weather_call[0]:
        flash("Looks like there's a problem with your weather key, or you didn't fill in your zip code.")
        return render_template("error.html")
    session["wform"] = weather_call[1]
    #retrieving book data
    session["age"]=request.args["age"]

    return render_template("info.html", name=session["name"], weatherdata=session["wform"])

@app.route("/events")
def event_page():
    period = int(request.args["period"])    
    try:
        getweather = api.getweather(session["wform"], period)
    except:
        flash("You need to fill out the form first!")
        return render_template("error.html")
    if not getweather[0]:
        flash("Looks like the weather api isn't cooperating. Try again?")
        return render_template("error.html")
    
    forecast = getweather[1]

    #IMPORTANT STUFF HERE::::
    description = forecast[0]
    temperature = forecast[1] #fahrenheit
    windspeed = forecast[2]
    zipcode = session["zipcode"]
    year = now.year
    month = now.month
    day = now.day + (period-1)/2
    if day > 30:
        day -= 30
        month += 1
    if temperature < 30: #too cold, go read a book
        #code for api call have been moved to util/api_calls.py
        book_call = api.bookcall(session["age"])
        if not book_call[0]:
            flash("Looks like there was an error with your NYT book key, or you didn't fill in your age.")
            return render_template("error.html")
        bform = book_call[1]
        return render_template("books.html", name=session["name"], bookdata=bform)
    
    return render_template("events.html", name=session["name"])


if __name__ == "__main__":
    app.debug = True
    app.run()
