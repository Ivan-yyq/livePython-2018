#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/4 11:39
# @Author : yangyuanqiang
# @File : 1到100求和.py


number = 100
sum = 0
count = 1
while count <= number:
    sum = sum + count
    count += 1
print("1 到 %d 之和为：%d" %(number, sum))