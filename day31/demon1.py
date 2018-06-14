#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/12 21:03
# @Author  : yangyuanqiang
# @File    : demon1.py


import requests

# get请求
# wd = "python"
# url = "http://www.baidu.com/s?wd={0}".format(wd)
# r = requests.get(url)
# r.encoding = "utf-8"
# html = r.text
# print(html)


wd = "python"
params = {"wd": "hello"}
url = "http://www.baidu.com/s"
r = requests.get(url=url, params=params)
r.encoding = "utf-8"
print(r.url)
html = r.text
# print(html)
