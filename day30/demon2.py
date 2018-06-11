#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/11 21:49
# @Author  : yangyuanqiang
# @File    : demon2.py


import codecs

import PyPDF2
import os

files = list()
for fileName in os.listdir("aming"):
    if fileName.endswith(".pdf"):
        files.append(fileName)

newFiles = sorted(files, key=lambda d: int(d.split(".pdf")[0]))
print(newFiles)


os.chdir("aming")
pdfWriter = PyPDF2.PdfFileWriter()#生成一个空白的pdf
for item in newFiles:
    pdfReader = PyPDF2.PdfFileReader(open(item, "rb"))
    for page in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(page))

with codecs.open("aminglinux.pdf", "wb") as f:
    pdfWriter.write(f)