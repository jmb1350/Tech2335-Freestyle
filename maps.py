import os
import json
import requests
from dotenv import load_dotenv
import datetime
from datetime import timedelta

load_dotenv()

MAPS_KEY = os.environ.get("MAPQUEST_API")

#TODO: Pull from user input
f_street = "2175 E 15 St"
f_city = "Brooklyn" 
f_state = "NY"
f_zip = "11229"

#TODO: Pull from aviationstack
t_street = "LaGuardia Airport"
t_city = "Queens" 
t_state = "NY"
t_zip = "11371"

#TODO: Pull this from aviationstack
flight_arrival = "2020-06-30T08:00"

request_url = f"http://www.mapquestapi.com/directions/v2/optimizedroute?key={MAPS_KEY}&from={f_street},+{f_city},+{f_state},+{f_zip}&to={t_street},+{t_city},+{t_state},+{t_zip}&timeType=3&isoLocal={flight_arrival}"

response = requests.get(request_url)
response_data = json.loads(response.text)
print(response.status_code)

travel_time = (response_data['route']['realTime'])
departure_time = datetime.datetime.fromisoformat(flight_arrival) - datetime.timedelta(seconds = travel_time)
d_time = departure_time.strftime("%B %d, %I:%M:%S %p")
print(f"LEAVE AT: {str(d_time)}")