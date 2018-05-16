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
    freemem = int(re.search("\d+", str_free).group()) // 1000

    mem_use = round(float(freemem) / float(totalmem), 2)
    # print("当前服务器IP地址：{0}\n内存总大小为：{1} M\n内存空闲为：{2} M\n内存使用率为：{3}\n".format(host["ip"], totalmem, freemem, mem_use))
    text = "当前服务器IP地址：{0}\n内存总大小为：{1}\n内存空闲为：{2}M\n内存使用率为：{3}\n".format(host["ip"], totalmem, freemem, mem_use)
    print(text)
    arr.append(text)


def convert(arr):
    temp = ''
    for text in arr:
        temp += text + "\n"
    return temp


url = 'https://oapi.dingtalk.com/robot/send?access_token=af3a595521fe84c9644835c93ec3821d0ff3f4654549c8eb1663e69b36ecd2c2'
data = {"msgtype": "text", "text": {"content": '服务器性能监控： ' + str(dt_new)
                                               + '\n' + convert(arr)
                                    }}
headers = {'Content-Type': 'application/json'}
request = urllib2.Request(url=url, headers=headers, data=json.dumps(data))
re = urllib2.urlopen(request, timeout=10)
re_data = re.read()
ssh.close()