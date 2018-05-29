#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/29 22:12
# @Author  : yangyuanqiang
# @File    : selectdata.py


# 查询数据

from sqlalchemy import create_engine, Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://user1:123456@192.168.3.11/sqlalchemy?charset=utf8')

Base = declarative_base()
class Dictionary(Base):
    __tablename__ = 'dictionary'
    id = Column(Integer, primary_key=True)
    key = Column(String(50))
    value = Column(String(50))

DBSession = sessionmaker(bind=engine)
session = DBSession()

word = input("please input your a word:")
result =session.query(Dictionary).filter(Dictionary.key.like("%{0}%".format(word))).all()
for each in result:
    print(each.id, each.key, each.value)
