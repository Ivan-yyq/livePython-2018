#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/18 10:39
# @Author : yangyuanqiang
# @File : 10.py


#10、计算从1加到100的值并输出   脚本名：10.py

#for循环：
# print("for循环方法一：")
# sum = 1
# for i in range(1,100):
#     i += 1
#     sum = sum + i
# print(sum)


#for循环：
# print("for循环方法二：")
# a = 0
# for i in range(0,100):
#     a += (i+1)
# print(a)


#while循环：
# print("while循环方法一：")
# def sum():
#     sum = 0
#     x = 1
#     while x < 101:
#         sum = sum + x
#         x += 1
#     return sum
# print(sum())


#导入模块的内建函数reduce
print("导入模块的内建函数reduce方法一：")
def sum(x, y):
    return x + y
from functools import reduce
print(reduce(sum, range(1,101)))