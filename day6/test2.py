#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/13 13:55
# @Author : yangyuanqiang
# @File : test2.py

# 计算从1到1000以内所有能被3或者17整除的数的和并输出

sum = 0
for i in range(1,1001):
    if i%3==0 or i%17==0:
        # print("{0} + {1} = {2}".format(i, sum, sum+i ))
        sum = sum + i
        # print("1到1000以内能被3或者17整除的数：{0}".format(i))
print("1到1000以内能被3或者17整除的数总和：{0}".format(sum))