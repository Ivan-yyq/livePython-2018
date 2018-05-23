#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 22:20
# @Author  : yangyuanqiang
# @File    : demon7.py


#锁

import threading
lock = threading.Lock()

lock.acquire()  #获取锁
lock.release()  #释放锁
# with lock:
#   time.sleep(3)
# with open("1.txt", "w") as f:
#     f.close()