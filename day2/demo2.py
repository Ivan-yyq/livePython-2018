#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/29 22:00
# @Author  : yangyuanqiang
# @File    : demo2.py

# 链表和数组         数据结构中的内容
# 列表简单理解成数组

m = ["11.11", "2", "3", "a", "b", "c", "True"]
# m.append()    #最后一个元素追加内容
# m.reverse()   #
m.sort()        #字符串进行排序
print(m.sort())
print(m)
m.pop()         #删除排序后的最后一个字符串
m.pop(2)        #删除第三列
print(m.pop(2)) #打印第三列
m.insert(2,"yangyuanqiang") #在第二列后面添加内容
print(m)


# # list 列表打印输出：方法一
# a = list()
# for i in range(1,10):
#     a.append(i)
# print(a)
#
#
# #list 列表打印输出：方法二
# b =list()
# b += [i for i in range(1,10)]
# print(b)
#
# #list 列表打印输出：方法三
# print([i for i in range(1,10)])
#
#
# # index 下标
# # count 统计
# # tuple 强制类型
# b = ["a", "b", "c"]
# a =(1, 2, 3, 1, 5, 6)
# print(a.index(5))
# print(a.count(1))



# 总结：
# ""   字符串
# 字符串的方法：
# find()  查找
# replace()   替换
# strip()    前后去空格
# join(可迭代对象)      集成
# split()     分割
# format()    字符串格式化

# []    列表     list()
# 列表常用的方法
# append()    屁股后追加
# pop()     最后删除，返回值是删除的那个元素
# index(x)    返回元素的下标
# remove(x)     删除元素
# sort()      list排除
# reverse()     反序
# [:]     分片，前开后闭
# 下标元素从0开始
# ()    元组     tuple()
# "".     字符串的方法
# [].      列表的方法
# ().index(x)    ().count(x)