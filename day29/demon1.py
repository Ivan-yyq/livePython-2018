#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 20:26
# @Author  : yangyuanqiang
# @File    : demon1.py


import csv

fileName = "test.csv"

with open(fileName, "r", encoding="utf-8") as f:
    text = csv.reader(f)
    for line in text:
        for i in line:
            print(i)


# with open(fileName, "r", encoding="utf-8") as f:
#     for line in f:
#         for i in line.split(","):
#             print(i.strip())