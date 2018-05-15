#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 12:50
# @Author  : yangyuanqiang
# @File    : iptables.py


import iptc
import datetime
import log

'''
体彩自动化监控并禁止异常ip
1.注意用户特殊字符的密码或者cmd命令,需做转义,直到代码不出现红色波浪线
2.
3.
'''


# 规则定义函数
def stop_ip(ips):
    if ips is not None:
        for ip in ips:
            table = iptc.Table(iptc.Table.FILTER)
            chain = iptc.Chain(table, "DOCKER")
            rule = iptc.Rule()
            rule.src = ip
            rule.protocol = "tcp"
            match = iptc.Match(rule,'tcp')
            match.dport = "80"
            rule.add_match(match)
            target = iptc.Target(rule, "DROP")
            rule.target = target
            chain.insert_rule(rule)
            # chain.delete_rule(rule)
            table.commit()

if __name__ == '__main__':
    dic = {}
    log = log.Log('/var/lib/docker/overlay/313493da52b84333d10423918c6ab83791b04482ddf9b362e79f123622556fa0/merged/app/nginx/logs/tlotteryAct-dlt-sz.access.log', 1, 60, dic, 30)
    ips = log.parse()
    stop_ip(ips)
    print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print ips


