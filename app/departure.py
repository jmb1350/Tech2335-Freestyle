import json
import csv
import os
import datetime
from datetime import timedelta

from dotenv import load_dotenv
import requests

load_dotenv()

#TODO: Pull from user input Flight Number

#f_flight = "UA2402"
APP_ENV = os.environ.get('APP_ENV', 'Dev')
FLIGHT_KEY = os.environ.get("PLANE_API_KEY")
#maps
MAPS_KEY = os.environ.get("MAPQUEST_API")
#user address
AIRLINE = os.environ.get("AIRLINE")
FLIGHT = os.environ.get("FLIGHT")
AIRPORT = os.environ.get("AIRPORT")
FLIGHT_ARRIVAL = os.environ.get("FLIGHT_ARRIVAL")
ADDRESS = os.environ.get("ADDRESS")
CITY = os.environ.get("CITY")
STATE = os.environ.get("STATE")
ZIP_CODE = os.environ.get("ZIP_CODE")

def get_flight_information(airline=AIRLINE,flight=FLIGHT):
    request_url = f"http://api.aviationstack.com/v1/flights?access_key={FLIGHT_KEY}&airline_name={airline}&flight_number={flight}&flight_status=active"
    response = requests.get(request_url)
    api_response = json.loads(response.text)
    # print(api_response) 
    # breakpoint()
    departure = dict()
    if any(api_response['data']):
        departure['arrival_airport'] = (api_response['data'][0]['arrival']['airport'])
        departure['timezone'] = (api_response['data'][0]['arrival']['timezone'][8:])
        departure['estimated_arrival'] = (api_response['data'][0]['arrival']['estimated_runway'])
    else:
        print("There was an error with the flight information entered. Please try again.")
        exit()
    return departure
        
def get_departure_time(f_street=ADDRESS,f_city=CITY,f_state=STATE,f_zip=ZIP_CODE,airport=AIRPORT,flight_arrival=FLIGHT_ARRIVAL):
    request_url = f"http://www.mapquestapi.com/directions/v2/optimizedroute?key={MAPS_KEY}&from={f_street},+{f_city},+{f_state},+{f_zip}&to={airport},+airport&timeType=3&isoLocal={flight_arrival}"
    response = requests.get(request_url)
    response_data = json.loads(response.text)
    # print(response.status_code)
    # print(response_data)
    travel_time = (response_data['route']['realTime'])
    departure_time = (datetime.datetime.fromisoformat(flight_arrival)-datetime.timedelta(seconds=travel_time))
    d_time = (departure_time.strftime("%B %d, %I:%M:%S %p"))
    return d_time

if __name__ == "__main__":

    if APP_ENV == "development":
        flight = input("PLEASE INPUT THE FLIGHT NUMBER (e.g. 5187): ")
        airline = input("PLEASE INPUT THE AIRLINE (e.g. American Airlines): ")
        results = get_flight_information(airline=airline,flight=flight)
    else:
        results = get_flight_information()
    # print(results)

    flight_arrival = (results['estimated_arrival'][:-6])
    airport = (results['arrival_airport'])
        
    if APP_ENV == "development":
        f_street = input("PLEASE INPUT YOUR STREET ADDRESS: ")
        f_city = input("PLEASE INPUT YOUR CITY: ")
        f_state = input("PLEASE INPUT YOUR STATE (e.g. NY): ")
        f_zip = input("PLEASE INPUT YOUR ZIP CODE (e.g. 10012): ")
        results = get_departure_time(f_street=f_street,f_city=f_city,f_state=f_state,f_zip=f_zip,flight_arrival=flight_arrival,airport=airport)
    else:
        results = get_departure_time()
    print(f"LEAVE AT: {results}") 
# print(get_departure_time())

