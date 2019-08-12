==============
mysql基本使用
==============

pymysql
-----------

操作
>>>>

::
 # -*- coding:utf-8 -*-
 import pymysql
 
  # 创建连接
  conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',db='test')

