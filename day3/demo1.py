#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/10 16:51
# @Author : yangyuanqiang
# @File : demo1.py


tuple1 = (1,2,3,4,5)
# tuple2 = (6,7,8,9,10)
tuple2 = 6,7,8,9,10
tuple3 = tuple1 + tuple2
print("%d",tuple3.__format__("name"))