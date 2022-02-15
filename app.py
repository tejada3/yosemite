from flask import Flask

from flask import Flask, jsonify, request
# This is a sample Python script.
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import boto3
from flask_cors import CORS
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
BASE_ROUTE = "/weather"


def print_hi(url):
    title = None
    try:
        html = urlopen(url)

    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs
        return title
    except AttributeError as e:
        print(e)

    return title


@app.route(BASE_ROUTE + "/yosemite-valley", methods=['GET'])
def yosemiteValley():  # put application's code here
    yvTemp = print_hi("https://forecast.weather.gov/MapClick.php?lon=-119.61292&lat=37.73639#.YgvkjejMIuV")
    temp = yvTemp.html.body.find('p', {'class': 'myforecast-current-lrg'}).getText().strip("°F")
    print(temp)
    return temp

@app.route(BASE_ROUTE + "/tuolumne-meadows", methods=['GET'])
def tuolumneMeadows():
    tmTemp = print_hi("https://forecast.weather.gov/MapClick.php?lon=-119.35666&lat=37.87522#.Ygvo2ujMIuV")
    temp = tmTemp.html.body.find('p', {'class': 'myforecast-current-lrg'}).getText().strip("°F")
    return temp

@app.route(BASE_ROUTE + "/mariposa-grove", methods=['GET'])
def mariposaGrove():
    mgTemp = print_hi("https://forecast.weather.gov/MapClick.php?lon=-119.60039&lat=37.50387#.YgvqX-jMIuV")
    temp = mgTemp.html.body.find('p', {'class': 'myforecast-current-lrg'}).getText().strip("°F")
    return temp

if __name__ == '__main__':
    app.run()
