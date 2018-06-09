#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 21:19
# @Author  : yangyuanqiang
# @File    : demon2.py

#读取excel表的数据

import xlrd

data = xlrd.open_workbook("test.xlsx")
table = data.sheets()[0]    #读取excel表里的下标表格
rows = table.nrows  #查看有多少行数据
# print("共有{0} ".format(rows) + " 行数据")
cols = table.ncols  #查看有多少列数据
# print("共有{0} ".format(cols) + " 列数据")
#一行一行取数据
# for i in range(rows):
#     print(table.row_values(i))

# print("##"*10)
# #一列一列取数据
# for j in range(cols):
#     print(table.col_values(j))

print("###"*10)
#按每行取第一个列的数据
for row in range(rows):
    for col in range(cols):
        cell = table.cell_value(row, col)
        print(cell)