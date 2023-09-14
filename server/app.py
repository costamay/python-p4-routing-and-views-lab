#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    result = ''
    for i in range(parameter):
        result += f'{i}\n'
    print('yyyyyyyyyyyyyyyyyyy')
    print(type(result))
    return result 

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    
    result = None

    if operation == '+':
        result = str(num1 + num2)
    elif operation == '-':
        result = str(num1 - num2)
    elif operation == '*':
        result = str(num1 * num2)
    elif operation == 'div':
        result = str(num1 / num2)
    elif operation == '%':
        result = str(num1 % num2)
    else:
        result = "Invalid operation"

    return result
if __name__ == '__main__':
    app.run(port=5555, debug=True)
