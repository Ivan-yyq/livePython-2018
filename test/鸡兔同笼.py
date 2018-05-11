#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/17 15:28
# @Author : lingxiangxiang
# @File : 鸡兔同笼.py

# 三十五头，下有九十四足，计算鸡和兔分别有多少只

# for循环方法
print("方法一：")
for ji in range(1,36):
    for tu in range(1,36):
        if (2*ji+4*tu==94)and(ji+tu==35):
            print("鸡有{0}只，兔有{1}只".format(ji, tu))
            tu+=1
    ji+=1

#函数方法
print("方法二：")
def sum(t, j):
    for ji in range(1,t):
        for tu in range(1,t):
            if (2*ji+4*tu==j)and(ji+tu==t):
                print("鸡有{0}只，兔有{1}只".format(ji, tu))
                tu+=1
        ji+=1

sum(35, 94)


# 最简单的方法
print("方法三：")
for a in range(1,35):
    if (2*a+(35-a)*4)==94:
        print("鸡有{0}只，兔有{1}只".format(a, 35-a))


# 使用numpy模块方法
import numpy as np
a=[[1,1],[2,4]]
a= np.array(a)
b = [35,94]
b = np.array(b)
print(np.linalg.solve(a,b))