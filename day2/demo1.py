#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/29 21:36
# @Author  : yangyuanqiang
# @File    : hello_name.py


'''
 这是一个测试程序
 三个单引号或者双引号都为多行注释

'''


str = " www.www.com "
name = "Ivan"
age = 24
# 字符串常用的方法：
# .strip()                  字符串过滤空格，有事没事，你用一下，只能过滤前和尾的空格
print(str.strip())
# .replace(old, new)        方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，默认替换1次，如果指定第三个参数max，则替换不超过 max 次
print(str.replace("www","aaa",2))
# .find(sub)                字符串查找sub字符串的内容，如果找到，返回自字符串的下标，下标由0开始，否则返回-1
print(str.find("c"))
# .format()                 字符串格式化
print(str + "{0}, {1}".format(name, age))
# .split()                  切割字符串
# .join(可迭代对象)         集成
# .startswith()             用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 Fals

# str = "www.baidu.cn"
# print("旧地址:", str)
# print("新地址：", str.replace("baidu.cn","baidu.com"))
# print(str.find('w',1))
# print(str.find('w',3))
print("hello'{0} {1}".format('s','yangyuanqiang'))

# print(" a1 b 2c3d4".strip())
# print("a1b1c1d2".split("1"))
# print("asdfasjdfas".startswith("asdfas"))
# #
# a = ["a", "b", "c", "d", "e"]
# print("-------".join(a))
# print(a)