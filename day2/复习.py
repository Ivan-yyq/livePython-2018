#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/14 14:14
# @Author  : yangyuanqiang
# @File    : 复习.py


# python不需要声明

# a  = 10     #int整型类型
# b = "hello world"   #str字符串类型
# c = 11.96   #float浮点型类型
# d = True    #bool布尔类型，True、False
#
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(int(c))   #强制类型转换为int整型
# print(round(c,1))   #四舍五入
#
# yang = "yang"
# chen = "chen"
# age = 18
# print("Hello " + yang)
# print("%s hahaha %s is %d" %(yang, chen, age))  #要区分类型，%s 整型，字符串  %d整型
# print("Hello's {0} and {1}".format(yang, chen)) #不用区分类型
#
# print(" a1 b 2c3d4".strip())    #过滤前和尾的空格，有事没事你就用一下
# print("a1b1c1d1".split("1"))    #以1为分隔
# print("asdfdfld".startswith("asd")) #以什么开头



# str1 = "a1b1c1d1"   #字符串相当于一个数组
# print(str1[0])
# print(str1[1])
# print(str1[2])
# print(str1[3])
# print(str1[4])
# print(str1[5])
#
# a = ["a", "b", "c", "d", "e"]   #列表，可以是字符串，数字
# print("-----".join(a))
# print(a)
#
# a = "a1b2c3d4"
# print(a[1:3])
# print(a[1  :])
# print(a[:-1])


# list 是一个列表
# 链表和数组     数据结构中的内容

# m = ["11.11", "1", "2", "3", "a", "b", "c", "True"]
# print(m)
# m.append("-----")  #默认在最后一个追加
# print(m)
# m.reverse() #把输出进行反转
# print(m)
# m.sort()  #排序
# print(m)
# m.pop()     #默认删除最后一个
# m.pop(2)      #删除下标第几个字符串
# print(m)
# print(m.index("True"))
# m.insert(2, "yang")     #在下标第几个字符串插入新的字符内容
# print(m)
# m.remove("11.11")       #删除一个字符串
# print(m)


# x = list()  #先声明，后使用，更好的使用
# for i in range(1,10):
#     x.append(i) #每循环一次，在屁股后面追加
# print(x)


# b = list()
# b += [i for i in range(1,10)]
# print(b)


b = list()
a = (1, 2, 3, 1, 5, 6)
print(a.index(5))   #打印列表5的下标
print(a.count(1))   #统计列表1的总数