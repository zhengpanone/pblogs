==============
mysql基本使用
==============

命令行操作
-------------------

**Windows服务**

::

 -- 创建Windows服务
    sc create mysql binPath = mysqld_bin_path(注意：等号与值之间有空格)
 -- 启动MySQL
    net start mysql

**连接与断开服务**

::

 mysql -h ip -P port -u user -p password
 SHOW PROCESSLIST -- 显示那些线程正在运行
 SHOW VARIABLES -- 显示系统变量信息

**数据库操作**

.. literalinclude:: ./code/04_mysql_used/cmd_operate.txt
    :encoding: utf-8
    :language: html
    :linenos:




https://mp.weixin.qq.com/s/6QemK32sLR1tlSDomuGDmw




pymysql
-----------












.. code:: python

 # -*- coding:utf-8 -*-
 import pymysql
 
  # 创建连接
  conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',db='test')

