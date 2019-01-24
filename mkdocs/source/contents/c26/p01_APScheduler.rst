========================================
26.1 定时任务框架APScheduler
========================================

1.简介
=================

APScheduler 基于Quartz的Python定时任务框架，实现了Quartz的所有功能。提供了基于日期、固定时间间隔以及crontab类型的任务，并且可以持久化任务。基于这些功能，我们可以很方便的实现一个python定时任务系统。在Python的世界中，另外一个齐名的调度模块是Celery，功能也非常的强大，号称分布式的调度器。
官方文档：http://apscheduler.readthedocs.io/en/latest/

2.安装
===========

::

 pip install APScheduler

3.基本概念
==================

- 触发器（trigger）包含调度逻辑，每一个作业有它自己的触发器，用于决定接下来哪一个作业会运行。除了他们自己初始配置以外，触发器完全是无状态的。

- 作业存储（job store）存储被调度的作业，默认的作业存储是简单地把作业保存在内存中，其他的作业存储是将作业保存在数据库中。一个作业的数据将在保存在持久化作业存储时被序列化，并在加载时被序列化。调度器不能分享同一个作业存储。

- 执行器（executor）

- 调度器（scheduler）

- Blocking Scheduler：仅可用在当前的进程内，与当前的进行共享计算资源

- BackgroundScheduler：在后台进行调度，不影响当前系统计算运行

- AsynclOScheduler：如果当前系统中使用了async module，则需要使用异步的调用器

- GeventScheduler：如果使用了gevent，则需要使用该调度器

- TornadoScheduler：如果使用了Tornado，则使用当前的调度器

- TwistedScheduler：Twister应用的调度器

- QtScheduler：Qt的调度器

::

 import time
 from apscheduler.schedulers.blocking import BlockingScheduler

 def my_job():
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))

 schec = BlockingScheduler()
 sched.add_job(my_job,'interval',seconds=5)
 sched.start()


参考文档
=================


简书：https://www.jianshu.com/p/b1606c7f8286