#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 21:47
# @Author  : yangyuanqiang
# @File    : dyz.py


# from redis_demo.demo import RedisHelper
from day19.demo import RedisHelper

obj = RedisHelper()
redis_sub = obj.subscribe()

while True:
    msg = redis_sub.parse_response()
    print(msg)
    print(type(msg))