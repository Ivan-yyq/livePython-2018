#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/14 09:25
# @Author  : yangyuanqiang
# @File    : 7.py



#7、计算1到100以内能被7或者3整除但不能同时被这两者整除的数的个数 脚本名：7.py

#方法一：
sum = 0
for x in range(1,101):
    if x % 3 == 0 or x % 7 == 0:
        if x % 21 != 0:
            sum += 1
print("1到100以内能被7或者3整除但不能同时被这两者整除的数的个数：{0}个".format(sum))

#方法二：
summations=0
for i in range(1,101):
    if (i % 3 == 0 or i % 7 == 0) and i % 21 != 0:
        summations += 1
print("1到100以内能被7或者3整除但不能同时被这两者整除的数的个数：{0}个".format(summations))


#方法三：
sum1 = 0
num = 1
while num <= 100:
    if (num % 3 == 0 or num % 7 ==0) and num % 21 != 0:
        sum1 += 1
        num += 1
        continue
    num += 1
print("1到100以内能被7或者3整除但不能同时被这两者整除的数的个数：{0}个".format(sum1))
