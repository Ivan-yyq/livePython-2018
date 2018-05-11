#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 20:52
# @Author  : lingxiangxiang
# @File    : demon2.py

'''
日志记录模块
日志的几个级别
debug
info
warning
error
critical
'''

import logging

# 定义日志级别，默认warning以上才会输出告警日志信息
# logging.basicConfig(level=logging.DEBUG)

# 日志输出格式，在当前目录下生成 myapp.log 存放日志输出信息
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt=' %Y/%m/%d %H:%M:%S', filename='myapp.log', filemode='w')


logger = logging.getLogger(__name__)    #本身


def hello():
    print("hello world")

def main():
    logger.info("开始执行main函数")
    print("##"*10)
    hello()
    logger.info("调用hello() 函数")
    try:
        a = 2/0
        f = open("demon1.py", "r")
    except Exception as e:
        logger.error("除数不能为0")
    finally:
        logger.warning("文件没有正常关闭")



main()