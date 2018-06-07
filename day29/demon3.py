#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 22:02
# @Author  : yangyuanqiang
# @File    : demon3.py

#写excel文件

import xlwt

workbook = xlwt.Workbook()
sheet1 = workbook.add_sheet("test1", cell_overwrite_ok=workbook)
sheet1.write(0,0,"hello1")
sheet1.write(0,1,"hello2")
sheet1.write(0,2,"hello3")
sheet1.write(1,0,"world1")
sheet1.write(1,1,"world2")
sheet1.write(1,2,"world3")

workbook.save("testwrite.xls")
print("create ok")