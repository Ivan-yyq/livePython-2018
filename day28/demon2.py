#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/5 21:57
# @Author  : yangyuanqiang
# @File    : demon2.py

import email.mime.multipart
import email.mime.text
import smtplib


msg = email.mime.multipart.MIMEMultipart()
msg['from'] = '657803478@qq.com'
msg['to'] = "15625087150@163.com"
