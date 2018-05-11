#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/18 11:36
# @Author : yangyuanqiang
# @File : 12.py


#12、判断一个字符串数字有多少个，字母有多少个，空格有多少个，其他字符 脚本名：12.py

# "".isdigit()    数字
# "".isspace()    空格
# "".isalpha()    字母
# other           其他字符

while 1:
    strings = input("Please input a string(quit will be exit)：")
    digit, space, alpha, other = 0, 0 ,0 ,0
    if strings.strip() == "quit":
        exit(1)
    for i in strings:
        if i.isdigit():
            digit += 1
        elif i.isspace():
            space += 1
        elif i.isalpha():
            alpha += 1
        else:
            other += 1
    print("digit: {0}".format(digit))
    print("space: {0}".format(space))
    print("alpha: {0}".format(alpha))
    print("other: {0}".format(other))
    print("数字有：{0}个，空格有：{1}个，字母有：{2}个，其他字符有：{3}个".format(digit, space, alpha, other))