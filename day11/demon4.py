#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 21:37
# @Author  : lingxiangxiang
# @File    : demon4.py


'''
sys
'''


import sys
print(sys.argv[1])  #传参数
print(sys.argv[2])
print(sys.stdout)   #文件类型
sys.stdout.write("allalallala")     #直接打印输出结果

# 在当前目录下生成1.log文件，把hello world写入到1.log文件中
# f = open("1.log", "w")
# sys.stdout = f
# print("hello world")