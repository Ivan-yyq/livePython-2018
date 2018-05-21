#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 22:32
# @Author  : yangyuanqiang
# @File    : demo7.py


from multiprocessing import Pool
import time


def task(msg):
    print('hello, %s' % msg)
    time.sleep(1)
    return 'msg: %s' % msg


if __name__ == '__main__':
    pool = Pool(processes=4)

    results = []
    for x in range(10):
        ret = pool.apply_async(task, args=(x,))
        results.append(ret)

    pool.close()
    pool.join()

    print('processes done, result:')

    for x in results:
        print(x.get())