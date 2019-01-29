========================
25.6 Redis基本使用
========================


1、连接方式
==================

    redis-py提供两个类Redis和StrictRedis用于实现Redis的命令，StrictRedis用于实现大部分官方的命令，并使用官方的语法和命令，Redis是StrictRedis的子类

::

 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 import redis

 r = redis.Redis(host='127.0.0.1',port=6379,db=0)
 r.set('name','zhengpanone')    # 添加
 print(r.get('name'))   # 获取

2、连接池
=================

    redis-py使用connection pool来管理对一个redis server的所有连接，避免每次建立、释放连接的开销。默认，每个Redis实例都会维护一个自己的连接池。可以直接建立一个连接池，然后作为参数Redis，这样就可以实现多个Redis实例共享一个连接池。

::
 
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 
 import redis
 pool = redis.ConnectionPool(host='127.0.0.1',port=6379)
 r = redis.Redis(pool)
 r.set('name','zhengpanone')    # 添加
 print(r.get('name'))   # 获取

3、管道
=======================

    redis-py默认在执行每次请求都会创建（连接池申请连接）和断开（归还连接池）一次连接操作，如果想要在一次请求中指定多个命令，则可以使用pipline实现一次请求指定多个命令，并且默认情况下一次pipline 是原子性操作。

::

 #!/usr/bin/env python
 # -*- coding:utf-8 -*-

 import redis
 pool = redis.ConnectionPool(host='127.0.0.1',port=6379)

 pipe = r.pipeline(transaction=True)

 r.set('name','zhengpanone')
 r.set('name','pipeline')

 pip.execute()

4、发布和订阅
===============================

    首先定义一个RedisHelper类，连接Redis，定义频道为monitor，定义发布(publish)及订阅(subscribe)方法。

::

 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 import redis

 class RedisHelper:
    def __init__(self):
        self.__conn = redis.Redis(host='127.0.0.1',port=6379)
        self.channel = 'monitor'

    def publish(self,msg):  # 定义发布方法
        self.__conn.publish(self.channel,msg)
        return True

    def subscribe(self):    # 定义订阅方法
        pub = self.__conn.pubsub()
        pub.subscribe(self.channel)
        pub.parse_response()
        return pub

发布者

::

 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 from RedisHelper import RedisHelper

 obj = RedisHelper()
 obj.publish('hello')   # 发布

订阅者

::

 #!/usr/bin/env python
 #-*- coding:utf-8 -*-
 from RedisHelper import RedisHelper

 obj = RedisHelper()
 redis_sub = obj.subscribe()    # 调用订阅方法

 while True:
    msg = redis_sub.parse_response()
    print(msg)


参考文档
=================

 `博客<http://www.cnblogs.com/melonjiang/p/5342383.html>`_
