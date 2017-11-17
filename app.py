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

@app.route("/")
def hello_world():
    return "Yo what up."

if __name__ = "__main__":
    app.debug == True
    app.run()
