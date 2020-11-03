from flask import Flask, jsonify, escape, request, Response
from hashlib import md5
import requests
import json
from math import factorial
import redis

red = redis.Redis(host="redis-server")

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

@app.route('/keyval/<n>', methods=["GET"])
def get_val(n):
    value = str(red.get(n))
    if n in red:                
        return jsonify(kv_key=n,
            kv_value=value[2:-1],
            command=('READ '+n),
            result=True,
            error=None), 200
    else:
        return jsonify(kv_key=n,
            kv_value=None,
            command=('READ '+n),
            result=False,
            error=True), 400        
 
@app.route('/keyval', methods=["POST"])
def add_data():
    post = request.get_json()
    res = list(post.keys())
    values = list(post.values())
    n = 0
    x = None
    status = 200    
    for i in res:
        if res[n] in red:   
            n += 1
            x = True
            status = 409             
        else:
            red.set(res[n], post[res[n]])
            n += 1
            status = 200
    return jsonify(kv_key=res,
        kv_value=values,
        command=('CREATE '+str(res)),
        result=True,
        error=x), status

@app.route('/keyval', methods=["PUT"])
def update_data():
    post = request.get_json()
    res = list(post.keys())
    values = list(post.values())
    n = 0
    x = None
    status = 200    
    for i in res:
        if res[n] in red:
            red.set(res[n], post[res[n]])   
            n += 1            
        else:
            x = True
            status = 404
            continue
    return jsonify(kv_key=res,
        kv_value=values,
        command=('UPDATE '+str(res)),
        result=True,
        error=x), status   

@app.route('/keyval/<n>', methods=["DELETE"])
def delete_data(n):
    value = str(red.get(n))
    if n in red:        
        red.delete(n)
        return jsonify(kv_key=n,
            kv_value=value[2:-1],
            command=('DELETE '+n),
            result=True,
            error='')
    else:
        return jsonify(kv_key=n,
            kv_value=None,
            command=('DELETE '+n),
            result=False,
            error=True), 404          


# Run  this flask server if file is called directly
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
