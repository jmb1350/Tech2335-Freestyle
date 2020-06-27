import os
import json
import requests
import pyflightdata
from dotenv import load_dotenv
import datetime
from datetime import timedelta

from app.flights import get_flight_information
from app.maps import get_departure_time

load_dotenv()
APP_ENV = os.environ.get('APP_ENV', 'Dev')
MAPS_KEY = os.environ.get("MAPQUEST_API")
#user address
ADDRESS = os.environ.get("ADDRESS")
CITY = os.environ.get("CITY")
STATE = os.environ.get("STATE")
ZIP_CODE = os.environ.get("ZIP_CODE")
#flight details
FLIGHT_KEY = os.environ.get("PLANE_API_KEY")
FLIGHT = os.environ.get("FLIGHT_NUMBER")
AIRLINE = os.environ.get("AIRLINE")

if __name__ == "__main__":

    if APP_ENV == "development":
        flight = input("PLEASE INPUT THE FLIGHT NUMBER (e.g. 5187): ")
        airline = input("PLEASE INPUT THE AIRLINE (e.g. American Airlines): ")
        results = get_flight_information(airline=airline,flight=flight)
    else:
        results = get_flight_information()
    # print(results)

if __name__ == "__main__":

    if APP_ENV == "development":
        f_street = input("PLEASE INPUT YOUR STREET ADDRESS: ")
        f_city = input("PLEASE INPUT YOUR CITY: ")
        f_state = input("PLEASE INPUT YOUR STATE (e.g. NY): ")
        f_zip = input("PLEASE INPUT YOUR ZIP CODE (e.g. 10012): ")
        results = get_departure_time(f_street=f_street,f_city=f_city,f_state=f_state,f_zip=f_zip,)
    else:
        results = get_departure_time()
    print(f"LEAVE AT: {results}") 