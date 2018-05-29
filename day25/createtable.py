#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/29 22:11
# @Author  : yangyuanqiang
# @File    : createtable.py


import codecs



from sqlalchemy import Column, MetaData, Table
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql+pymysql://user1:123456@192.168.3.11/sqlalchemy?charset=utf8')

metadata = MetaData(engine)

dictionary = Table('dictionary', metadata,
             Column('id', Integer, primary_key=True),
             Column('key', String(50)),
             Column('value', String(50))
             )
metadata.create_all(engine)
