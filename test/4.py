#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/13 23:20
# @Author  : yangyuanqiang
# @File    : 4.py


#4、输出10行内容，每行的内容都不一样，第1行一个星号，第2行2个星号，依此类推第10行10个星号   脚本名：4.py

#方法一：
print("方法一：")
for i in range(1,11):
    print("*" * i)

#方法二：
print("方法二：")
sum = [0,1,2,3,4,5,6,7,8,9]
for x in sum:
    for j in sum:
        print("*", end="")
        if j == x:
            break
    print("")
    if x == 9:
        break


#方法三：
print("方法三：")
orw = 0
while orw < 10:
    number = 0
    while number <= orw:
        print("*", end="")
        number += 1
    print()
    orw += 1