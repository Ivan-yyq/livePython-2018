#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/9 18:08
# @Author  : yangyuanqiang
# @File    : demon6.py


#抓取aming的linux教程，然后制作成pdf文件
#先抓取每个的网页，然后生成pdf文件

import codecs
import os
import sys

import pdfkit
import requests

base_url = 'http://www.apelearn.com/study_v2/'
if not os.path.exists("aming"):
    os.mkdir("aming")

os.chdir("aming")
s = requests.session()

for i in range(1, 27):
    url = base_url + 'chapter' + str(i) + '.html'
    print(url)
    file = str(i) + '.pdf'
    print(file)
    config = pdfkit.configuration(wkhtmltopdf=r"D:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
    try:
        pdfkit.from_url(url, file)
    except:
        continue

