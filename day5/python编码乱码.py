#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/11 16:42
# @Author : yangyuanqiang
# @File : python编码乱码.py


'''
原有编码       ->      unicode编码    -> 目的编码
decode("utf-8")  解码  ->       unicode       ->  encode("gbk")  编码
'''

a = [1, "哈哈"]
print(a)
print(a[1])

m = u"哈哈哈"
print(m)

n = "你好"
print(n.decode("utf-8").encode("gbk"))
