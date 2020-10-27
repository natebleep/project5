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

@app.route('/md5/<string>')
def md5_response(string):
    hash1 = md5(string.encode())
    hash2 = hash1.hexdigest()
    return jsonify(
        input = string,
        output = hash2
    )

@app.route('/factorial/<int:num>')
def factorial_response(num):
    if num < 0:
        fac = "Error: Input must be a positive integer"
    else:
        fac = factorial(int(num))
    return jsonify(
        input = num,
        output = fac
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
        while c <= n:                       
            c = a + b            
            a = b
            if c <= n:
                b = c
                fib.append(c)
            else:
                continue
        return jsonify(
            input = n,
            output = fib
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
            output = isprime
        )
         

@app.route('/slack-alert/<msg>')
def slack_post(msg):
    web_hook_url = 'https://hooks.slack.com/services/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'
    slck_msg = {'text': msg}
    requests.post(web_hook_url,data=json.dumps(slck_msg))
    return jsonify(
        input = msg,
        output = True
    )

@app.route('/keyval', methods = ['POST', 'PUT'])
def kv_upsert():
    json = jsonresponse(command = 'CREATE' if request.method == 'POST' else 'UPDATE')
    #Check for valid JSON payload
    try:
        payload = request.get_json()
        json.key = payload['key']
        json.value = payload['value']
        json.command += f" {payload['key']}/{payload['value']}"
    except:
        json.error = 'Missing or malformed JSON in the client request.'
        return jsonify(json), 400
    #Attempt to connect to redis
    try:
        test_value = redis.get(json.key)
    except RedisError:
        json.error = 'Cannot connect to redis'
        return jsonify(json), 400
    #POST == create only
    if request.method == 'POST' and not test_value == None:
        json.error = 'Cannot create a new record: key already exists.'
        return jsonify(json), 409
    #PUT == update


    #JSON payload returns 5 values


    #Attempt to connect to redis again
    try:
        test_value = redis.get(key)
    except RedisError:
        _JSON['error'] = 'Cannot connect to redis.'
        return jsonify(_JSON), 400
    #Cannot delete or retrieve if value doesn't exist
    if test_value == None:
        _JSON['error'] = 'Key does not exist.'
        return jsonify(_JSON), 404
    else:
        #Use value from test and decode the byte string to unicode
        _JSON['value'] = test_value.decode('unicode-escape')
    #GET == retrieve
    if request.method == 'GET':
        _JSON['result'] = True
        return jsonify(_JSON), 200
    #DELETE == delete
    elif request.method == 'DELETE':
        ret = redis.delete(key)
        if ret == 1:
            _JSON['result'] = True
            return jsonify(_JSON)
        else:
            _JSON['error'] = f'Not able to delete key (expected return value 1; client returned {ret})'
            return jsonify(_JSON), 400

# Run  this flask server if file is called directly
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
