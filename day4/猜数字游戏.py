#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/4 11:15
# @Author : yangyuanqiang
# @File : 猜数字游戏.py



number = 7
guess = 0
print("数字猜迷游戏开始！")
while 1:
    guess = int(input("请输入你猜的数字："))
    if guess == number:
        print("恭喜，你猜对了！")
        break
    elif guess < number:
        print("猜的数字小了...")
        continue
    elif guess > number:
        print("猜的数字大了...")
        continue