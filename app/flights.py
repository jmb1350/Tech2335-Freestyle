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

#TODO: Pull from user input Flight Number

#f_flight = "UA2402"
APP_ENV = os.environ.get('APP_ENV', 'Dev')
FLIGHT_KEY = os.environ.get("PLANE_API_KEY")
FLIGHT = os.environ.get("FLIGHT_NUMBER")
AIRLINE = os.environ.get("AIRLINE")

def get_flight_information(airline=AIRLINE,flight=FLIGHT):
    request_url = f"http://api.aviationstack.com/v1/flights?access_key={FLIGHT_KEY}&airline_name={airline}&flight_number={flight}&flight_status=active"

    response = requests.get(request_url)
    api_response = json.loads(response.text)
    # print(api_response) 
    arrival_airport = (api_response['data'][0]['arrival']['airport'])
    timezone = (api_response['data'][0]['arrival']['timezone'][8:])
    estimated_arrival = (api_response['data'][0]['arrival']['estimated_runway'])
    return arrival_airport, timezone, estimated_arrival

# print(get_flight_information())
# print(type(get_flight_information()))

if __name__ == "__main__":

    if APP_ENV == "development":
        flight = input("PLEASE INPUT THE FLIGHT NUMBER (e.g. 5187): ")
        airline = input("PLEASE INPUT THE AIRLINE (e.g. American Airlines): ")
        results = get_flight_information(airline=airline,flight=flight)
    else:
        results = get_flight_information()
    print(results)

#https://stackoverflow.com/questions/25855276/parsing-json-with-python-typeerror-list-indices-must-be-integers-not-str/25855320
#this was helpful in getting the list to respond correctly.
# arrival_airport = (api_response['data'][0]['arrival']['airport'])
# print(arrival_airport)

# timezone = (api_response['data'][0]['arrival']['timezone'][8:])
# print(timezone)

# estimated_arrival = (api_response['data'][0]['arrival']['estimated_runway'])
# print(estimated_arrival)