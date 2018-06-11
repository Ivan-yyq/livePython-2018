#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/11 21:51
# @Author  : yangyuanqiang
# @File    : demon6.py


'''python3 操作图片需要
pip install pillow
'''
from PIL import Image
image = Image.open("test.jpg")
position = (320, 65, 460, 220)
cutjpg = image.crop(position).transpose(Image.ROTATE_180)
image.paste(cutjpg, position)

(x, y) = image.size
newx = 30
newy = int(y*newx/x)
newimage = image.resize((newx, newy))
newimage.show()
