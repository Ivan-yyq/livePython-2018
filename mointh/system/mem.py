#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/19 15:43
# @Author : yangyuanqiang
# @File : mem.py


'''

内存信息的读取。

通过远程执行‘cat /proc/meminfo’可以获取内存相关信息。这里我只读取MemTotal和MemFree的信息。需要读取其他信息可以利用正则表达式匹配获取其他数据。
例子把这两个信息输出到标准输出中，实际应用可以通过crontab定时执行脚本，把结果写入文件，可以给传给监控系统，当超越一定阀值的时候进行相应的处理

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
    stdin, stdout, stderr = ssh.exec_command("cat /proc/meminfo")
    str_out = stdout.read().decode()
    str_err = stderr.read().decode()

    if str_err != "":
        print(str_err)
        continue

    str_total = re.search("MemTotal:.*?\n", str_out).group()
    # print(str_total)
    totalmem = int(re.search("\d+", str_total).group()) // 1000

    str_free = re.search("MemFree:.*?\n", str_out).group()
    # print(str_free)
    freemem = int(re.search("\d+", str_free).group()) // 1000

    mem_use = round(float(freemem) / float(totalmem), 2)
    # print('当前内存使用率为：' + str(mem_use))
    print("当前服务器IP地址：{0}\n内存总大小为：{1} M\n内存空闲为：{2} M\n内存使用率为：{3}\n".format(host["ip"], totalmem, freemem, mem_use))


    ssh.close()