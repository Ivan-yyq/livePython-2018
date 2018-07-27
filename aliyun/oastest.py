#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/7/26 10:36
# @Author : yangyuanqiang
# @File : oastest.py
# Centos 7 测试通过

from __future__ import print_function

import urllib

import oss2
import crcmod._crcfunext
from itertools import islice
import os, sys
import requests
import urllib2
import datetime, time


# print oss2.__version__
startTime = time.time()
# print (time.strftime("start: %Y-%m-%d %H:%M:%S", time.localtime()))



auth = oss2.Auth('yourAccessKeyId', 'yourAccessKeySecret')
endpoint = 'yourEndpoint'
bucket = oss2.Bucket(auth, endpoint, 'yourBucketName')

#oss归档存储上传
files = os.listdir('imgs/')
# print (files)
number=0
for i in files:
    number = number+1
    print (number)
    bucket.put_object_from_file(i,'imgs/'+ i )
os.system('/root/ossutil64 restore oss://oas-test/ -rf')    #通过ossutil64工具，批量对oss归档存储文件进行解冻



#当前目录下创建文件存储目录
path = "imgs_oas"
path = path.strip()
path = path.rstrip("\\")
isExists = os.path.exists(path)
if not isExists:
    os.makedirs(path)
    print (path + ' success')
else:
    print (path + ' false')


#oss归档存储下载
for b in islice(oss2.ObjectIterator(bucket), 1000): #遍历1000次
    # print (b.key)
    number = number+1
    print (number)
    url = 'http://yourBucketName.oss-cn-shenzhen.aliyuncs.com/{0}'.format(b.key)
    print (url)
    f = urllib2.urlopen(url)
    data = f.read()
    with open("imgs_oas/"+b.key, "wb") as code:
        code.write(data)

endTime=time.time()
td = int(endTime - startTime)
print (td)
# print (time.strftime("End: %Y-%m-%d %H:%M:%S", time.localtime()))