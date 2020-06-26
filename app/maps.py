import os
import json
import requests
from dotenv import load_dotenv
import datetime
from datetime import timedelta

from app.flights import estimated_arrival
from app.flights import arrival_airport
from app.flights import timezone

load_dotenv()
APP_ENV = os.environ.get('APP_ENV', 'Dev')
MAPS_KEY = os.environ.get("MAPQUEST_API")
#user address
ADDRESS = os.environ.get("ADDRESS")
CITY = os.environ.get("CITY")
STATE = os.environ.get("STATE")
ZIP_CODE = os.environ.get("ZIP_CODE")

flight_arrival = estimated_arrival[:-6]
airport = arrival_airport
t_city = timezone


def get_departure_time(f_street=ADDRESS,f_city=CITY,f_state=STATE,f_zip=ZIP_CODE,airport=arrival_airport,t_city=timezone,flight_arrival=flight_arrival):
    request_url = f"http://www.mapquestapi.com/directions/v2/optimizedroute?key={MAPS_KEY}&from={f_street},+{f_city},+{f_state},+{f_zip}&to={t_city},+{airport}&timeType=3&isoLocal={flight_arrival}"
    response = requests.get(request_url)
    response_data = json.loads(response.text)
    print(response.status_code)
    # print(response_data)
    travel_time = (response_data['route']['realTime'])
    departure_time = (datetime.datetime.fromisoformat(flight_arrival)-datetime.timedelta(seconds=travel_time))
    d_time = (departure_time.strftime("%B %d, %I:%M:%S %p"))
    return d_time
    
# print(get_departure_time())

if __name__ == "__main__":

    if APP_ENV == "development":
        f_street = input("PLEASE INPUT YOUR STREET ADDRESS:")
        f_city = input("PLEASE INPUT YOUR CITY:")
        f_state = input("PLEASE INPUT YOUR STATE (e.g. NY):")
        f_zip = input("PLEASE INPUT YOUR ZIP CODE (e.g. 10012):")
        results = get_departure_time(f_street=f_street,f_city=f_city,f_state=f_state,f_zip=f_zip)
    else:
        results = get_departure_time()
    print(f"LEAVE AT: {results}")    