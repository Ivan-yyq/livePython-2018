#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/16 21:36
# @Author  : yangyuanqiang
# @File    : 第三周周测.py



'''
第1题
下面的结果是[x*x for x in range(5)]

A. [0, 1, 2, 3, 4]
B. [1, 2, 3, 4, 5]
C. [0, 1, 4, 9, 16]
D. [0, 1, 4, 9, 16, 25]


程序：
def f(x):
    return  x * x
for i in map(f, [0, 1, 2, 3, 4]):
    print(i)
结果：[0, 1, 4, 9, 16]



第2题
下面哪些不是函数中的关键字

A. def
B. exit
C. return
D. test

程序：
D. test不是函数中的关键字



第3题
函数参数*args代表的是一个什么

A. list
B. tuple
C. set
D. dict

程序：
*args代表tuple元组



第4题
函数参数**kwargs代表的是一个什么

A. list
B. tuple
C. set
D. dict

程序：
**kwargs代表dict字典



第5题
a = lambda x,y: x+y 中的a代表是什么

A. x+y的值
B. 一个函数名字
C. 传入的参数
D. 以上都不是

程序：
a代表是一个函数的名字


第6题
sorted({"a": 10, "c": 15, "b": 20})的返回值是什么

A. ["a", "b", "c"]
B. [10, 15, 20]
C. {"a": 10, "b": 20, "c": 15}
D. {"a": 10, "c": 15, "b": 20}

程序：
print(sorted({"a": 10, "c": 15, "b": 20}))
结果：['a', 'b', 'c']



第7题
print sorted(mm.items(), key = lambda d:d[1], reverse = True) 改表达式中d代表的是什么

A. mm
B. mm中的每一个元素
C. mm.items()中的每一个额元素
D. 以上都不是

程序：
表达式d代表mm.items()中的每一个额元素


第8题
python3中如果小调用a = (x for x in range(5))的下一个元素，可以使用哪个方法

A. a.next()
B. a.append()
C. next(a)
D. a.to()

程序：
next(a)


第9题
以下哪种编码不可以表示中文

A. utf-8
B. acsii
C. gbk
D. gb2312

程序：
acsii编码不可以表示为中文


第10题
decode和encode方法分别代表什么意思

A. 解码， 编码
B. 编码， 解码
C. 中间编码，解码
D. 以上都不是

程序：
decode解码，encode编码


第11题
以下代码在Python3下的输出结果是什么？

# range(m, n, k): 初始值为m，最大值为n-1，步长为k(每次加k)
for i in range(1, 100, 3):
    if i % 5 == 0:
        print(i, end=' ')
print()

A 0 15 30 45 60 75 90
B 10 25 40 55 70 85
C 1 2 3 4 5..99
D 0 1 2 3 4..100

程序：
for i in range(1, 100, 3):
    if i % 5 == 0:
        print(i, end=' ')
print()
结果：10 25 40 55 70 85


第12题
以下代码在Python3下的输出结果是什么？
# range(m, n, k): 初始值为m，最大值为n-1，步长为k(每次加k)
j = 0
for i in range(3, 100, 3):
    if i % 5 == 0:
        break
    j += i
print(j)

A 0
B 30
C 1368
D 其他

程序
j = 0
for i in range(3, 100, 3):
    if i % 5 == 0:
        break
    j += i
print(j)
结果：30


第13题
以下代码在Python3下的输出结果是什么？  ()
# range(m, n, k): 初始值为m，最大值为n-1，步长为k(每次加k)
j = 0
for i in range(1, 30, 3):
    if i % 5 == 0:
        continue
    j += i
print(j)


A 0
B 12
C 110
D 其他

程序：
j = 0
for i in range(1, 30, 3):
    if i % 5 == 0:
        continue
    j += i
print(j)
结果：110


第14题
以下代码在Python3下的输出结果是什么？
# 伟业(罗马)非一日建成。
s = 'Rome was not built in one day.'
print('t: {0}, blank: {1}'.format(s.count('t'), s.count(' ')))


A t: {0}, blank: {1}
B t: 0, blank: 1
C t: 2, blank: 0
D t: 2, blank: 6

程序：
s = 'Rome was not built in one day.'
print('t: {0}, blank: {1}'.format(s.count('t'), s.count(' ')))
结果：t: 2, blank: 6


第15题
执行以下代码，哪些结果是不可能出现的？
import random
print(random.randint(10, 20))


A 10
B 15
C 20
D 10.5

程序：
20 >= x >= 10，且x是int型整数
结果：10.5


第16题
下列选项哪些是正确的？

A 生成器相比列表解析，效率更高，内存更省
B 列表里的元素是不可变的
C 元组里的元素是不可变的，所以又叫做只读列表
D 列表的clear()方法作用是将列表清空

程序：
列表的clear()方法作用是将列表清空


第17题
以下代码在Python3下的输出结果是什么？
f = lambda n: 1 if n <= 2 else f(n - 1) + f(n - 2)
print(f(6))


A 0
B 1
C 8
D 13

程序：
f = lambda n: 1 if n <= 2 else f(n - 1) + f(n - 2)
print(f(6))
结果：8


第18题
关于Python函数，下列说法哪些是不正确的？

A Python使用lambda创建匿名函数
B lambda函数不能递归调用自身
C Python函数支持可变数量的参数
D 默认参数尽量避免使用可变对象

程序：
lambda函数不能递归调用自身


第19题
Python open方法打开文件，哪个表示再末尾追加内容的

A 'r'
B 'a'
C 'w'
D 'c'

程序：
末尾追加内容 a



第20题
以下代码在Python3下的输出结果可能会出现？
# 其中 random.randint(m,n) 输出的值x: m <= x <= n
# f(30)=832040  f(40)=102334155
import random
f = lambda n: 1 if n <= 2 else f(n - 1) + f(n - 2)
a = b = [1, 1000]
a.append(f(random.randint(a[0], a[1])))
print(a, end=' ')
b.append(f(random.randint(b[0], b[1])))
print(b)


A [1, 1000, 8] [1, 1000, 13]
B [6, 8, 832040] [6, 8, 21]
C [ 6, 8, 8] [6, 8, 8, 13]
D [1, 1000, 84267] [1, 1000, 832040]

程序：
[ 6, 8, 8] [6, 8, 8, 13]



'''
