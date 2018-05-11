#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/14 09:45
# @Author  : yangyuanqiang
# @File    : 8.py

'''
8、输出空心正方形 5 * 5，结果为 *****     脚本名：8.py
                   *   *
                   *   *
                   *   *
                   *****
'''

#打印空心正方形
for i in range(5):
    for o in range(5):
        if i == 0 or i == 4:
            print(' * ',end=''),
        elif o == 0 or o == 4:
            print(' * ',end='')
        else:
            print('   ',end='')
    print(" ")



#打印实心正方形
# for i in range(5):
#     for o in range(4):
#        print(' * ',end='')
#     print(' * ')


#打印空心三角形
# for i in range(6):
#     for o in range(6):
#         if i ==5 :
#             print(' * ',end='')
#         elif o == 0 :
#             print(' * ', end='')
#         elif o == i -0:
#             print(' * ', end='')
#         else:
#             print('   ', end='')
#     print('  ')