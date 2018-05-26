#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/24 22:31
# @Author  : yangyuanqiang
# @File    : ivan.py
import time

from celery import Celery
import redis

broker = "redis://192.168.3.11:6379/5"
backend = "redis://192.168.3.11:6379/6"
app = Celery("ivan", broker=broker, backend=backend)

@app.task
def add(x, y):
        time.sleep(5)
        return x+y
