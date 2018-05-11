#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/13 16:10
# @Author : yangyuanqiang
# @File : test3.py

#  输出10行内容，每行的内容都不一样，第1行一个星号，第2行2个星号，依此类推第10行10个星号。

# for i in range(1,11):
#     print("*"*i)
for i in range(1,11):
    print("*"*(11-i))


# list = [0,1,2,3,4,5,6,7,8,9]
# for i in list:
#     for j in list:
#         print("*", end="")
#         if j==i:
#             break
#     print("")
#     if i==9:
#         break