#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 21:37
# @Author  : yangyuanqiang
# @File    : demon6.py


# set操作


# import redis
# r = redis.Redis(host='192.168.3.20',port=6379,decode_responses=True)
# r.sadd('s1',1,2,3)
# r.sadd('s2',4,5,2)
# r.sadd('s3',7,8,1)
# print(r.sdiff('s1','s2','s3'))


# import redis
# r = redis.Redis(host='192.168.3.20',port=6379,decode_responses=True)
# # r.sadd('s1',1,2,3)
# # r.sadd('s2',4,5,2)
# # r.sadd('s3',7,8,1)
# print(r.sdiffstore('s4','s1','s2','s3'))
# print(r.smembers('s4'))


# import redis
# r = redis.Redis(host='192.168.3.20',port=6379,decode_responses=True)
# r.sadd('s1',1,2,3)
# r.sadd('s2',4,5,2)
# print(r.sinter('s1','s2'))



# import redis
# r = redis.Redis(host='192.168.3.20',port=6379,decode_responses=True)
# r.sadd('sex1',1,2,3,4)
# r.sadd('sex2',4,5,2,7)
# r.sadd('sex3',7,8,1,4,2)
# r.sinterstore('sex4','sex1','sex2','sex3')
# print(r.smembers('sex4'))


import redis
r = redis.Redis(host='192.168.3.20',port=6379,decode_responses=True)
r.sadd('sex3',7,8,1,4,2)
print(r.sismember('sex3','8'))