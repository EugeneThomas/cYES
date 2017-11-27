# Team CYES
# Samantha Ngo, Carol Pan, Eugene Thomas, Yuyang Zhang
# SoftDev1 pd7
# P01 -- ArRESTed Development
# 2017-11-22

import urllib2
import json

# Global Variables
book_key = ""
events_key = ""
weather_key = ""

def readingKeys(file):
    print "Reading keys..."
    with open(file,"r") as l:
        book_key = l.readline().strip()
        print book_key
        events_key = l.readline().strip()
        print events_key
        weather_key = l.readline().strip()
        print weather_key
    return True

readingKeys("testKeys.txt")

# URLs
geo_url = "http://api.wunderground.com/api/" + weather_key + "/geolookup/q/"
weather_url = "http://api.wunderground.com/api/" + weather_key + "/forecast/q/"
book_url = "https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json" \
           + "?api-key=" + book_key +"&age-group="
events_url = ""
    
def weathercall(zipcode):
    geoResp = urllib2.urlopen(geo_url + zipcode + ".json")
    gdata= geoResp.read()
    gform= json.loads(gdata)
    location= gform["location"]["requesturl"]
    location= location.replace("html", "json")
    print "retrieving data from " + weather_url + location
    weatherResp = urllib2.urlopen(weather_url + location)
    wdata = weatherResp.read()
    wform= json.loads(wdata)
    return wform

def bookcall(age):
    print "retrieving data from " + book_url + age
    bookResp = urllib2.urlopen(book_url + age)
    burl= bookResp.geturl()
    bdata= bookResp.read()
    bform= json.loads(bdata)
    return bform
