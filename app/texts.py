#Send the User a Reminder Email


import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
MY_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")

client = SendGridAPIClient(SENDGRID_API_KEY)
print("CLIENT:", type(client))
send_at=

subject = "Your flight is arriving soon!"

html_content = "Almost time to leave!"
print("HTML:", html_content)

message = Mail(from_email=MY_ADDRESS, to_emails=MY_ADDRESS, subject=subject, html_content=html_content)

try:
    response = client.send(message)

    print("RESPONSE:", type(response)) 
    print(response.status_code) 
    print(response.body)
    print(response.headers)

except Exception as e:
    print("OOPS", e.message)










#3import sendgrid
import os

#sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
#data = {
#  "personalizations": [
#    
#    {
#      "to": [
#        {
#          "email": "test@example.com"
#        }
#      ],
#      "subject": "Sending with SendGrid is Fun"
#    }
#  ],
#  "from": {
#    "email": "test@example.com"
#  },
#  "content": [
#    {
#      "type": "text/plain",
#      "value": "and easy to do anywhere, even with Python"
#    }
#  ]
#}
#response = sg.client.mail.send.post(request_body=data)
#print(response.status_code)
#print(response.body)
#print(response.headers)