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

**数据库外键约束**

删除和更新有四种设置方式

- cascade：级联，当父表更新、删除，子表会同步更新和删除

- set null：置空，当父表更新、删除的时候，字表会把外键字段变为null，所以这个时候设计表的时候该字段要允许为null，否则会出错

- restrict：父表在删除和更新记录的时候，要在子表中检查是否有有关该父表要更新和删除的记录，如果有，则不允许删除个更改

- no action：和restrict一样




https://mp.weixin.qq.com/s/6QemK32sLR1tlSDomuGDmw




pymysql
----------

.. code:: python

 # -*- coding:utf-8 -*-
 import pymysql
 
  # 创建连接
  conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',db='test')

