#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 21:44
# @Author  : yangyuanqiang
# @File    : demo.py


import redis


class RedisHelper:
    '''类'''

    def __init__(self):
        # 链接
        self.__conn = redis.Redis(host='192.168.3.20')
        self.chan_sub = 'fm104.5'
        # 创建频道
        self.chan_pub = 'fm104.5'

    def public(self, info):
        '''公共的'''
        self.__conn.publish(self.chan_pub, info)
        '''将内容发布到频道'''
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub