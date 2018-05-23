#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 21:50
# @Author  : yangyuanqiang
# @File    : demo1.py


# import time
# def sayhello(str):
#     print("Hello ",str)
#     time.sleep(2)
#
# name_list =['xiaozi','aa','bb','cc']
# start_time = time.time()
# for i in range(len(name_list)):
#     sayhello(name_list[i])
# print('%d second'% (time.time()-start_time))


#花费时间更少
import time
import threadpool
# def sayhello(str):
#     print("Hello ",str)
#     time.sleep(2)
#
# name_list =['xiaozi','aa','bb','cc']
# start_time = time.time()
# pool = threadpool.ThreadPool(10)
# requests = threadpool.makeRequests(sayhello, name_list)
# [pool.putRequest(req) for req in requests]
# pool.wait()
# print('%d second'% (time.time()-start_time))


def hello(m, n, o):
    """"""
    print("m = %s, n = %s, o = %s" % (m, n, o))


if __name__ == '__main__':
    # 方法1
    lst_vars_1 = ['1', '2', '3']
    lst_vars_2 = ['4', '5', '6']
    func_var = [(lst_vars_1, None), (lst_vars_2, None)]
    # 方法2
    # dict_vars_1 = {'m': '1', 'n': '2', 'o': '3'}
    # dict_vars_2 = {'m': '4', 'n': '5', 'o': '6'}
    # func_var = [(None, dict_vars_1), (None, dict_vars_2)]

    pool = threadpool.ThreadPool(2)
    requests = threadpool.makeRequests(hello, func_var)
    [pool.putRequest(req) for req in requests]
    pool.wait()