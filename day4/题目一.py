#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/4 13:49
# @Author : yangyuanqiang
# @File : 题目一.py

something = input("请输入字符：")
digit = 0   #中英文字母
space = 0       #空格
number = 0      #数字
cstring = 0     #其他字符

for i in something:
    if i.isalpha():     #判断是否为中英文字母
        digit += 1
    elif i.isspace():   #判断是否为空格
        space += 1
    elif i.isdigit():   #判断是否为数字
        number += 1
    else:     #判断是否为字符
        cstring += 1

print("中英文字母有{0}个，空格有{1}个，数字有{2}个，其他字符有{3}个".format(digit, space, number,cstring))
