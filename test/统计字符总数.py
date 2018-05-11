#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/11 13:33
# @Author : yangyuanqiang
# @File : 统计字符总数.py

'''
判断一个字符串数字有多少个
字母有多少个
空格有多少个
其他字符

'''


#方法一：
while 1:
    strings = input("Please inpur a string(quit will be exit):")
    alpha, dig, space, other = 0, 0, 0, 0
    if strings.strip() == "quit":
        exit(1)
    for i in strings:
        if i.isdigit():
            dig += 1
        elif i.isspace():
            space += 1
        elif i.isalpha():
            alpha += 1
        else:
            other += 1
    print("alpha = {0}".format(alpha))
    print("dig = {0}".format(dig))
    print("space = {0}".format(space))
    print("other = {0}".format(other))
    print("字符串数字有{0}个，字母有{1}个，空格有{2}个，其他字符有{3}个".format(alpha, dig, space, other))


#方法二：
# something = input("请输入字符：")
# digit = 0   #中英文字母
# space = 0       #空格
# number = 0      #数字
# cstring = 0     #其他字符
#
# for i in something:
#     if i.isalpha():     #判断是否为中英文字母
#         digit += 1
#     elif i.isspace():   #判断是否为空格
#         space += 1
#     elif i.isdigit():   #判断是否为数字
#         number += 1
#     else:     #判断是否为字符
#         cstring += 1
#
# print("中英文字母有{0}个，空格有{1}个，数字有{2}个，其他字符有{3}个".format(digit, space, number,cstring))