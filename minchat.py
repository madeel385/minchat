#!/usr/bin/env python
import os
import sys
from flask import Flask ,request

app = Flask(__name__)

@app.route("/")
def HandleVerification():

    if (request.args.get('hub.mode')=="subscribe"  ):
        if(request.args.get('hub.challenge')):
            if(request.args.get('hub.verify_token')==os.environ["hook_verification"]):
                return request.args['hub.challenge']
            else :
                "not allowed!!"
        else:
            "not allowed!!"

    else:
        return "not allowed!!"

<<<<<<< HEAD
'''@app.route('/', methods=['POST'])
=======

@app.route('/', methods=['GET'])
>>>>>>> 4691cd428c32ca96e69b10033473aed8f35b2ade
def handle_incoming_messages():
    data = request.json
    sender = data['entry'][0]['messaging'][0]['sender']['id']
    message = data['entry'][0]['messaging'][0]['message']['text']
    reply(sender, message[::-1])
 
    return "ok"'''

@app.route("/", methods=['POST'])
def handle_incoming_messages():
    fbdata = request.json
    log(fbdata)
    if fbdata["object"]=="page" :
        for entry in fbdata['entry'] :
            for fbmsg in entry["messaging"]:
                if fbmsg.get("message"):
                    sender_id = fbmsg["sender"]["id"]
                    recipient = fbmsg["recipient"]["id"]
                    messag_txt = fbmsg["message"]["text"]


    return  "ok"

def log(text):
    print str(text)
    sys.stdout.flush()























if __name__ == "__main__":
    app.run(host='127.0.0.1')
