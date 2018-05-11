#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/14 09:15
# @Author  : yangyuanqiang
# @File    : 6.py



#6、计算从1到1000以内所有能被3或者17整除的数的和并输出 脚本名：6.py

#方法一：
sum = 0
for x in range(1,1001):
    if x % 3 == 0 or x % 17 == 0:
        sum += x
print("1到1000以内所有能被3或者17整除的数的和：{0}".format(sum))

#方法二：
summation = 0
num = 1
while num <= 1000:
    if num % 3 ==0 or num % 17 == 0:
        summation += num
        num += 1
        continue
    num += 1
print("1到1000以内所有能被3或者17整除的数的和：{0}".format(summation))
