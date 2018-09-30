import os
from twilio.rest import Client

account_sid = os.environ.get('TWILIO_ACCT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TKN')
client = Client(account_sid, auth_token)

msg = client.messages.create(
    to=os.environ.get('CELL_PH_NUM'),
    from_=os.environ.get('TWILIO_PH_NUM'),
    body='Please respond with your sort method (A=Bubble, B=Merge, C=Selection) followed by a space and then your space-separated, unsorted list of integers to be sorted.'
)

print(msg.body)