#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 22:33
# @Author  : yangyuanqiang
# @File    : demo8.py


from multiprocessing import Pool
import time


def task(msg):
    print('hello, %s' % msg)
    time.sleep(1)
    return 'msg: %s' % msg


if __name__ == '__main__':
    pool = Pool(processes=4)

    results = []
    msgs = [x for x in range(10)]
    results = pool.map(task, msgs)

    pool.close()
    pool.join()

    print('processes done, result:')

    for x in results:
        print(x)