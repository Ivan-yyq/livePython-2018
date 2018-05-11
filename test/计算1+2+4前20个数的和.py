#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/11 17:15
# @Author : yangyuanqiang
# @File : test2.py

'''

利用while True无限循环配合 break 语句，计算 1 + 2 + 4 + 8 + 16 + .....的前20个数的和

'''
# 方法一：
sum = 0
x = 1
n = 1
while 1:
    if x<=20:
        # print(x)
        x += 1
        sum = sum + n
        n *= 2
    else:
        break
print("方法一：{0}".format(sum))

#方法二：
sum1 = 0
a = 1
b = 1
while 1:
    if a>20:
        break
    a += 1
    # print(a)
    sum1 = sum1 + b
    b *= 2
print("方法二：{0}".format(sum1))