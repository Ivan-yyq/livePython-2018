#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 20:53
# @Author  : yangyuanqiang
# @File    : demon4.py


# hash操作

# import redis
# r= redis.Redis(host='192.168.3.20',port=6379,decode_responses=True)
# r.hset('haset','python','3.5')
# print(r.hget('haset','python'))
# r.hset('haset','redis','1.8')
# print(r.hgetall('haset'))


# import redis
# r= redis.Redis(host='192.168.3.20',port=6379,decode_responses=True)
# r.hmset('hashmore',{'k1':'v1','k2':'v2','k3':'v3'})
# print(r.hmget('hashmore','k1','k2','k3'))
# print(r.hgetall('hashmore'))


# import redis
# r= redis.Redis(host='192.168.3.20',port=6379,decode_responses=True)
# r.hmset('hashmore',{'k1':'v1','k2':'v2','k3':'v3'})
# print(r.hmget('hashmore','k1','k2','k3'))
# print(r.hgetall('hashmore'))
# print(r.hexists('hashmore','k2'))
# print(r.hexists('hashmore','k4'))


# import redis
# r= redis.Redis(host='192。168.3.20',port=6379,decode_responses=True)
# r.hmset('hashmore',{'k1':'v1','k2':'v2','k3':'v3'})
# print(r.hgetall('hashmore'))
# print(r.hdel('hashmore','k3'))
# print(r.hgetall('hashmore'))



# import redis
# r= redis.Redis(host='192.168.3.20',port=6379,decode_responses=True)
# r.hmset('hashmore',{'k1':'1','k2':'2','k3':'3'})
# print(r.hgetall('hashmore'))
# r.hincrby('hashmore','k1','2')
# print(r.hgetall('hashmore'))


# import redis
# r= redis.Redis(host='192.168.3.20',port=6379,decode_responses=True)
# r.hmset('hashmore',{'k1':'1','k2':'2','k3':'3','k4':'4'})
# print(r.hgetall('hashmore'))
# print(r.hscan('hashmore',cursor=2,match='k2',count=1))
# print(r.hscan('hashmore',count=4))


import redis
r= redis.Redis(host='192.168.3.20',port=6379,decode_responses=True)
r.hmset('hashmore',
{'k1':'1','k2':'2','k3':'3','k4':'4','k5':'5','k6':'6','k7':'7','k8':'8'})
oo = r.hscan_iter('hashmore')
print(next(oo))
print(next(oo))
print(next(oo))
print(next(oo))