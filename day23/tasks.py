#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/26 10:31
# @Author  : yangyuanqiang
# @File    : tasks.py

#多worker，多队列

from celery import Celery

app = Celery()
app.config_from_object("celeryconfig")

@app.task
def taskA(x,y):
    return x + y

@app.task
def taskB(x,y,z):
    return x + y + z


@app.task
def add(x,y,z):
    return x * y * z












