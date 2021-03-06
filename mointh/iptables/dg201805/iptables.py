#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/17 12:18
# @Author : yangyuanqiang
# @File : iptables.py



# python 2.x 版本使用

import iptc
import paramiko
import datetime
# import commands
import subprocess
import log
import urllib
# import urllib2
import json

'''
体彩自动化监控并禁止异常ip
1.注意用户特殊字符的密码或者cmd命令,需做转义,直到代码不出现红色波浪线
2.
3.
'''


# 规则定义函数
def stop_ip(ips):
    if len(ips) == 0 :  #ips等于0，直接退出循环
        return
    robot_ip = []
    # print ips
    for ip in ips:  #ips不等于0，进入循环判断
        ip = ip + '.0/24'
        robot_ip.append(ip)
        # print ip
        table = iptc.Table(iptc.Table.FILTER)
        chain = iptc.Chain(table, "INPUT")
        rule = iptc.Rule()
        rule.src = ip
        rule.protocol = "tcp"
        match = iptc.Match(rule, 'tcp')
        match.dport = "80"
        rule.add_match(match)
        target = iptc.Target(rule, "DROP")
        rule.target = target
        chain.insert_rule(rule)
        # chain.delete_rule(rule)
        table.commit()
        # print 'z'

#发送钉钉群机器人告警
    start = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    url = 'https://oapi.dingtalk.com/'
    data = {"msgtype": "text", "text": {"content": '东莞扫码活动\n当前时间:' + str(start)
                                                    +'\niptables防火墙新增加规则，Block掉的IP:' + str (robot_ip)}}

    headers = {'Content-Type': 'application/json'}
    # request = urllib2.Request(url=url, headers=headers, data=json.dumps(data))
    # re = urllib2.urlopen(request, timeout=10)
    # re_data = re.read()


if __name__ == '__main__':
    dic = {}
    log = log.Log('/logs/dg201805.access.log', 1, 60, dic)
    ips = log.parse()
    stop_ip(ips)



