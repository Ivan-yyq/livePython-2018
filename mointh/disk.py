#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/19 16:10
# @Author : yangyuanqiang
# @File : disk.py


'''
python2和python3环境运行
磁盘使用率

这里使用df命令获取磁盘使用情况。这个命令相当方便，既获取了磁盘的容量，也获取了使用率，可以根据需要进行后续的处理

'''

import paramiko
import re
import time
import sys
import pexpect
import smtplib
from email.mime.text import MIMEText

# 设置邮箱
# mail_host = "smtp.163.com"  #定义SMTP服务器
# mail_to = "yangyuanqiang@everflourish.com"  #邮件收件人
# mail_from = "15625087150@1com"  #邮件发件人
# mail_pass = "163.com"   #邮件发件人邮箱密码


# 设置主机列表
host_list = ({"ip":"192.168.0.131","port":22, "username":"root","password":"ever2016"},
             {"ip":"192.168.0.141","port":22, "username":"root","password":"ever2016"},
             {"ip":"192.168.0.145","port":22, "username":"root","password":"ever2016"},
             {"ip":"192.168.0.137","port":22, "username":"root","password":"ever2016"},
             )


ssh = paramiko.SSHClient()
# 设置为授受不在known_hosts 列表的主机可以进行ssh连接
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


for host in host_list:
    ssh.connect(hostname=host["ip"], port=host["port"], username=host["username"], password=host["password"])
    # print(host["ip"])
    stdin, stdout, stderr = ssh.exec_command("df -lm")
    str_out = stdout.read().decode()
    str_err = stderr.read().decode()

    if str_err != "":
        print(str_err)
        continue

    print(host["ip"],str_out)

    ssh.close()