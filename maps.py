import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

MAPS_KEY = os.environ.get("GOOGLE_API")

request_url = f"https://maps.googleapis.com/maps/api/directions/json?origin=Disneyland&destination=Universal+Studios+Hollywood&key={MAPS_KEY}"

response = requests.get(request_url)
response_data = json.loads(response.text)
print(response_data)
# print(response.status_code)
# print(response.text)
