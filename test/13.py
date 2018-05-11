#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/18 11:55
# @Author : yangyuanqiang
# @File : 13.py


#13、利用while True无限循环配合 break 语句，计算 1 + 2 + 4 + 8 + 16 + .....的前20个数的和    脚本名：13.py

sum = 0
a = 1
b = 1
while 1:
    if a <= 20:
        a += 1
        sum = sum + b
        b *= 2
    else:
        break
print("方法一：{0}".format(sum))


sum1 = 0
x = 1
y = 1
while 1:
    if x > 20:
        break
    x += 1
    sum1 = sum1 + y
    y *= 2
print("方法二：{0}".format(sum1))