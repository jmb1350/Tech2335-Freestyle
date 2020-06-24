#flights.py

# app/robo_advisor.py

import json
import csv
import os
import pyflightdata
from datetime import datetime

from pyflightdata import FlightData
from dotenv import load_dotenv
import requests

api=FlightData()
api.get_countries()
print({countries})






















Info Inputs and Data Requests


api_key = os.environ.get("PLANE_API_KEY")

request_url = f"http://api.aviationstack.com/v1/flights?access_key={api_key}"
access_key = api_key

requests.get(request_url)

response = requests.get(request_url)

api_response = json.loads(response.text) 







response = requests.get(request_url, api_key)


api_response = api_result.json()

api_result = requests.get('http://api.aviationstack.com/v1/flights?acess_key', api_key)



flight = ("AF5393")

for flight in api_response['results']:
    if (flight['live']['is_ground'] is False):
        print(u'%s flight %s from %s (%s) to %s (%s) is in the air.' % (
            flight['airline']['name'],
            flight['flight']['iata'],
            flight['departure']['airport'],
            flight['departure']['iata'],
            flight['arrival']['airport'],
            flight['arrival']['iata']))


for flight in api_response['airline']:
    print("The airline is": {airline}) 
    flight['airline']['name']