#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/21 11:12
# @Author : yangyuanqiang
# @File : curl2.py

#查找IP地址归属地

import urllib2
import json
import time
import linecache


ENCODEING = "utf-8"
fr = open("ip.txt", 'r')
line = fr.readlines()
# print(linecount)
for ip in line:
    # print(ip)
# ip = "182.90.42.221"
# ip = f.read()
    apiurl = "http://ip.taobao.com/service/getIpInfo.php?ip=%s" % ip
    # apiurl = "http://ip.taobao.com/service/getIpInfo.php?ip={0}".format(f)
    content = urllib2.urlopen(apiurl).read()
    # print(content)
    data = json.loads(content)['data']
    code = json.loads(content)['code']

    if code == 0:
        print "ip:%s 来自 %s %s %s %s \n" % (
        data["ip"].encode('utf-8'), data["country"].encode('utf-8'), data["region"].encode('utf-8'),
        data["city"].encode('utf-8'), data["isp"].encode('utf-8'))
        data_ip = "ip:%s 来自 %s %s %s %s \n" % (
        data["ip"].encode('utf-8'), data["country"].encode('utf-8'), data["region"].encode('utf-8'),
        data["city"].encode('utf-8'), data["isp"].encode('utf-8'))
        fw = open("ipout.log", "a")
        fw.write(data_ip)
        time.sleep(5)
    else:
        print data.encode('utf-8')

fr.close()
fw.close()