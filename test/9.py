#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/4 11:52
# @Author : yangyuanqiang
# @File : 9.py

# 9、打印99乘法表   脚本名：9.py

for y in range(1,10):
    for x in range(1, y+1):
        print("{0}x{1}={2}".format(x, y, x*y),end=" ")
        if x == y:
            print()