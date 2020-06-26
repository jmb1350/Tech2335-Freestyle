#flights.py

# app/robo_advisor.py

import json
import csv
import os
import pyflightdata
from datetime import datetime

from dotenv import load_dotenv
import requests

load_dotenv()



#Info Inputs and Data Requests

#TODO: Pull from user input Flight Number

#f_flight = "UA2402"

FLIGHT_KEY = os.environ.get("PLANE_API_KEY")
flight = "2745"
airline = "DL"

#estimated_runwway = "estimated_runway"

request_url = f"http://api.aviationstack.com/v1/flights?access_key={FLIGHT_KEY}&airline_iata={airline}&flight_number={flight}&flight_status=active"


response = requests.get(request_url)
api_response = json.loads(response.text) 

#https://stackoverflow.com/questions/25855276/parsing-json-with-python-typeerror-list-indices-must-be-integers-not-str/25855320
#this was helpful in getting the list to respond correctly.
print(api_response['data'][0]['arrival']['airport'])





#TODO: Provide Arrival Airport and Arrival Time



#for flight in api_response['airline']:
    #print("The airline is": {airline}) 
    #flight['airline']['name']