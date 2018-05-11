#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 21:09
# @Author  : lingxiangxiang
# @File    : demon1.py

#  !!!!!!!start!!!!!!!!
#  hello world   (hello)
# !!!!!!!!end!!!!!!!!!


def hello():
    print("!!!!!!!start!!!!!!!!")
    print("hello world")
    print("!!!!!!!!end!!!!!!!!!")



a = hello()
print("-------------------------")
b = hello

# a 代表什么     hello函数把返回这给到a  None
# b 代表什么     b是一个函数, b()相当于hello()
b()