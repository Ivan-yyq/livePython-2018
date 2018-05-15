#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/19 16:36
# @Author : yangyuanqiang
# @File : mail2.py


# Python版本：2.7

#####脚本使用说明######
# 1. 首先定义好脚本中的邮箱账号和密码
# 2. 脚本执行命令为：python mail.py 目标邮箱 "邮件主题" "邮件内容"


import os, sys

reload(sys)
sys.setdefaultencoding('gbk')
import getopt
import smtplib
from email.mime.text import MIMEText
from email.mime.text import MIMENonMultipart
from subprocess import *


def sendqqmail(username, password, mailfrom, mailto, subject, content):
    gserver = 'smtp.xxx.net'
    gport = 25
    try:
        msg = MIMEText(unicode(content).encode('utf-8'))
        msg['from'] = mailfrom
        msg['to'] = mailto
        msg['Reply-To'] = mailfrom
        msg['Subject'] = subject
        smtp = smtplib.SMTP(gserver, gport)
        smtp.set_debuglevel(0)
        smtp.ehlo()
        smtp.login(username, password)
        smtp.sendmail(mailfrom, mailto, msg.as_string())
        smtp.close()
    except Exception, err:
        print"Send mail failed. Error: %s" % err


def main():
    to = sys.argv[1]
    subject = sys.argv[2]
    content = sys.argv[3]
    ##定义QQ邮箱的账号和密码，你需要修改成你自己的账号和密码（请不要把真实的用户名和密码放到网上公开，否则你会死的很惨）
    sendqqmail('yuwei@xxx.com', 'xxx', 'yuwei@xxx.com', to, subject, content)


if __name__ == "__main__":
    main()
