#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/30 22:11
# @Author  : yangyuanqiang
# @File    : insertdata.py


# 插入数据

import codecs

from sqlalchemy import Integer, Column, String, create_engine
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






class HandleData(object):
    def __init__(self, dataFile):
        self.dataFile = dataFile
    def make_data_to_str(self):
        with codecs.open(self.dataFile, encoding='utf-8') as file:
            for (num, value) in enumerate(file):
                line = value.strip().split()
                diction =Dictionary(id=num+1, key=line[0], value=line[1])
                session.add(diction)
        session.commit()


handleData = HandleData('dictionary.txt')   #数据
handleData.make_data_to_str()
session.close()