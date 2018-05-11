#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/14 19:52
# @Author  : yangyuanqiang
# @File    : demon11.py


# 申明一个函数，第一个参数是整型，第二个参数是list类型
# l 有一个默认值，默认值为[]空列表

def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)


# f(2) = f(2, l=[])

f(2)
f(3,[3,2,1])
f(3)