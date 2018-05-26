#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/24 22:10
# @Author  : yangyuanqiang
# @File    : demon4.py
'''
pip install redis
pip install celery

安装redis，启动redis

'''
import time

from ivan import add
re = add.delay(10, 20)
print(re.task_id)
print(re)   #传入ID
print(re.status)    #是否处理
time.sleep(8)
print(re.status)    #是否处理
print(re.get(timeout=1))    #获取结果
print(re.result)    #获取结果
