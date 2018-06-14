#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/12 21:50
# @Author  : yangyuanqiang
# @File    : demon2.py

import requests

# post请求
url = "https://www.qiushibaike.com"
header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36"}
r = requests.get(url=url, headers=header)
print(r.request)
print(r.headers)
print(r.encoding)
print(r.cookies)
print(r.cookies.get("_xsrf"))
print(r.url)
print(r.status_code)