#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 22:13
# @Author  : yangyuanqiang
# @File    : test.py


from multiprocessing import Process
import os,time,random
def work():
    r = random.randint(1, 5)
    print('{0} is running: {1}'.format(os.getpid(), r))
    time.sleep(r)
    print('{0} is done'.format(os.getpid()))
if __name__ == '__main__':
    for i in range(2):
        p=Process(target=work)
        p.start()