#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/18 15:32
# @Author : yangyuanqiang
# @File : cpu_mail.py

#https://blog.csdn.net/sadoshi/article/details/77247501
'''
代码支持python2和python3 环境下运行
CPU使用率的读取
这里使用cat /proc/stat命令读取实时的CPU使用率。这个命令可以获取到cpu的各种时间。具体的分析请自行百度。由于这个时间数值是从开机之后一直累加的，因此我们要取一次值之后，隔一小段时间再取一次值，前后两次的值相减，再计算这段时间的CPU利用率。具体公式是：
CPU利用率= 1-(CPU空闲时间2 - CPU空闲时间1) / (CPU总时间2 - CPU总时间1)
其中"CPU空闲时间1"为第一次取值时第4项的值，"CPU空闲时间2"为第二次取值时第4项的值，"CPU总时间1"为第一次取值时各项数值的总和，"CPU总时间2"为第二次取值时各项数值的总和
'''

import paramiko
import re
import time
import sys
import smtplib
from email.header import Header
from email.mime.text import MIMEText


# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # SMTP服务器
mail_user = "xxx@qq.com"  # 用户名
mail_pass = "hhaidszodmeabahi"  # 授权密码，非登录密码

sender = "xxx@qq.com"    # 发件人邮箱(最好写全, 不然会失败)
receivers = "xxx@163.com"  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# content = '我用Python'    #邮件内容
# title = '人生苦短'  # 邮件主题

# content = '我用Python'    #邮件内容
title = "服务器监控情况-CPU使用率"  # 邮件主题



# 设置主机列表
host_list = ({"ip":"192.168.0.131","port":22, "username":"root","password":"ever2016"},
             {"ip":"192.168.0.141","port":22, "username":"root","password":"ever2016"},
             {"ip":"192.168.0.145","port":22, "username":"root","password":"ever2016"},
             {"ip":"192.168.0.137","port":22, "username":"root","password":"ever2016"},
             )

arr = []
ssh = paramiko.SSHClient()
# 设置为授受不在known_hosts 列表的主机可以进行ssh连接
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


for host in host_list:
    ssh.connect(hostname=host["ip"], port=host["port"], username=host["username"], password=host["password"])
    # print(host["ip"])
    stdin, stdout, stderr = ssh.exec_command('cat /proc/stat | grep "cpu "')
    str_out = stdout.read().decode()
    str_err = stderr.read().decode()

    if str_err != "":
        print(str_err)
        continue
    else:
        cpu_time_list = re.findall("\d+", str_out)
        # print(cpu_time_list)
        cpu_idle1 = cpu_time_list[3]
        # print(cpu_idle1)
        total_cpu_time1 = 0
        for t in cpu_time_list:
            total_cpu_time1 = total_cpu_time1 + int(t)
            # print(total_cpu_time1)

    time.sleep(2)

    stdin, stdout, stderr = ssh.exec_command('cat /proc/stat | grep "cpu "')
    str_out = stdout.read().decode()
    str_err = stderr.read().decode()
    if str_err != "":
        print(str_err)
        continue
    else:
        cpu_time_list = re.findall("\d+", str_out)
        cpu_idle2 = cpu_time_list[3]
        total_cpu_time2 = 0
        for t in cpu_time_list:
            total_cpu_time2 = total_cpu_time2 + int(t)

    cpu_usage = round(1 - (float(cpu_idle2) - float(cpu_idle1)) / (total_cpu_time2 - total_cpu_time1), 2)
    if cpu_usage == 0.00:
        # print("waning")
        text = "当前服务器IP地址：{0}  CPU使用率为：{1}".format(host["ip"], cpu_usage)
        arr.append(text)
    # print("当前CPU使用率为：" + str(cpu_usage))
    #print("当前服务器IP地址：{0}  CPU使用率为：{1}".format(host["ip"], cpu_usage))
print(arr)

def convert(arr):
    temp = ''
    for text in arr:
        temp += text + "\n"
    return temp

def sendEmail():
    message = MIMEText(convert(arr), 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)

def send_email2(SMTP_host, from_account, from_passwd, to_account, subject, content):
    email_client = smtplib.SMTP(SMTP_host)
    email_client.login(from_account, from_passwd)
    # create msg
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')  # subject
    msg['From'] = from_account
    msg['To'] = to_account
    email_client.sendmail(from_account, to_account, msg.as_string())

    email_client.quit()

if __name__ == '__main__':
    sendEmail()
    # receiver = '***'
    # send_email2(mail_host, mail_user, mail_pass, receiver, title, content)
    ssh.close()