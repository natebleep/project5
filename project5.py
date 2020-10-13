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

@app.route('/md5/')
def md5_response():
    word = input('Input: ')
    resp = hashlib.md5(word)
    return "Output: {resp}"

@app.route('/factorial/')
def factorial_response(resp = 'result'):
    num = int(input('Input a number to compute the factorial: '))
    resp = math.factorial(num)
    return f'Output: {resp}'

@app.route('/fibonacci/')
def fibonacci_response(resp = 'result'):
    num = input('Input: ')
    fib_list = []
    
    fib1 = 0
    fib2 = 1
    fib3 = 1

    while fib1 <= num:
        fib_list.append(fib1)
        fib1 = fib2
        fib2 = fib3
        fib3 = fib1 + fib2
        return f'Output: {fib_list}'


@app.route('/is-prime/')
def isprime_response(resp = 'Input'):
        num = int(input('Input: '))
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return f'{num} is not a prime number'
                    break
            else:
                return f'{num} is a prime number'
        else:
            return f'{num} is not a prime number'
         

'''@app.route('/slack-alert/')
def slack_alert_response():
    resp =
'''

# Run  this flask server if file is called directly
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
