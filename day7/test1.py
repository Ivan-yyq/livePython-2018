#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/16 11:18
# @Author : yangyuanqiang
# @File : test1.py


def f(x):
    return x*x
#
# print(map(f, [1, 2, 3, 4]))
# print(list((map(f, [1, 2, 3, 4]))))
# for i in map(f, [1, 2, 3, 4]):
#     print(i)
def testMap(fun, iter):
    l = list()

    for i in iter:
        l.append(fun(i))
    return l
print(testMap(f, [1, 2, 3, 4]))