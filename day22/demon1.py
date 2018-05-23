#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 20:15
# @Author  : yangyuanqiang
# @File    : demon1.py


'''

强大的 Manage

'''
from multiprocessing import Manager, Process



def worker(dt, lt):
    for i in range(10):
        key = "args" + str(i)
        dt[key] = i*i

    lt += [x for x in range(10)]

if __name__ == '__main__':
    manager = Manager()
    dt = manager.dict()
    lt = manager.list()
    p = Process(target=worker, args=(dt, lt))
    p.start()
    p.join(timeout=3)    #父进程要等待子进程处理完，才结束
    print(dt)
    print(lt)