#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 22:30
# @Author  : yangyuanqiang
# @File    : demo6.py


from multiprocessing import Pool
import time


def task(msg):
    print('hello, %s' % msg)
    time.sleep(1)


if __name__ == '__main__':
    pool = Pool(processes=4)

    for x in range(10):
        pool.apply_async(task, args=(x,))

    pool.close()
    pool.join()

    print('processes done.')