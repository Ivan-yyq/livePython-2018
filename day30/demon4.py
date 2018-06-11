#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/11 21:50
# @Author  : yangyuanqiang
# @File    : demon4.py


'''python3 操作图片需要
pip install pillow
'''
from PIL import Image
image = Image.open("test.jpg")

cutjpg = image.crop((320, 65, 460, 220))
cutjpg.show()