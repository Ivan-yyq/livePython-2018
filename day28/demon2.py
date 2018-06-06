#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/5 21:57
# @Author  : yangyuanqiang
# @File    : demon2.py

'''
通过python发邮件步骤：
前提是：开通了第三方授权，可以使用smtp服务
1. 创建一个smtp对象
2. 连接smp服务器，默认端口都是25
3. 登录自己邮箱账号，
4. 调用发送消息函数，参数：发件人，收件人，消息内容
5. 关闭连接

'''



import email.mime.multipart
import email.mime.text
import smtplib



msg = email.mime.multipart.MIMEMultipart()
msg['from'] = '15625087150@163.com'
msg['to'] =  '974644081@qq.com'
msg['subject'] = 'ajing is very very cool'

context = '''
    <h1>老师好</h1>
    你好，
     这是一封自动发送的邮件。
      www.ustchacker.com hello
    '''
text = email.mime.text.MIMEText(_text=context, _subtype="html")
msg.attach(text)

em = smtplib.SMTP_SSL()
em.connect("smtp.163.com", 465)
em.login("15625087150@163.com", '163.com')
em.sendmail(from_addr='15625087150@163.com', to_addrs='974644081@qq.com', msg=msg.as_string())
em.quit()
