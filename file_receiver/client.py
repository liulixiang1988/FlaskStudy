#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import base64
import time


filename = '1.jpg'
num = '1'
size = 512
url = 'http://192.168.1.103:8080/api/test/%s' % num
# 秒
delay = 1
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'


def send():
    with open(filename, mode='rb') as f:
        encoding_string = base64.b64encode(f.read())

    while True:
        if len(encoding_string) > size:
            data = encoding_string[:size]
            encoding_string = encoding_string[size:]
            r = requests.get(
                url, headers={'X-Session': data, 'user-agent': useragent})
            print(r.text)
        else:
            r = requests.get(
                url, headers={'X-Session': encoding_string, 'user-agent': useragent})
            print(r.text)
            break
        time.sleep(delay)

    print('finish')


if __name__ == '__main__':
    send()
