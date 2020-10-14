from flask import Flask, jsonify, escape, request, Response
from hashlib import md5
import requests
import json
from math import factorial

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
def md5_response(string):
    hash1 = md5(string.encode())
    hash2 = hash1.hexdigest()
    return jsonify(
        input = string,
        hash = hash2
    )

@app.route('/factorial/<int:num>')
def factorial_response(num):
    if num < 0:
        fac = "Error: Input must be a positive integer"
    else:
        fac = factorial(int(num))
    return jsonify(
        input = num,
        factorial = fac
    )

@app.route('/fibonacci/<int:n>')
def fibonacci_response(n):
    a = 0
    b = 1
    c = 0
    fib = [a,b]
    if n <= 0:
        print("Incorrect input")
    elif n == 1:
        return b
    else:       
        while c < n:                       
            c = a + b            
            a = b
            if c < n:
                b = c
                fib.append(c)
            else:
                continue
        return jsonify(
            input = n,
            fibonacci = fib
        )


@app.route('/is-prime/<int:num>')
def isprime_response(num):        
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    isprime = False
                    break
            else:
                isprime = True
        else:
            isprime = False
        return jsonify(
            input = num,
            isprime = isprime
        )
         

@app.route('/slack/<msg>')
def slack_post(msg):
    web_hook_url = 'https://hooks.slack.com/services/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'
    slck_msg = {'text': msg}
    requests.post(web_hook_url,data=json.dumps(slck_msg))
    return 'Done'

# Run  this flask server if file is called directly
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
