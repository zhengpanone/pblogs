========================
mongodb基本使用
========================

1. 启动mongodb实例
===================================

环境变量设置成功后,在D盘中创建一个文件夹data，用于存储MongoDB的数据库文件。然后，打开一个命令行工具，
输入mongod 启动MongoDB实例，默认监听的TCP端口是 27017 。


.. code-block:: shell

   mongodb 

MongoDB同时启动一个HTTP服务器，监听27017端口，如果MongoDB 实例安装在本地，那么在浏览器中输入：http://localhost:27017/

mongod 是整个MongoDB最核心的进程，负责数据库的创建，删除等管理操作，运行在服务器端，监听客户端的请求，提供数据服务。

2. 链接到MongoDB实例
===============================

不要关闭MongoDB实例，新打开一个命令行工具，输入mongo ，该命令启动mongo shell，shell 将自动连接本地(localhost)的MongoDB实例，默认的端口是27017：


.. code-block:: shell

   mongo 

mongo进程是构造一个Javascript Shell，用于跟mongod进程交互，根据mongod提供的接口对MongoDB数据库进行管理，相当于SSMS(SQL Server Management Studio)，是一个管理MongoDB的工具。



3. MongoDB常用命令
=====================

1、Help查看命令提示
>>>>>>>>>>>>>>>>>>>>

.. code-block:: shell
    :linenos:
    
    help 
    de.help() # 查看数据库级别的帮助
    db.test.help() # 查看集合级别的帮助
    db.test.find().help()


2、查看数据库
>>>>>>>>>>>>>>>>>>

.. code-block:: shell
   :linenos:

   show dbs 
   show collections
   # 查看当前使用的数据库
   db/db.getCollectionNames()

3、创建/切换数据库
>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: shell
   :linenos:

   use pm_cms  # 创建数据库
   db.createCollection('user')  # 创建集合
   db.getCollectionNames()  # 查看数据库中的所有集合


4、在foo数据库中创建users集合，向集合中插入一条document
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


.. code-block:: shell
   :linenos:

   use foo
   # 添加
   db.users.insert({"name":"name 1",age:21})
   db.users.save({name:'zhangsan',age:18,sex:true})

   #修改
   # 相当于: update users set name='wangwu' where age = 30
   db.users.update({age:30},{$set:{name:'wangwu'}},false,true)
   
   # 相当于: update users set age=age+50, name='赵六' where name='wangwu'
   db.users.update({name:'wangwu'},{$inc:{age:50},$set: {name:'赵六'}},false,true)
   
   db.users.find()

5、关闭MongoDB 实例
>>>>>>>>>>>>>>>>>>>>>>>>>>

在mongo shell中，执行以下命令，关闭MongoDB实例

.. code-block:: shell
   :linenos:

   use admin
   db.shutdownServer()



9, mongod 命令常用参数
======================================

 **1，常用参数**
 
 mongod 是MongoDB系统的主要守护进程，用于处理数据请求，数据访问和执行后台管理操作，必须启动，才能访问MongoDB数据库。

 在启动mongod时，常用的参数是：

    --dbpath <db_path>：存储MongoDB数据文件的目录

    --directoryperdb：指定每个数据库单独存储在一个目录中（directory），该目录位于--dbpath指定的目录下，每一个子目录都对应一个数据库名字。Uses a separate directory to store data for each database. The directories are under the --dbpath directory, and each subdirectory name corresponds to the database name.

    --logpath <log_path>：指定mongod记录日志的文件

    --fork：以后台deamon形式运行服务

    --journal：开始日志功能，通过保存操作日志来降低单机故障的恢复时间

    --config（或-f）<config_file_path>：配置文件，用于指定runtime options

    --bind_ip <ip address>：指定对外服务的绑定IP地址

    --port <port>：对外服务窗口

    --auth：启用验证，验证用户权限控制

    --syncdelay<value>：系统刷新disk的时间，单位是second，默认是60s

    --replSet <setname>：以副本集方式启动mongod，副本集的标识是setname

MongoDB的启动方式
======================================

 2.1 以命令方式启动，默认的dbpath是 C:\data\db


    mongod --dbpath=C:\data\db

 2.2 以配置文档的方式启动


    将mongod的命令参数写入配置文档，以参数-f 启动

    mongod -f C:\data\db\mongodb_config.config

 2.3 以daemon方式启动
 

 当启动MongoDB的进程关闭后，MongoDB随之关闭，只需要使用--fork参数，就能使MongoDB以后台守护进程方式启动。

 mongod -fork

 3，查看mongod的启动参数
 

 db.serverCmdLineOpts()

10，mongo命令常用参数
============================================================

mongo 是一个交互式的js shell，提供了一个强大的js 环境，为DBA管理MongoDB，developer查询MongoDB数据提供接口。通过mongo shell和MongoDB进行交互，查询和修改MongoDB数据库，管理MongoDB数据库，维护MongoDB的副本集和分片集群，是一个非常强大的工具。

在启动mongo shell时，常用的参数是：

--nodb: 阻止mongo在启动时连接到数据库实例；

--port <port> ：指定mongo连接到mongod监听的TCP端口，默认的端口值是27017；

--host <hostname> ：指定mongod运行的server，如果没有指定该参数，那么mongo尝试连接运行在本地（localhost）的mongod实例；<db address>：指定mongo连接的数据库

--username/-u <username> 和 --password/-p <password>：指定访问MongoDB数据库的账户和密码，只有当认证通过后，用户才能访问数据库

--authenticationDatabase <dbname>：指定创建User的数据库，在哪个数据库中创建User时，该数据库就是User的Authentication Database；

11，MongoDB的可视化工具
============================================================

Robomongo
>>>>>>>>>>>>>>>>

Robomongo 是开源，免费的MongoDB管理工具，下载地址：Robomongo下载

MongoBooster
>>>>>>>>>>>>>>>>>>>>>>

支持MongoDB 3.2 版本，个人使用免费，用于商业收费，下载地址：MongoBooster下载



