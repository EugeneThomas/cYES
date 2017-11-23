'''
Team CYES
Samantha Ngo, Carol Pan, Eugene Thomas, Yuyang Zhang
SoftDev1 pd7
P01 -- ArRESTed Development
2017-11-22
'''
import urllib2
import json

'''
use the following code to retrieve keys (specify as needed)
'''
with open("weatherapi.txt", "r") as w:
    weather_key = w.readline().rstrip()
    
with open("eventapi.txt", "r") as e:
    book_key = e.readline().rstrip()
    local_key = e.readline().rstrip()
    tourist_key = e.readline().rstrip()

'''
the follow are bases for api call strings
'''
geo_url = "http://api.wunderground.com/api/" + weather_key + "/geolookup/q/"
weather_url = "http://api.wunderground.com/api/" + weather_key + "/forecast/q/"
book_url = "https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json" \
           + "?api-key=" + book_key +"&age-group="
    

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
