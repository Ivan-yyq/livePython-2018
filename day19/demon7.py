#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 21:42
# @Author  : yangyuanqiang
# @File    : demon7.py


import redis

pool = redis.ConnectionPool(host='192.168.3.20', port=6379)

r = redis.Redis(connection_pool=pool)

# pipe = r.pipeline(transaction=False)
pipe = r.pipeline(transaction=True)

r.set('name', 'python')
r.set('age', '18')

pipe.execute()