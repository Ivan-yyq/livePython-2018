#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 20:35
# @Author  : yangyuanqiang
# @File    : demon2.py



import redis
#创建连接池
pool = redis.ConnectionPool(host='192.168.3.20',port=6379,decode_responses=True)
#创建链接对象
r=redis.Redis(connection_pool=pool)
#设置集合
r.sadd('set1','v1','v2','v3')
r.sadd('set1','v2')
#显示集合的值
print(r.smembers('set1'))

#使用strictRedis连接池
rs = redis.StrictRedis(connection_pool=pool)
r.lpush('l1','python','memcache','redis','mongodb')
print(r.lrange('l1',0,-1))