#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/2 21:58
# @Author  : yangyuanqiang
# @File    : 第一周周测.py


"""

第1题
Python3中下列语句错误的有哪些？

A s = input()
B s = raw_input()
C print('hello world.')
D print('''hello world.''')

解析：
Python3中已经没有raw_input了


第2题
下面哪个是 Pycharm 在 Windows 下 默认 用于“批量注释”的快捷键

A Ctrl + d
B Ctrl + 鼠标左键
C Ctrl + /
D Ctrl + Shift + f

解析：
Ctrl + /


第3题
下面哪个是 Pycharm 在 Windows 下 默认 用于“查找当前文件中的关键字”的快捷键

A Ctrl + f
B Ctrl + Shift + f
C Ctrl + n
D Ctrl + Shift + n

解析：
Ctrl + f


第4题
下面哪个是 Pycharm 在 Windows 下 默认 用于“查找当前项目中的关键字”的快捷键

A Ctrl + f
B Ctrl + Shift + f
C Ctrl + n
D Ctrl + Shift + n

解析：
Ctrl + Shift + f



第5题
下面哪个是 Pycharm 在 Windows 下 默认 用于“搜索最近编辑过的文件”的快捷键

A Ctrl + e
B Ctrl + Shift + p
C Ctrl + p
D Ctrl + Shift + e

解析：
Ctrl + Shift + e


第6题
下面哪个是 Pycharm 在 Windows 下 默认 用于“任意位置换行”的快捷键

A Ctrl + Enter
B Ctrl + Shift + Enter
C Ctrl + Shift
D Shift + Enter

解析：
Shift + Enter


第7题
下面哪个是 Pycharm 在 Windows 下 默认 用于“快速代码格式化（PEP8格式）”的快捷键

A Ctrl + Alt + L
B Shift + L
C Alt + L
D Ctrl + Shift + L

解析：
Ctrl + Alt + L


第8题
Python关系运算符中表示“不等于”的是哪个？

A ==
B =!
C !=
D !!

解析：
!=

第9题
下面选项哪个是python不支持的数据类型

A char
B int
C float
D list

解析：
char


第10题
下列表达式的值为True的是

A 5+4j > 2-3j
B 3>2<=2
C (3,2) 'xyz'
D 1=1

解析：
3>2<=2


第11题
如何定义一个list？

A a=(1,2,3,4,5)
B a=[1 2 3 4 5]
C a={ 1 2 3 4 5}
D a=[1,2,3,4,5]

解析：
a=[1,2,3,4,5]

第12题
如下赋值，b[0]的值是？

a=100

b=["a",20,10,55,90]

A 100
B a
C "a"
D 'a'

解析：
'a'


第13题
定义列表

list=['abc',99,'ccc','ddd']

然后执行

list.pop()

则list的值为？

A ['abc', 99, 'ccc']
B ['abc', 99, 'ccc', 'ddd']
C [abc, 99, ccc]
D 'ddd'

解析：
list=['abc',99,'ccc','ddd']
list.pop()
print(list)
结果：['abc', 99, 'ccc']


第14题
如果我们需要把连个字典合并是一个字典，需要调用字典的哪种方法

A. update
B. index
C. append
D. get

解析：
update


第15题
字典的value是什么类型的数据

A. str
B. list
C. tuple
D. 可以为任何类型

解析：
可以为任何类型


第16题
表达式a, b = (1, 2)代表的是什么意思

A. a = b = 1
B. a = b = 2
C. a = 1, b = 2
D. a = 2, b = 1

解析：
a = 1, b = 2


第17是
print(str(tuple(dict(a=1, b=2))))返回的结果是什么类型的数据

A. 字典
B. 元组
C. 字符串
D. 以上都不是

解析：
元组


多选题
第1题
Pycharm设置Python模板文件中可以使用的变量有哪些？

A ${TIME} ${DATE}
B ${USER}
C ${AUTHOR}
D ${NAME}

解析：
这里很容易把 C 选项也选上了，但实际上${AUTHOR}是没有的，这个打开Pycharm试一遍就好了
${TIME} ${DATE}
${USER}
${NAME}


第2题
下面选项哪些是正确的？

A 位：计算机的计算单位，代表0或者1
B 字节：一字节相当于8位
C Python中单行注释的符号是 '#'
D Python中多行注释的符号是 '/**/'

解析：
Python多行注释的符号应该是 ''' ""

位：计算机的计算单位，代表0或者1
字节：一字节相当于8位
Python中单行注释的符号是 '#'


第3题
以下运算符正确的有？

A a**b
B a == b
C c //= b
D not(a and b)

解析：
a**b
a == b
c //= b
not(a and b)


第4题
下面选项对变量赋值，哪个是正确的？

A s='It's my book'
B s="It's my book"
C s='It\'s my book'
D s="It\'s my book"

解析：
s="It's my book"
s='It\'s my book'
s="It\'s my book"


第5题
假设str='This is a test character.'，以下选项正确的有？



A print str[:-3]的结果为This is a test charac

B print str[1:10]的结果为This is a

C print str[::-1]的结果为.retcarahc tset a si sihT

D print str[2]的结果为i


解析：
str='This is a test character.'
print(str[:-3])
print(str[1:10])
print(str[::-1])
print(str[2])
结果：
This is a test charact
his is a
.retcarahc tset a si sihT
i


第6题
字典常用的定义方式有哪些？

A. dict(a=1, b=2)
B. {“name”: “lingjing”}
C. dict([(“name”, “ling”), (“age”, 20)])
D. 以上都是

解析：
dict(a=1, b=2)
{“name”: “lingjing”}
dict([(“name”, “ling”), (“age”, 20)])
以上都是


第7题
我们想判断一个数据的类型，可以使用下面的哪个函数

A. type
B. help
C. isinstance
D. hasattr

解析：
type
isinstance


第8题
以下哪个选项是一个json串

A. 以下都是
B. [{"name": "ling"}, {"a": "1"}]
C. dict(a=1, b=2)
D. {"hello": "world"}

解析：
[{"name": "ling"}, {"a": "1"}]
{"hello": "world"}


"""