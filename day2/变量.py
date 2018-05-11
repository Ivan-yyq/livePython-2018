#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/3/30 14:50
# @Author : yangyuanqiang
# @File : 变量.py

T = True
F = False
print("This True is stand for %d" %(T))
print("This False is stand for %d" %(F))

a = 111.95
print(type(a))

a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))


a = 11
print (isinstance(a,int))

a = "Hello"
b = "Python"

print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])

if ("H" in a):
    print("H 在变量 a 中")
else:
    print("H 不在变量 a 中")

if ("M" not in a):
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")

print(r'\n')
print(R'\n')


x = 5
x += 2
print(x)