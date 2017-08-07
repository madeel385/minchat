#!/usr/bin/env python

from flask import Flask ,request

app = Flask(__name__)

@app.route("/")
def index():
    return "request method %s" % request.method


@app.route("/adi",methods=['POST'])
def adi():
    return "request method "

@app.route("/user/<username>")
def user(username):
    return '<h2>hello %s</h2>' % username

@app.route("/post/<int:postid>")
def post_id(postid):
    return '<h2>your post id is  %s</h2>' % postid



if __name__ == "__main__":
    app.run(host='127.0.0.1')