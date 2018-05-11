#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/13 23:11
# @Author  : yangyuanqiang
# @File    : 2.py


#2、利用while True 无限循环配置break语句，计算1 + 2 + 4 + 8 + 16 + ... 的前20项的和     脚本名：2.py

#方法一：
sum = 0
x = 1
y = 1
while 1:
    if x <= 20:
        x += 1
        sum = sum + y
        y *= 2
    else:
        break
print("方法一：{0}".format(sum))


#方法二：
sum1 = 0
a = 1
b = 1
while 1:
    if a >20:
        break
    a += 1
    sum1 = sum1 + b
    b *= 2
print("方法二：{0}".format(sum1))