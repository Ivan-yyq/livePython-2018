#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 20:59
# @Author  : yangyuanqiang
# @File    : demon5.py


# list操作

# import redis
# r = redis.Redis(host='192.168.3.20',port=6379,decode_responses=True)
# r.lpush('l3',1,2)
# print(r.lrange('l3',0,-1))
# r.lpush('l3','88')
# print(r.lrange('l3',0,-1))


# import redis
# r = redis.Redis(host='192.168.3.20',port=6379,decode_responses=True)
# r.lpushx('l4',1)
# print(r.lrange('l4',0,-1))
# r.lpush('l4',2)
# r.lpushx('l4',1)
# print(r.lrange('l4',0,-1))


# import redis
# r = redis.Redis(host='192.168.3.20',port=6379,decode_responses=True)
# r.lpush('num','1','2')
# r.linsert('num','after','2','python')#在2后面添加python元素值
# r.linsert('num','before','1','redis') #在1之前插入redis
# print(r.lrange('num',0,-1))


# import redis
# r = redis.Redis(host='192.168.3.20',port=6379,decode_responses=True)
# print(r.lrange('num',0,-1))
# r.lset('num','0','hello')
# print(r.lrange('num',0,-1))


import redis
r = redis.Redis(host='192.168.3.20',port=6379,decode_responses=True)
print(r.lrange('num',0,-1))
r.lrem('num','1','2')   #2为num指定的值的个数,可以指定-2从后往前删除
print(r.lrange('num',0,-1))