#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/23 20:51
# @Author  : yangyuanqiang
# @File    : 第四周周测.py


'''
第1题
Python装饰器语法糖的符号是什么？

A %
B @
C &
D $

解析：
@


第2题
Python中定义一个匿名函数的关键字是什么？

A lambda
B def
C map
D class

解析：
lambda


第3题
关于Python闭包下列说法不正确的是？

A 闭包函数必须有内嵌函数
B 闭包函数的返回值是内函数的引用
C 闭包函数的内函数必须用到外函数的变量
D 闭包函数的内函数不需要用到外函数的变量

解析：
闭包函数的内函数不需要用到外函数的变量



第4题
Python中当多个装饰器修饰一个函数时，执行顺序应该是？（例如下面的：）

# A B C 是三个装饰器
@A
@B
@C
def f():
    pass
A ABC
B CBA
C ACB
D 无序

解析：
ABC


第5题
Python中类的构造函数和析构函数的写法分别是？

A init(self) del(self)
B __del(self)__ __init(self)__
C del(self) init(self)
D __init(self)__ __del(self)__

解析：
__init(self)__ __del(self)__


第6题
Python中定义一个类的关键字是？

A def
B Def
C class
D Class

解析：
class

第7题
类的三大特性是？

A 封装、继承、多态
B 封装、继承、抽象
C 封装、抽象、多态
D 抽象、继承、多态

解析：
封装、继承、多态


第8题
下列说法正确的是？
class Person(object):
    name = 'xxx'  # @1
    def __init__(self, name):
        self.name = name  # @2
p1 = Person('demo1')
p2 = Person('demo2')
A @1 是类变量，p1 p2共用这个类变量
B @1 是实例变量，又叫做（静态）属性，p1 p2独自拥有这个实例变量
C @2 是类变量，p1 p2共用这个类变量
D @2 是实例变量，又叫做（动态）属性，p1 p2独自拥有这个实例变量

解析：
@1 是类变量，p1 p2共用这个类变量


第9题
下面代码执行的结果是？  (A)
class Person(object):
    name = 'xxx'
    hair = 'blond'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print('{0} {1}: __del__'.format(Person.name, self.name), end=' ')


def f(flag=False):
    p1 = Person('Jim', '30')
    if flag:
        print(p1.name, Person.name, p1.age, p1.hair, Person.hair)


f(True)
# print('Start.', end=' ')
# f()
# print('End.', end=' ')
A xxx Jim 30 blond blond
B Jim xxx 30 blond blond
C Jim xxx 30 None blond
D xxx Jim 30 None blond

解析：
Jim xxx 30 blond blond


第10题
下面代码执行的结果是？  (B)
class Person(object):
    name = 'xxx'
    hair = 'blond'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print('{0} {1}: __del__'.format(Person.name, self.name), end=' ')


def f(flag=False):
    p1 = Person('Jim', '30')
    if flag:
        print(p1.name, Person.name, p1.age, p1.hair, Person.hair)


# f(True)
print('Start.', end=' ')
f()
print('End.', end=' ')
A Start. End.
B Start. xxx Jim: __del__ End.
C Start. End. xxx Jim: __del__
D xxx Jim: __del__ Start. End.

解析：
Start. xxx Jim: __del__ End.


第11题
以下变量只有类本身可以访问的是：

A. _name
B. __name
C. name
D. 以上都不是

解析：
__name


第12题
def hello(): print("hello world") a = hello; 请问a变量代表什么意思

A. 一个函数名字，如同hello
B. hello函数的执行结果
C. 一个字符串变量
D. 以上都不是

解析：
一个函数名字，如同hello


第13题
在类的封装中，我们应该把主要的代码逻辑应该写在什么地方

A if __name__ == "__main__"
B. 自定义的额def main(): 函数中
C. 自定义的类中
D. 直接写在文件内容中

解析：
自定义的额def main(): 函数中


第14题
装饰器写在函数的前面，相当于什么？

A. 把函数作为参数传递给装饰器
B. 把装饰器作为参数，传递给函数
C. 他们没有任何关系
D. 把他们都作为参数传递给主函数

解析：
把函数作为参数传递给装饰器


第15题
with open("1.txt", "r") as f: f.read()的返回值是什么类型

A. list
B. tupel
C. str
D. dict

解析：
str


第16题
with open("1.txt", "w") as f: f.writelines(args)的参数args是什么类型？

A. list
B. tupel
C. str
D. dict

解析：
list


第17题
子类在重写父类中的__init__方法时，还想先继承父类的方法，然后在写自己对应的方法，应该怎么操作？

A. super(子类， self).__init__()
B. super(父类， self).__init__()
C. super().__init__()
D. super()

解析：
super(子类， self).__init__()


第18题
在子类继承父类的时候，如果子类中已经重写了父类的方法，子类在调用该方法时，调用的是谁的方法？

A. 父类的方法
B. 子类中的方法
C. 其他方法
D. 报错

解析：
子类中的方法


第19题
class A(Name): pass 代表的是什么意思

A. A类需要一个参数Name
B. A类继承Name类
C. A类什么方法都没有
D. Name类继承A类

解析：
A类继承Name类


第20题
写代码我们在起变量名字的时候都需要使用驼峰，定义类首字母（）写， 函数名字首字母（）写， 实例化类首字母（）写

A. 大， 小， 小
B. 小， 小， 大
C. 小， 大， 小
D. 大， 大， 小

解析：
大， 小， 小


'''