#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 22:15
# @Author  : yangyuanqiang
# @File    : demon6.py


# 共享内存

import threading, time

class Hello(threading.Thread):
    def __init__(self, args):
        super(Hello, self).__init__()
        self.args = args
        global a    #全局变量
        print("a = {0}".format(a))
        a += 1


    def run(self):
        print("开始子进程 {0}".format(self.args))
        print("结束子进程 {0}".format(self.args))

if __name__ == '__main__':

        a = 1
        print("start main")
        t1 = Hello(5)
        time.sleep(3)
        t2 = Hello(5)
        t1.start()
        t2.start()
        print("### a = {0} ###".format(a))
        print("end main")