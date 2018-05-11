#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/14 22:10
# @Author  : yangyuanqiang
# @File    : 用户列表排序.py

'''
对/etc/passwd文件排序操作，以uid用户ID号进行排序，输出的结果：
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin

'''



import codecs


def px(item):
    pass    #滤过
result = "" #空字符串
with codecs.open("passwd", "r") as f:   #读取完文件，自动关闭文件
    result = sorted(f.readlines(), key=lambda item: int(item.split(":")[2]))    #f.readlines() 一行一行的读，key=lambda 匿名函数，int整数，split进行切片，以"："为分隔符，取第三列uid

with codecs.open("sortPasswd", "w") as f:   #写入到新的文件中
    f.writelines(result)    #一行一行的写入到文件中