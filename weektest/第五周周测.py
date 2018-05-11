#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/2 20:19
# @Author : yangyuanqiang
# @File : 第五周周测.py

'''
1、下面标识时间戳的是哪一个？

A. time.time()
B. datatime.time()
C. datetime.now()
D. time.now()

解释：
time.time()


2、在python中如何标识昨天的时间？

A. datetime.datetime.now()
B. time.now()
C. datetime.datetime.now() + datetime.timedelta（days=-1）
D. time.time()

解释:
datetime.datetime.now() + datetime.timedelta(days=-1)


3、如何在程序中让程序休眠？

A. datetime.sleep(2)
B. time.sleep(2)
C. datetime.timedelta.sleep(3)
D. datetime.ctime()

解释：
time.sleep(2)


4、如何把json类型的字符串转换成python对象使用json模块的哪个方法？

A. load
B. dump
C. dumps
D. loads

解决：
Python 数据结构转换为JSON：dumps
JSON编码的字符串转换回一个Python数据结构：loads


5、在使用logging模块记录日志之前，我们首先要做什么

A. logging.debug("hello")
B. logging.info("hello")
C. logging.error("hello")
D. logger = logging.getLogger(__name__)

解释：
logger = logging.getLogger(__name__)


6、如果要执行系统命令，并取得命令行返回的结果，可以使用下面哪个方法

A. os.system("ipconfig")
B. os.popen("ipconfig")
C. os.path.exists()
D. os.listdir("")

解释：
os.popen("ipconfig")        ？？？


7、在string模块中，如何标识特殊字符

A. string.ascii_letters
B. string.printable
C. string.punctuation
D. string.hexdigits

解释：
string.punctuation


8、执行命令“./test.py a b c”时，如何在test.py中获取参数a

A. sys.argv[0]
B. sys.argv[1]
C. sys.argv[2]
D. sys.argv[3]

解释：
sys.argv[1]


9、
如果我们想获取一个1-100的随机整数，应该使用下面哪种方法？

A. random.random()
B. random.randint(1,100)
C. random.randrange(1,100)
D. random.sample([x for x in rang(1, 101)], 5)

解释：
random.randrange(1,100)

10、下面哪个加密算法是我们最常用的？

A. md5()
B. rsa128
C. rsa256
D. base64()

解释：
md5()



'''
