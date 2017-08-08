#!/usr/bin/env python
import os
import requests
import json
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



@app.route("/", methods=['POST'])
def handle_incoming_messages():
    fbdata = request.json

    if fbdata["object"]=="page" :
        for entry in fbdata['entry'] :
            for fbmsg in entry["messaging"]:
                if fbmsg.get("message"):
                    sender_id = fbmsg["sender"]["id"]
                    recipient = fbmsg["recipient"]["id"]
                    messag_txt = fbmsg["message"]["text"]
                    replyfb(sender_id, messag_txt)


    return  "ok"







def replyfb (user_id,msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    params = json.dump({
        "access_token": os.environ["page_verification"]
    })
    headers = {
        "Content-Type": "application/json"
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers ,data=data)
    print(resp.content)










if __name__ == "__main__":
    app.run(host='127.0.0.1')
