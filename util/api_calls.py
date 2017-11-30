# Team CYES
# Samantha Ngo, Carol Pan, Eugene Thomas, Yuyang Zhang
# SoftDev1 pd7
# P01 -- ArRESTed Development
# 2017-11-22

import urllib2
import json

# Variable to hold latest forecast for analysis
# global currentForecast

# Setup: read in keys and set urls
def readingKeys(file):
    global book_key
    global events_key
    global weather_key
    global geo_url
    global weather_url
    global book_url
    global events_url
    global currentForecast
    
    print "Reading keys..."
    with open(file,"r") as l:
        book_key = l.readline().strip()
        print book_key
        events_key = l.readline().strip()
        print events_key
        weather_key = l.readline().strip()
        print weather_key
    # Set base URLs
    geo_url = "http://api.wunderground.com/api/" + weather_key + "/geolookup/q/"
    weather_url = "http://api.wunderground.com/api/" + weather_key + "/forecast/q/"
    book_url = "https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json" \
               + "?api-key=" + book_key +"&age-group="
    events_url = "https://www.eventbriteapi.com/v3/events/search/?token=" + events_key + "&q=outdoors&location.address=<zipcode>&location.within=50mi"
    return True

def weathercall(zipcode):
    geoResp = urllib2.urlopen(geo_url + str(zipcode) + ".json")
    gdata= geoResp.read()
    gform= json.loads(gdata)
    print "retrieving data from " + geo_url + str(zipcode) +".json"
    try: 
        #change zip code to appropriate city and state
        location= gform["location"]["requesturl"]
        print location
        print "+++++++++++++++++++++++++++++++++++++++++++++++++"
        location= location.replace("html", "json")
        print location
        print "+++++++++++++++++++++++++++++++++++++++++++++++++"
        
        #now actually getting the weather
        print "retrieving data from " + weather_url  + location
        weatherResp = urllib2.urlopen(weather_url + location)
        wdata = weatherResp.read()
        wform= json.loads(wdata)
        forecasts = wform["forecast"]["txt_forecast"]["forecastday"]
        currentForecast = forecasts
        return (True, forecasts)
    except:
        print "Could not find location"
        currentForeCast = "Could not find location"
        return (False,)

def getweather(data, period):
    try:
        forecast = data[period]["fcttext"].split(".")
        temp = ""
        for char in forecast[1]:
            if char.isdigit():
                temp += char
                forecast[1] = int(temp)
        forecast[2]=forecast[2].lstrip()
        for item in forecast:
            print item
        return (True, forecast)
    except:
        return (False,)

def bookcall(age):
    try:
        print "retrieving data from " + book_url + age
        bookResp = urllib2.urlopen(book_url + age)
        burl= bookResp.geturl()
        bdata= bookResp.read()
        bform= json.loads(bdata)
        if bform["num_results"] == 0:
            bookResp= urllib2.urlopen(book_url)
            bdata= bookResp.read()
            bform= json.loads(bdata)
        return (True, bform)
    except:
        return (False,)

def fiveEvents(zipcode):
    retList = []
    print events_url
    events = events_url.replace("<zipcode>", str(zipcode))
    response = urllib2.urlopen(events_url)
    url = response.geturl()
    info = response.read()
    info = json.loads(info)
    #print info
    i = 0
    while i < 5:
        button = '<form action="<url>"><input type="submit" value="See event"></form>'
        try:
            a = []
            a.append(info["events"][i]["name"]["text"]) 
            a.append( info["events"][i]["description"]["text"])
            a.append(info["events"][i]["url"])
            retList.append(a)
            i += 1
        except:
            retList[i] = "STOP"
            break;
    ## print retList
    return retList

# Testing
# print readingKeys("keys.txt")
# print geo_url
# print weather_url
# weathercall(11229)

# fiveEvents(11229)
