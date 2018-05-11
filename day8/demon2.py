#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 21:25
# @Author  : lingxiangxiang
# @File    : demon2.py


def startEnd(fun):
    def wraper(name):
        print("!!!!!!!start!!!!!!!!")
        fun(name)
        print("!!!!!!!end!!!!!!!!")
    return wraper
# 返回值 wraper函数
# hello()  相当于执行  wraper()
@startEnd
def hello(name):
    print("hello {0}".format(name))
hello("ajing")


# 1. wraper = startEnd(hello)
# 2. hello = wraper
# 3. 调用hello()

# 装饰器的作用：在不改变源代码的情况下，给现有的函数增加新的功能
# 装饰器通过@进行使用 ,相当于把hello() 函数作为参数，传给startEnd()
# @startEnd  相当于    hello = startEnd(hello)
