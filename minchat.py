#!/usr/bin/env python
import os
from flask import Flask ,request

app = Flask(__name__)

@app.route("/")
def HandleVerification():

    if (request.args['hub.mode']=="subscribe"  ):
        if(request.args['hub.challenge']):
            if(request.args['hub.verify_token']==os.environ["hook_verification"]):
                return request.args['hub.challenge']
            else :
                "not allowed!!"
        else:
            "not allowed!!"

    else:
        return "not allowed!!"





if __name__ == "__main__":
    app.run(host='127.0.0.1')