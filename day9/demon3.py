#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/20 20:05
# @Author  : yangyuanqiang
# @File    : demon3.py


'''
类的构造器
就是类在初始化的时候，首先，必须要执行的函数
'''

class A(object):
    #
    def __init__(self, name):
        self.name = name
        print("init class A")
    def hello(self):
        print("hello {0}".format(self.name))

a = A("ajing")
a.hello()   #调用函数 hello(self)