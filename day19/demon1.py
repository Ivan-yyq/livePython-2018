#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 20:35
# @Author  : yangyuanqiang
# @File    : demon1.py



import redis

#创建redis链接对象
r = redis.Redis(host='192.168.3.20',port=6379,decode_responses=True)
#存储键值对
r.set('site','www.qi.cn')
#获取值
print(r.get('site'))
#指定decode_responses为True，表示输出为字符串
red = redis.StrictRedis(host='192.168.3.20',port=6379,decode_responses=True)

#默认redis入库编码是utf-8，如果要修改的话，需要指明 charset 和 decode_responsers 为True
#test = redis.StrictRedis(host='localhost', port=6379, db=0, password=None, socket_timeout=None, connection_pool=None, charset='utf-8', errors='strict', decode_responses=False, unix_socket_path=None)

red.lpush('list1','mongdb','redis','mysql')
print(r.lrange('list1',0, -1))
print(r.llen('list1'))