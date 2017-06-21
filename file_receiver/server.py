#!/usr/bin/env python
# -*- coding:utf-8 -*-

import base64
from flask import Flask, request

app = Flask(__name__)


@app.route('/api/test')
def hello():
    return "hello"


@app.route('/api/test/<name>')
def test(name):
    data = request.headers.get('X-Session')
    with open(name, mode='a+', encoding='utf-8') as file:
        file.write(data)
    return "hello"


@app.route('/api/bin/<name>/<real_name>')
def convert(name, real_name):
    with open(name, 'rb') as file_origin,\
            open(real_name, 'wb') as file_real:
        decoded_data = base64.b64decode(file_origin.read())
        file_real.write(decoded_data)
    return "convert ok"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
