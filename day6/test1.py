#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/13 12:58
# @Author : yangyuanqiang
# @File : test1.py


#计算1到100以内能被7或者3整除但不能同时被这两者整除的数的个数。

for i in range(0,101):
    if i%7 == 0 or i%3 ==0:
        if i%7 != 0 or i%3!=0:
            print(i)