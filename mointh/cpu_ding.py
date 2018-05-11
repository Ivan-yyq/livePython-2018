#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/18 15:32
# @Author : yangyuanqiang
# @File : cpu_mail.py

#https://blog.csdn.net/sadoshi/article/details/77247501
'''
python版本2
CPU使用率的读取
这里使用cat /proc/stat命令读取实时的CPU使用率。这个命令可以获取到cpu的各种时间。具体的分析请自行百度。由于这个时间数值是从开机之后一直累加的，因此我们要取一次值之后，隔一小段时间再取一次值，前后两次的值相减，再计算这段时间的CPU利用率。具体公式是：
CPU利用率= 1-(CPU空闲时间2 - CPU空闲时间1) / (CPU总时间2 - CPU总时间1)
其中"CPU空闲时间1"为第一次取值时第4项的值，"CPU空闲时间2"为第二次取值时第4项的值，"CPU总时间1"为第一次取值时各项数值的总和，"CPU总时间2"为第二次取值时各项数值的总和
通过钉钉群机器人发送告警
'''

import paramiko
import re
import time
import datetime
import sys
import urllib
import urllib2
import json

data_ext=0
start = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
timeArray = time.strptime(str(start), "%Y-%m-%d %H:%M:%S")
timeStamp = int(time.mktime(timeArray))
time_local = time.localtime(timeStamp)
dt_new = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
# print dt_new


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
    if cpu_usage >= 0.80:
        # warning = "CPU使用率大于0.80"
        text = "当前服务器IP地址： {0}  CPU使用率为：{1}".format(host["ip"], cpu_usage)
        print(text)
        arr.append(text)


# print(arr)

def convert(arr):
    temp = ''
    for text in arr:
        temp += text + "\n"
    return temp

url = 'https://oapi.dingtalk.com/robot/send?access_token=af3a595521fe84c9644835c93ec3821d0ff3f4654549c8eb1663e69b36ecd2c2'
data = {"msgtype": "text", "text": {"content": '服务器性能监控： '+ str(dt_new)
                                             # +'\n' + warning
                                             +'\n' + convert(arr)
                                    }}
headers = {'Content-Type': 'application/json'}
request = urllib2.Request(url=url, headers=headers, data=json.dumps(data))
re = urllib2.urlopen(request, timeout=10)
re_data = re.read()

ssh.close()