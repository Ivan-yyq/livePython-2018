#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 21:14
# @Author  : lingxiangxiang
# @File    : demon3.py
'''
os模块
os.name
如果结果为nt， 则为windows系统，
如果结果为posix， 则为unix系统
os.system(cmd)   纯粹的执行系统命令，但是没有返回结果
result = os.popen(cmd)
result.read()  这样你就可以对reuslt进行控制了
os.
'''


import os

# 打印系统名称
print(os.name)

# 判断系统
if os.name == "nt":
    cmd = "ipconfig"
elif os.name == "posix":
    cmd = "ifconfig"

# 打印输出结果
os.system(cmd)

# print(os.listdir("C:"))   #列出当前目录， ls
# os.chdir("..")   #改变目录， cd
# print(os.listdir(os.getcwd()))
# print(os.getcwd())  #pwd
# os.mkdir("test")
# os.remove("myapp.log")
# os.rmdir("test")
# os.rename("demon1.py", "demon111.py")
# print(os.linesep)
# windows换行符\n\r  linux换行符\n   mac \r

# 创建一个test目录，not非
# if not os.path.exists("test"):
#     os.mkdir("test")

# 打印当前路径
# print(os.path.abspath("./"))
# 以最后一个目录为分隔
print(os.path.split("~/Desktop/Python一期直播课/livePython-2018/第十一节课"))
