'''
Team CYES
Samantha Ngo, Carol Pan, Eugene Thomas, Yuyang Zhang
SoftDev1 pd7
P01 -- ArRESTed Development
2017-11-16
'''

from flask import Flask, render_template, request
from flask import redirect, flash, url_for
import urllib2

app = Flask (__name__)

'''
use the following code to retrieve keys (specify as needed)
'''
with open("weatherapi.txt", "r") as w:
    weather_key = w.readline().rstrip()

with open("eventapi.txt", "r") as e:
    book_key = e.readline().rstrip()
    local_key = e.readline().rstrip()
    tourist_key = e.readline().rstrip()
    
    
#home route, takes zipcode and other inputs
@app.route("/")
def hello_world():
    print "**DIAG: has api key been acquired?**"
    print "The weather api key is " + weather_key
    print "The weather api key is " + book_key
    print "The weather api key is " + local_key
    print "The weather api key is " + tourist_key
    return "Yo what up."

#reach out to apis and acquire info
@app.route("/info")
def display_info():
    return "Yo what up."

if __name__ == "__main__":
    app.debug = True
    app.run()
