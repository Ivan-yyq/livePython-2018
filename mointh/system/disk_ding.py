#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/19 16:10
# @Author : yangyuanqiang
# @File : disk.py


'''
python2环境运行
磁盘使用率

这里使用df命令获取磁盘使用情况。这个命令相当方便，既获取了磁盘的容量，也获取了使用率，可以根据需要进行后续的处理

'''

import paramiko
import re
import time
import datetime
import sys
import urllib
import urllib2
import json
import pexpect


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
    stdin, stdout, stderr = ssh.exec_command("df -lm")
    str_out = stdout.read().decode()
    str_err = stderr.read().decode()

    if str_err != "":
        print(str_err)
        continue

    text = (str_out)
    arr.append(text)


    print(arr)

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