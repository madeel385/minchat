#!/usr/bin/env python

from flask import Flask ,request

app = Flask(__name__)

@app.route("/")
def HandleVerification():


    return request.args['hub.challenge']





if __name__ == "__main__":
    app.run(host='127.0.0.1')