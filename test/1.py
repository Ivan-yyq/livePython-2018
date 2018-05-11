#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/13 23:01
# @Author  : yangyuanqiang
# @File    : 1.py


#1、对100以内的两位数，请使用for循环打印出所有十位数数字比个位数数字小的数，例如，23（2 < 3）   脚本名：1.py

count = 0
for i in [1,2,3,4,5,6,7,8,9]:
    for j in [0,1,2,3,4,5,6,7,8,9]:
        if i < j:
            count += 1
            print("第{0}个，十位数数字比个位数数字小的数有：{1}".format(count, i * 10 + j))
print("十位数数字比个位数数字小的数总共有：{0}个".format(count))