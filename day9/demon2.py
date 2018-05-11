#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/20 20:04
# @Author  : yangyuanqiang
# @File    : demon2.py



'''
类， 面向对象一个很重要的载体
1. 类的定义
class StuentName(object):   #（object）是一个超级类，StuentName继承object的类
    pass
2. 类里面一般都是由很多函数组成，函数的第一个参数默认都是self
如果需要全局变量，就在类的内部直接定义
3. 类的内部在调用函数或者调用变量的时候，必须使用self.变量   或者self.函数
self 代表的是类实例化以后的个体
4.类的实例化
实例化类的首字母小写作为实例，然后类实例化
studentName = StudentName();

'''

class A(object):    #(object) 是一个超级类，A继承object的类
    name = "ajing"
    def hello(self):
        print("hello {0}".format(self.name))
    def test(self):
        self.hello()
        print("This is test.")

a = A()
b = A()