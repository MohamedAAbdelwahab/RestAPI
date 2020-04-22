import  urllib
import json
import flask
from flask import render_template, request
from API import BaseAPI
from DataBase import OfflineData
import requests_cache

app = flask.Flask(__name__)



@app.route('/', methods=["GET"])
def home():
   return"Welcome to Our simple API <br/> " \
         "to use our API please follow the following instruction <br/> " \
         "for specific country with all info please type localhost:5000/ and type the country name <br/>" \
         "for specific info about a specific country please type localhost:5000/ then add the country name then / and here add your specific info <br/>" \
         "for more than one info please type  localhost:5000/ then add the country name then / and here add your specific info , the second info"
@app.route('/<country>')
def ALLInfo(country=None):
        countryInfo=gettingInfo(country)
        if countryInfo is not None:
            return str(countryInfo)
            print("ana hnaaa")
        else:
             return ("Not Found")

@app.route("/<country>/<path:varargs>")
def GetSpecificInfo(varargs=None,country=None):
    varargs = varargs.split(",")
    string=" "
    countryInfo = gettingInfo(country)
    if countryInfo=="Not Found":
      return "Not Found"
    try:
         for i in varargs:
              string = " "+i+"= "+str(countryInfo[i])+string + " "
    except KeyError:
        return  "invalid key"
    return str(string)
def CheckInternetConnection(host='http://google.com'):
    try:
        urllib.request.urlopen(host)  # Python 3.x

        return True
    except:

        return False
def gettingInfo(country):
    countryInfo = None
    baseAPI = BaseAPI()
    country = country
    if CheckInternetConnection():
        countryInfo = baseAPI.get_country_info(country)

    else:
        o = OfflineData()
        countryInfo = o.GetData(country)
    return countryInfo




if __name__ == '__main__':
    app.run()