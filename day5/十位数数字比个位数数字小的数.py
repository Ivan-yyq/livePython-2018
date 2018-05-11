#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/11 16:34
# @Author : yangyuanqiang
# @File : 十位数数字比个位数数字小的数.py

'''

对100以内的两位数，请使用一个两重循环打印出所有十位数数字比个位数数字小的数，例如，23（2 < 3）。

'''

count = 0
for x in [1,2,3,4,5,6,7,8,9]:
    for y in [0,1,2,3,4,5,6,7,8,9]:
        if x < y :
            count += 1
            print("第{0}个数：{1}".format(count, x * 10 + y))
print("十位数数字比个位数数字小的数总数有：{0} 个".format(count))