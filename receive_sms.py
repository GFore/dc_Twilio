import os
from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

def bubblesort(nlist, descending):

    if descending:
        end_pos = len(nlist)-1

        while end_pos > 0:
            for i in range(end_pos):
                if nlist[i] < nlist[i+1]:  # then swap them
                    nlist[i], nlist[i+1] = nlist[i+1], nlist[i]
                #print(num_list, end_pos)
            end_pos -= 1
    else:
        end_pos = len(nlist)-1

        while end_pos > 0:
            for i in range(end_pos):
                if nlist[i] > nlist[i+1]:  # then swap them
                    nlist[i], nlist[i+1] = nlist[i+1], nlist[i]
                #print(num_list, end_pos)
                
            end_pos -= 1

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

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    resp = MessagingResponse()      #starts the TwiML response
    #resp.message("The robots are coming! Head for the hills!")  #customize this per received msg

    message_body = request.form['Body']
    message_body = message_body.strip().split()
    desc = message_body[1] == 'D'
    msg = []
    for i in range(2, len(message_body)):
        msg.append(int(message_body[i]))

    bubblesort(msg, desc)
    
    reply_msg = []
    for i in msg:
        reply_msg.append(str(i))
    
    # resp.message(' '.join(message_body[2:]))
    resp.message(' '.join(reply_msg))
    print("Your list:", msg)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)