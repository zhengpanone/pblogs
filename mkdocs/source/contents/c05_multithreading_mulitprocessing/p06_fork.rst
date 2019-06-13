=============================================
6. fork 多任务
=============================================

fork函数
====================

fork函数只在Unix/Linux/Mac上运行，windows不可以运行，父进程中fork的返回值，就是刚刚创建出来的子进程的id
全局变量在多个进程中不共享

::

 import os
 import time

 ret = os.fork() # 创建新的进程，父进程ret>0 ，子进程ret=0 
 print("父子进程都执行")

 if ret==0:
  while True:
    print('-----子进程--------&d--%d',%(os.getpid(),os.ppid()))
    time.sleep(1)
 else:
  while True:
    print('-----父进程-------%d'%os.getpid())
    time.sleep(1)

