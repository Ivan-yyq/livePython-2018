#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 21:51
# @Author  : yangyuanqiang
# @File    : demo4.py


from multiprocessing import Semaphore, Process
import time


def task(s, msg):
    s.acquire()
    print('hello, %s' % msg)
    time.sleep(1)
    s.release()


if __name__ == '__main__':
    s = Semaphore(2)

    processes = []
    for x in range(8):
        p = Process(target=task, args=(s, x,))
        processes.append(p)

    start = time.time()
    for p in processes:
        p.start()

    for p in processes:
        p.join()

    end = time.time()

    print('8 process takes %s seconds' % (end - start))