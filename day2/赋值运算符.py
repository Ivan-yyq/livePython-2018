#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/3/30 14:30
# @Author : yangyuanqiang
# @File : 3.py
# Python赋值运算符

a = 21
b = 10
c = 0

c = a + b
print("1 - c 的值为：", c)

c += a
print("2 - c 的值为：", c)

c *= a
print("3 - c 的值为：", c)

c /= a
print("4 - c 的值为：", c)

c = 2
c %= a
print("5 - c 的值为：", c)

c **= a
print("6 - c 的值为：", c)

c //= a
print("7 - c 的值为：", c)