#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/11 13:41
# @Author : yangyuanqiang
# @File : 9801.py


'''

ABCD乘9=DCBA，A=? B=? C=? D=? 答案：a=1,b=0,c=8，d=9      1089*9=9801

'''
import datetime
import time

t1 = time.time()   # 当前时间转换为时间戳
print("版本一启动时间：{0}".format(t1))

for A in [1]:
# for A in range(1,10):
    for B in range(0, 10):
        for C in range(0, 10):
            for D in [9]:
            # for D in range(1,10):
                if ((1000* A + 100*B + 10*C + D)*9 == 1000*D + 100*C + 10*B + A ):
                    print("A = {0}".format(A))
                    print("B = {0}".format(B))
                    print("C = {0}".format(C))
                    print("D = {0}".format(D))
                    print("{0}{1}{2}{3}x9={3}{2}{1}{0}".format(A, B, C, D))
t2 = time.time()   # 当前时间转换为时间戳
print("版本一结束时间：{0}".format(t2))
print("版本一运行效率：{0}".format(t2 - t1))