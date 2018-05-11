#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/14 08:55
# @Author  : yangyuanqiang
# @File    : 5.py


#5、输出10行内容，每行的内容都不一样，第1行一个星号，第2行2个星号，依此类推第10行10个星号，倒序显示  脚本名：5.py

#方法一：
print("方法一：")
for i in range(1,11):
    print("*" * (11 - i))


#方法二：
print("方法二：")
for x in range(1,11):
    for y in range(1,11):
        print("*", end="")
        if y == x:
            break
    print("")
    if x == 10:
        break

