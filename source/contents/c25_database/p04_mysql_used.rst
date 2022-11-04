==============
mysql基本使用
==============

命令行操作
-------------------

**Windows服务**

 -- 创建Windows服务

    sc create mysql binPath = mysqld_bin_path(注意：等号与值之间有空格)

 -- 启动MySQL

    net start mysql

**连接与断开服务**

.. code-block:: shell
   :linenos:

   mysql -h ip -P port -u user -p password
   SHOW PROCESSLIST -- 显示那些线程正在运行
   SHOW VARIABLES -- 显示系统变量信息


**数据库授权**  


.. code-block:: shell
   :linenos:

   # 某个数据库所有的权限 ALL 后面+ PRIVILEGES
   GRANT ALL PRIVILEGES ON 库名.* TO '用户'@'%' IDENTIFIED BY '密码';   # *代表所有表， %代表所有IP


   # 某个数据库 特定的权限 权限后面没有 PRIVILEGES  所有的数据库权限- *.* 
   GRANT select,update,insert,delete ON 库名.* TO '用户名'@'%' IDENTIFIED BY '用户密码';


   # 授权语法 SQL详解
   GRANT -权限- ON 1.库名.表名(全部*) 2.所有数据库 *.*  TO '用户名'@'允许的ip(所有%)' IDENTIFIED BY '用户密码';


   
   FLUSH PRIVILEGES; # 权限刷新 - 每当调整权限后，通常需要执行以下语句刷新权限：


   SHOW GRANTS; # 显示授权

   # 移除授权

   EVOKE ALL PRIVILEGES ON *.* (库名或者 '*'-表示全部) FROM '用户名'@'ip';

   # 删除创建的用户

   DROP USER username@localhost;

   # 给用户改名 - '%'指的是所有ip

   RENAME user '老用户名'@'%' to '新名字'@'%';

   # 给用户修改密码 

   SET PASSWORD FOR '用户名'@'ip' = PASSWORD('123456');

   # 将BINLOG里的SQL语句提出来
   mysqlbinlog -v --skip-gtids=true  --base64-output=DECODE-ROWS /software/mysql-bin.001928 > /ss.sql


**数据库操作**

.. literalinclude:: ./code/04_mysql_used/cmd_operate.sh
    :encoding: utf-8
    :language: shell
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

