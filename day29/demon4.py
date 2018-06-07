#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 22:12
# @Author  : yangyuanqiang
# @File    : demon4.py


#pdf

import pdfkit
config = pdfkit.configuration(wkhtmltopdf="C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
pdfkit.from_url("http://www.geeksforgeeks.org/convex-hull-set-2-graham-scan/", "out.pdf",configuration=config)