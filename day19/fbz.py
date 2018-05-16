#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 21:46
# @Author  : yangyuanqiang
# @File    : fbz.py


#导入模块
# from redis_demo.demo import RedisHelper
from day19.demo import RedisHelper
#实例化
obj = RedisHelper()
#把内容发布到频道
obj.public('python')