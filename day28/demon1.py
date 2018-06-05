#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/5 20:41
# @Author  : yangyuanqiang
# @File    : demon1.py

#使用别人封装好的第三方模块发送邮箱

import yagmail

args = {
    "user": "xxxxxxxxxx@163.com",
    "password": "******",
    "host": "smtp.163.com",
    "port": "465"
}


emailList = ['344315429@qq.com','981240760@qq.com','564801795@qq.com','26795909@qq.com','353272297@qq.com','121295926@qq.com','937174156@qq.com','zhdya@zhdya.cn','657803478@qq.com','451133699@qq.com','757681618@qq.com' ]
email = yagmail.SMTP(**args)
email.send(to=emailList, subject="Test E-Mail", contents="Have a good day!", attachments="__init__.py", cc="974644081@qq.com")