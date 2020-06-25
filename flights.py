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

f_flight = "UA2402"

FLIGHT_KEY = os.environ.get("PLANE_API_KEY")
flight = "UA2402"

request_url = f"http://api.aviationstack.com/v1/flights?access_key={FLIGHT_KEY}"




response = requests.get(request_url)
api_response = json.loads(response.text) 
print(response.status_code)



#TODO: Provide Arrival Airport and Arrival Time




#flight = ("DAL1429")

#for flight in api_response['results']:
    #if (flight['live']['is_ground'] is False):
       # print(u'%s flight %s from %s (%s) to %s (%s) is in the air.' % (
        #    flight['airline']['name'],
         #   flight['flight']['iata'],
          #  flight['departure']['airport'],
           # flight['departure']['iata'],
            #flight['arrival']['airport'],
            #flight['arrival']['iata']))


#for flight in api_response['airline']:
    #print("The airline is": {airline}) 
    #flight['airline']['name']