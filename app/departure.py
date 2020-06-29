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
ADDRESS = os.environ.get("ADDRESS")
CITY = os.environ.get("CITY")
STATE = os.environ.get("STATE")
ZIP_CODE = os.environ.get("ZIP_CODE")

if __name__ == "__main__":


    if APP_ENV == "development":
        flight = input("PLEASE INPUT THE FLIGHT NUMBER (e.g. 5187): ")
        airline = input("PLEASE INPUT THE AIRLINE (e.g. American Airlines): ")
        def get_flight_information(airline=airline,flight=flight):
            request_url = f"http://api.aviationstack.com/v1/flights?access_key={FLIGHT_KEY}&airline_name={airline}&flight_number={flight}&flight_status=active"
            response = requests.get(request_url)
            api_response = json.loads(response.text)
            # print(api_response) 
            departure = dict()
            departure['arrival_airport'] = (api_response['data'][0]['arrival']['airport'])
            departure['timezone'] = (api_response['data'][0]['arrival']['timezone'][8:])
            departure['estimated_arrival'] = (api_response['data'][0]['arrival']['estimated_runway'])
            return departure
        results = get_flight_information(airline=airline,flight=flight)   
    else:
        results = get_flight_information()
    # print(results)

    departure_info = (get_flight_information())
    flight_arrival = (departure_info['estimated_arrival'][:-6])
    airport = (departure_info['arrival_airport'])
    t_city = (departure_info['timezone'])

    if APP_ENV == "development":
        f_street = input("PLEASE INPUT YOUR STREET ADDRESS: ")
        f_city = input("PLEASE INPUT YOUR CITY: ")
        f_state = input("PLEASE INPUT YOUR STATE (e.g. NY): ")
        f_zip = input("PLEASE INPUT YOUR ZIP CODE (e.g. 10012): ")
        def get_departure_time(f_street=ADDRESS,f_city=CITY,f_state=STATE,f_zip=ZIP_CODE,airport=airport,t_city=t_city,flight_arrival=flight_arrival):
            request_url = f"http://www.mapquestapi.com/directions/v2/optimizedroute?key={MAPS_KEY}&from={f_street},+{f_city},+{f_state},+{f_zip}&to={airport}&timeType=3&isoLocal={flight_arrival}"
            response = requests.get(request_url)
            response_data = json.loads(response.text)
            # print(response.status_code)
            # print(response_data)
            travel_time = (response_data['route']['realTime'])
            departure_time = (datetime.datetime.fromisoformat(flight_arrival)-datetime.timedelta(seconds=travel_time))
            d_time = (departure_time.strftime("%B %d, %I:%M:%S %p"))
            return d_time
        results = get_departure_time(f_street=f_street,f_city=f_city,f_state=f_state,f_zip=f_zip,)
    else:
        results = get_departure_time()
    print(f"LEAVE AT: {results}") 
# print(get_departure_time())

