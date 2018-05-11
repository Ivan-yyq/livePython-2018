#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 20:51
# @Author  : yangyuanqiang
# @File    : demon11.py

'''
文件操作
参数1：    文件名，可以是文件的绝对路径
参数2：    option  r读  w写  b二进制    a追加
'''


# 声明全局变量的时候，变量名一定要全部大写
ENCODING = "utf-8"



# 读取文件内容
fr = open("11.txt", "rb")
# print(fr.read())
# 读取文件内容的每一行
# print(fr.readline())
# print(fr.readline())
# print(fr.readline())
#以列表的形式读取文件内容
# print(fr.readlines())
# print(fr.readline())
# print(fr.readline())
# print(fr.tell())
fr.seek(-3, 2)
print(fr.tell())

# print(fr.name)
# print(fr.encoding)
# print(fr.closed)



# print(fr.read())
fr.close()
# print(fr.closed)


# 读取文件内容，并按行号打印出来
# fr = open("11.txt", "r", encoding=ENCODING)
# for i, line in enumerate(fr.readlines()):
#     print("第{0}行内容为：{1}".format(i, line))
#     fr.close()


# 写入文件内容
fw = open("11.log", "w", encoding=ENCODING)
fw.write("hello word\n你咋不上天呢？\nno 作no die!")
fw.truncate(10)
fw.close()


# # 追加文件内容
# f = open("11.log", "a", encoding=ENCODING)
# f.write("\n嗨喽\n咋地？\nbi bi bi...\nso ga!")
# f.close()


# 文件对象f常用的操作方法：
# read()        把文件的所有内容都读取出来，返回一个字符串
# write("data") 把字符串"data"写入到文件中，只接受字符串参数
# fr.readline()    每次读取文件一行数据，返回每行的字符串数据
# fr.readlines()   读取文件内容，返回一个List，每一行是一个元素
# fr.name       文件名
# fr.fileno()   文件描述符
# fr.close()    关闭文件
# fr.encoding   文件编码
# fr.closed     返回bool值，判断文件是否已经关闭
# fr.seek(offset, whence)   offset偏移量正数向后偏移，负数向前偏移   whence 0开头，1现在位置，2代表结束
# fr.tell()     返回文件光标位置
# fr.truncate()   只有写文件才可以用，清空文件，size表示清空到什么地方
# help(fr.seek)   控制文件光标，文件需要使用b二进制方式打开


# print("##############################")
# with open("11.txt", "r", encoding=ENCODING) as f:   #冒号接着下一行就是要缩进
#     print(f.read())