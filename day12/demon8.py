#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/29 23:55
# @Author  : yangyuanqiang
# @File    : demon8.py
import codecs
ENCODING = "utf-8"

with codecs.open("1.txt", "r", encoding=ENCODING) as f:
    print(f.read())


a = lambda x: x*x
print(a)
print([x for x in range(1, 10) if x%2==0])

def startEnd(fun):
    def wrap(name):
        print("start")
        fun(name)
        print("end")
    return wrap



@startEnd
def hello(name):
    print("hello {0}".format(name))

hello("ajing")