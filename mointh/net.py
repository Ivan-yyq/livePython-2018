#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/19 16:13
# @Author : yangyuanqiang
# @File : net.py

'''

网络流量

网络流量可以使用cat /proc/net/dev查看，可以看到每个网络接口当前发送和接收的字节和包的数量，由于是一个累计的值，如果需要计算一定时间间隔内的流量，
可以让程序sleep一定时间，然后再次获取，进行计算。个人建议每隔一段时间获取这个值，并且写入文件中，然后再使用其他程序去计算其速度和流量


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
    stdin, stdout, stderr = ssh.exec_command("cat /proc/net/dev")
    str_out = stdout.read().decode()
    str_err = stderr.read().decode()

    if str_err != "":
        print(str_err)
        continue

    print(str_out)

    ssh.close()