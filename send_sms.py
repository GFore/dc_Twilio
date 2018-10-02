import os
from twilio.rest import Client

# Twilio account info are cell numbers are stored in env variables accessed via os.environ.get()

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TKN')
client = Client(account_sid, auth_token)

msg = client.messages.create(
    to=os.environ.get('CELL_PH_NUM'),
    # to='+15551234567',            USE FOR DEMO WITH DIFFERENT CELL NUM, MUST CONFIRM IT IN TWILIO FIRST
    from_=os.environ.get('TWILIO_PH_NUM'),
    body='Respond with your sort method (A=Bubble, B=Merge, C=Selection) followed by a space, sort order (A=Ascending D=Descending) followed by a space, and then your space-separated, unsorted list of integers. I will return the list sorted.'
)

print(msg.body)