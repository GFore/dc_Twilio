import os
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
#from sorter import bubblesort
def bubblesort(nlist, descending):

    if descending:
        end_pos = len(nlist)-1

        while end_pos > 1:
            for i in range(end_pos):
                if nlist[i] < nlist[i+1]:  # then swap them
                    nlist[i], nlist[i+1] = nlist[i+1], nlist[i]
                #print(num_list, end_pos)
            end_pos -= 1
    else:
        end_pos = len(nlist)-1

        while end_pos > 1:
            for i in range(end_pos):
                if nlist[i] > nlist[i+1]:  # then swap them
                    nlist[i], nlist[i+1] = nlist[i+1], nlist[i]
                #print(num_list, end_pos)
                
            end_pos -= 1


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