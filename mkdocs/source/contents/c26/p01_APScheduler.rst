========================
26.1 定时任务框架APScheduler
========================

1.简介
======

APScheduler 基于Quartz的Python定时任务框架，实现了Quartz的所有功能。提供了基于日期、固定时间间隔以及crontab类型的任务，并且可以持久化任务。基于这些功能，我们可以很方便的实现一个python定时任务系统。在Python的世界中，另外一个齐名的调度模块是Celery，功能也非常的强大，号称分布式的调度器。
官方文档：http://apscheduler.readthedocs.io/en/latest/

2.安装
=====

::

 pip install APScheduler

3.基本概念
========

- 触发器（trigger）

- 作业存储（job store）

- 执行器（executor）

- 调度器（scheduler）

- Blocking Scheduler：仅可用在当前的进程内，与当前的进行共享计算资源

- BackgroundScheduler：在后台进行调度，不影响当前系统计算运行

- AsynclOScheduler：如果当前系统中使用了async module，则需要使用异步的调用器

- GeventScheduler：如果使用了gevent，则需要使用该调度器

- TornadoScheduler：如果使用了Tornado，则使用当前的调度器

- TwistedScheduler：Twister应用的调度器