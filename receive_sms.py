import os
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    resp = MessagingResponse()      #starts the TwiML response
    #resp.message("The robots are coming! Head for the hills!")  #customize this per received msg

    message_body = request.form['Body']
    message_body = message_body.strip()
    # if message_body == "yes":
    #     resp.message("You said yes.")
    # elif message_body == "no":
    #     resp.message("You said no.")
    # else:
    message_body = "You said: " + message_body
    resp.message(message_body)
    print("You said:", message_body)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)