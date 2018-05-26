#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/24 21:06
# @Author  : yangyuanqiang
# @File    : demon2.py


'''
Pipe的方法返回一个tuple    (conn1, conn2)
Pipe的方法还有一个参数duplex参数，如果deplex=True，叫双工模式
如果deplex=False conn1只负责接收，conn2只负责发送消息
发消息：    send
收消息：    recv
关闭管道：   close
'''
import time, multiprocessing
from multiprocessing import Process, Pipe


def proc1(pipe):
    for i in range(10):
        print("send {0}".format(i))
        pipe.send(i)
        time.sleep(0.1)

def proc2(pipe):
    n = 10
    while n:
        print("proc2 recv: {0}".format(pipe.recv()))
        n -= 1


if __name__ == '__main__':
    (p1, p2) = multiprocessing.Pipe(duplex=False)
    pr = Process(target=proc1, args=(p2,))  #发消息
    cu = Process(target=proc2, args=(p1,))  #收消息
    pr.start()
    cu.start()
