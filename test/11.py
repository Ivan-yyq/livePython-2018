#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/18 10:50
# @Author : yangyuanqiang
# @File : 11.py

#11、猜数字游戏，while 1 无限循环，小于7继续continue循环，大于7继续continue循环，等于7，break退出循环 脚本名：11.py



while 1:
    number = int(input("请输入一个数字，开始猜数字游戏："))
    if number < 7:
        print("猜的数字小了...")
        continue
    elif number == 7:
        print("恭喜你猜对了！")
        break
    elif number > 7:
        print("猜的数字大了...")
        continue