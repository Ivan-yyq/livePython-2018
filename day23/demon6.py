#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/26 10:42
# @Author  : yangyuanqiang
# @File    : demon6.py



from tasks import *
re1 = taskA.delay(100, 200)
print(re1.result)
re2 = taskB.delay(1, 2, 3)
print(re2.result)
re3 = add.delay(1, 2, 3)
print(re3.status)     #PENDING
