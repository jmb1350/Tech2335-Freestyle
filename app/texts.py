#texts.py
import json
import requests
import datetime
import os
from datetime import datetime
from dotenv import load_dotenv



import nexmo

client = nexmo.Client(key='6c2e943c', secret='WvVKYyYuA8bIW5qc')

client.send_message({
    'from': '13024861693',
    'to': '15165101124',
    'text': 'Time to Leave!',
})