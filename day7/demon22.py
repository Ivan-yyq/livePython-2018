#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/14 20:22
# @Author  : yangyuanqiang
# @File    : demon22.py



'''
函数的额关键字
def     定义函数
return  返回值
pass    滤过
exit(1) 直接退出
'''


# def add1(x, y):
#     print(x + y)
#
# def add2(x, y):
#     return x + y
#
# def hello():
#     pass
#     print("hello")
#
# def helloworld():
#     exit(1)
#     print("hello world")
#
#
#
# add1(1, 2)
# result = add2(1, 2)
# print(result)
# hello()
# helloworld()


'''
函数的参数
*args       tuple参数，对应赋值
**kwargs    dict参数，对应赋值
fun(*args, **keargs)
fun(1, 2, 3, 4, 5, a=10, b=40)

args = (1, 2, 3, 4, 5)
keargs = (a=10, b=40)

'''


'''
匿名函数
def add(x, y):
    return x + y
    
add = lambda x,y:x + y
'''


# def test(m, *args, **kwargs):
#     print("m = {0}".format(m))
#     print("args = {0}".format(args))
#     print("kwargs = {0}".format(kwargs))
#
# test(10,1,11,12,a=10,b=20)
# test(m=10, 1, 2, 3, a=1, b=2)

def add(x, y):
    return x + y


add = lambda x, y: 1 + 2