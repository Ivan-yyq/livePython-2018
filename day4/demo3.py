#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/4 11:29
# @Author : yangyuanqiang
# @File : demo3.py

while 1:
    age = input("Please is age: ")
    if age.strip():
        if age.isdigit():
            if int(age) >= 18:
                print("你是一个成年人！")
                break
            else:
                print("你还是一个小屁孩！")
                break
        else:
            print("你输入的不是数字，请重新输入数字：")
            continue
    else:
        print("你输入的是空格字符串，请重新数字：")
        continue