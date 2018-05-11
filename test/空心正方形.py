#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/16 11:34
# @Author : yangyuanqiang
# @File : 空心正方形.py

# 空心正方形
print("空心正方形")
for i in range(5):
    for j in range(5):
        if i == 0 or i == 4:
            print(" * ", end="")
        elif j == 0 or j == 4:
            print(" * ", end="")
        else:
            print("   ", end="")
    print(" ")


# 实心正方形
print("实心正方形")
for a in range(5):
    for b in range(4):
        print(" * ", end="")
    print(" * ")


# 空心三角形
print("空心三角形")
for x in range(6):
    for y in range(6):
        if x == 5:
            print(" * ", end="")
        elif y == 0:
            print(" * ", end="")
        elif y == x - 0:
            print(" * ", end="")
        else:
            print("   ", end="")
    print(" ")