#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/24 20:31
# @Author  : yangyuanqiang
# @File    : demon1.py


'''
消息队列
一个是生产者producer
一个是消费者customer
创建一个队列  q = Queue()
发消息：    q.put()
收消息：    dat = q.get()
'''
import time
from multiprocessing import Queue, Pipe
from threading import Thread


def producer(q):
    print("start producer")
    for i in range(10):
        q.put(i)
        # print("producer has producer value {0}".format(i))
        time.sleep(0.3)
    print("end producer")

def customer(q):
    print("start customer")
    while 1:
        date = q.get()
        print("customer has get value {0}".format(date))




if __name__ == '__main__':
    q = Queue()
    p = Thread(target=producer, args=(q,))
    c = Thread(target=customer, args=(q,))
    p.start()
    c.start()
