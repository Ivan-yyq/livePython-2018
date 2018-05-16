#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 20:45
# @Author  : yangyuanqiang
# @File    : demon3.py

# string操作

# import redis
# #创建连接池
# pool = redis.ConnectionPool(host='192.168.3.20',port=6379,decode_responses=True)
# #创建链接对象
# r=redis.Redis(connection_pool=pool)
# r.set('test','dddddddddddd',ex=3,nx=True)
# print(r.get('test'))


# import redis
# #创建连接池
# pool = redis.ConnectionPool(host='192.168.3.20',port=6379,decode_responses=True)
# #创建链接对象
# r=redis.Redis(connection_pool=pool)
# r.set('test','12345',nx=True)
# r.setrange('test',0,'8888')
# print(r.get('test'))



# import redis
# r=redis.Redis(host='192.168.3.20',port=6379,decode_responses=True)
# r.set('name','p')
# print(r.get('name'))
# #打印p,q对应的ascii码
# print(ord('p'),ord('q'))
# #打印ascii码对应的二进制
# print(bin(ord('p')),bin(ord('q')))
# print('修改前7位的值：',r.getbit('name','7'))
# #设置二进制位的第7位为1，相当于移动ascii码位112为113对应的字符为q
# r.setbit('name','7','1')
# print('修改后7位的值：',r.getbit('name','7'))
# print(r.get('name'))


# import redis
# r= redis.Redis(host='192.168.3.20',port=6379,decode_responses=True)
# r.set('age','10')
# print(r.get('age'))
# print(r.append('age','11'))
# print(r.get('age'))