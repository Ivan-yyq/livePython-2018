#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 21:50
# @Author  : yangyuanqiang
# @File    : demo3.py


from multiprocessing import Lock, Process
import time


def task1(lock, f):
    with lock:
        f = open(f, 'w+')
        f.write('hello ')
        time.sleep(1)
        f.close()


def task2(lock, f):
    lock.acquire()
    try:
        f = open(f, 'a+')
        time.sleep(1)
        f.write('world!')
    except Exception as e:
        print(e)
    finally:
        f.close()
        lock.release()


if __name__ == '__main__':
    lock = Lock()
    fn = './file.txt'

    start = time.time()
    p1 = Process(target=task1, args=(lock, fn,))
    p2 = Process(target=task2, args=(lock, fn,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()
    print('time cost: %s seconds' % (end - start))

    with open(fn, 'r') as f:
        for x in f.readlines():
            print(x)