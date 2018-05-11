#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 22:17
# @Author  : lingxiangxiang
# @File    : demon6.py
import random
import string

# print(string.ascii_letters)     #ascii码小写a-z到大写A-Z
# print(string.digits)            #数字
# print(string.ascii_lowercase)   #小写a-z
# print(string.ascii_uppercase)   #大写A-Z
# print(string.printable)         #可打印的字符
# print(string.punctuation)       #特殊字符
# print(string.hexdigits)         #16进制


# 随机打印6位验证码
print("".join(random.sample(string.ascii_letters + string.digits, 6)))