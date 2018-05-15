#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/14 21:14
# @Author  : yangyuanqiang
# @File    : 第六周周测.py


'''
1、下面语句是授权用户的操作是？

A. create database test;
B. grant all privileges on *.* to 'xiang'@'%' identified by '1qaz@WSX';
C. create table student(id int not null);
D. select * from tabel_name where 条件1 and  条件2;

解析：
grant all privileges on *.* to 'xiang'@'%' identified by '1qaz@WSX';


2、如何检测一条SQL是否走索引
A explain select * from student where name = 'ling';
B expalin select * from student where id>1001;
C explain select * from student where name like '%ling%';
D create index inx_test_student_name (name);

解析：
explain select * from student where name = 'ling';



3、在使用pymysql操作中，cus.fetchone和fetchall返回数据的区别

A. fetchall() 返回list， fetchone() 返回tuple
B. fetchall() 返回tuple， fetchone() 返回list
C. fetchall()和fetchone() 都返回list
D. fetchall()和fetchone() 都返回tuple

解析：
fetchall() 返回list， fetchone() 返回tuple



4、在使用SQLAlchemy创建引擎的时候，正确的使用方式是

A. pymysql+mysql://username:password@hostname:port/db
B. mysql+pymysql://username:password@hostname:port/db
C. mysql+pymysql://username@password:hostname:port/db
D. mysql+pymysql://username:password:hostname:port/db

解析：
mysql+pymysql://username:password@hostname:port/db



5、在使用metadata.create_all()函数来创建表格的时候,说法正确的是

A. 表已经存在，会覆盖
B. 表已经存在，会重写
C. 表已经存在，不会任何操作
D. 以上都不对

解析：
表已经存在，不会任何操作


6、在SQLAlchemy中filter和filter_by的区别，正确的是

A. filter可以使用组合查询
B. filter_by需要表名+列名来表示
C. filter可以使用> < 等
D. filter()等于是=

解析：
filter可以使用> < 等


7、在使用SQLAchemy使用模糊查询的时候，使用正确的是

A. session.query(Student).filter(Student.name like('%ling%'))
B. session.query(Student).filter(Student.name.like('%ling%'))
C. session.query(Student).filter(like(Student.name, ('%ling%')))
D. session.query(Student).filter(like(('%ling%'), Student.name))

解析：
session.query(Student).filter(Student.name.like('%ling%'))


8、使用SQLAlchemy更新数据库中的数据时，我们使用的技巧是

A. 直接执行update的sql语句
B. 查出来我们的需要的数据
C. 查出来以后直接修改对象的数据就好了
D. alter函数修改

解析：
查出来以后直接修改对象的数据就好了


9、通过ORM方式创建一个表，需要加载哪些函数？选出不对的。

A column
B string
C sessionmake
D table

解析：
sessionmake



10、关于数据库连接池的说法，哪个是错误的。

A 使用pymysql连接数据库，每次连接都需要发起一次请求
B 使用连接池的目的是为了节省资源，使资源复用
C python的DBUtils连接池包有两个接口，分别是persistentDB和polledDB
D 使用连接池连接mysql可以保证数据库不会因为连接数过多而造成数据库宕掉

解析：
python的DBUtils连接池包有两个接口，分别是persistentDB和polledDB


'''