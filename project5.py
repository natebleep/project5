from flask import Flask, jsonify, escape, request, Response
import random
import hashlib
import math

# instansiate the Flask object
app = Flask(__name__)

# the main route url route
@app.route('/')
def hello():
    return "Hello, Welcome to group project #5."

''' example
@app.route('/md5/<string>')
def json_response():
    resp = Response('{ "foo": "bar", "baz": "bat" }')
    resp.headers['Content-Type'] = 'application/json'
    return resp
'''

@app.route('/md5/<string>')
def md5_response():
    resp = hashlib.md5(<string>)
    return resp

@app.route('/factoral/<int>')
def factoral_response():
    resp = math.factoral(<int>)
    return resp

@app.route('/fibonacci/<int>')
def fibonacci_response():
    resp = 

@app.route('/is-prime/<int>')
def prime_response():
    resp = 

@app.route('/slack-alert/<string>')
def slack_alert_response():
    resp =

# show a random cat gif
''' @app.route('/cat')
def random_cat():
    gif = random.random(0, 11)
    image_path = f"https://storage.googleapis.com/tcmg-gifs/{gif}.gif"
    return f"<html><img src='{image_path}' /></html'>"
'''

# Run  this flask server if file is called directly
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

