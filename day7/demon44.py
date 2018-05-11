#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/14 21:34
# @Author  : yangyuanqiang
# @File    : demon44.py



'''
列表生成式
[exp for val in collection if condition]
生成器
方法一：
(exp for val in collection if condition)
方法二：
'''

# 列表生成式
def jgg():
    count = 1
    number = list()
    for i in range(1, 10):
        number.append(i)
    for A in [x for x in range(1, 10)]:
        for B in [x for x in range(1, 10) if x != A]:
            for C in [x for x in range(1, 10) if x != A and x != B]:
                for D in [x for x in range(1, 10) if x != A and x != B and x != C]:
                    for E in [x for x in range(1, 10) if x != A and x != B and x != C and x != D]:
                        for F in [x for x in range(1, 10) if x != A and x != B and x != C and x != D and x != E]:
                            for G in [x for x in range(1, 10) if x != A and x != B and x != C and x != D and x != E and x != F]:
                                for H in [x for x in range(1, 10) if x != A and x != B and x != C and x != D and x != E and x != F and x != G]:
                                    for I in [x for x in range(1, 10) if x != A and x != B and x != C and x != D and x != E and x != F and x != H]:
                                        # print("A = {0} B = {1} C = {2} D = {3} E = {4} F = {5} G = {6} H = {7} I {8}".format(A, B, C, D, E, F, G, H, I))
                                        if (A + B + C == D + E + F == G + H + I == A + D + G == B + E + H == C + F + I == A + E + I == G + E + C == 15):
                                            print('''
                                                  第{9}种例子
                                                  -------------
                                                  | {0} | {1} | {2} |
                                                  | {3} | {4} | {5} |
                                                  | {6} | {7} | {8} |
                                                  -------------'''.format(A, B, C, D,E, F, G, H,I, count))
                                            count += 1


# jgg()



# a1 = (x for x in range(1, 10) if x%2==0)
# print(a1)   #是一个生成器，所以不会输出结果
# # python2   a1.next()
# print(next(a1)) #python3 是直接调用next方法
# print("##"*5)   #输出10个*
# for i in a1:
#     print(i)
#
# a2 = [x for x in range(1, 10) if x%2==0]
# print(a2)


def test():
    a = 1
    for i in range(1, 10):
        yield i
        # return i
        a += 1
        # return i
#return和yield的区别
# yield 可以理解成return，但是比return多一些角色
# yiele 每次都返回，但是下一次取值时，从上一次yield的下一行开始
m = test()
print(m)