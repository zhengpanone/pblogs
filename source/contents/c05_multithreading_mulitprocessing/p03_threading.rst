=============================================
多线程编程
=============================================

Thread基本使用
===============================

Thread创建多线程
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. literalinclude:: ./code/03.多线程编程/01.Thread创建多线程.py
    :encoding: utf-8
    :language: python
    :lines: 1-
    :emphasize-lines: 1
    :linenos:

Thread子类完成创建多线程
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. literalinclude:: ./code/03.多线程编程/02.继承thread子类来实现多线程.py
    :encoding: utf-8
    :language: python
    :lines: 1-
    :emphasize-lines: 1
    :linenos:

线程间通信
====================================

线程共享全局变量
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

多线程共享全局变量，多进程各自独有全局变量

.. literalinclude:: ./code/03.多线程编程/03.线程间通信_共享全局变量.py
    :encoding: utf-8
    :language: python
    :lines: 1-
    :emphasize-lines: 1
    :linenos:

共享全局变量遇到的问题
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. literalinclude:: ./code/03.多线程编程/03.共享变量的问题.py
    :encoding: utf-8
    :language: python
    :lines: 1-
    :emphasize-lines: 1
    :linenos:

避免全局变量修改bug
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

通过Queue

.. literalinclude:: ./code/03.多线程编程/03线程通过queue.py
    :encoding: utf-8
    :language: python
    :lines: 1-
    :emphasize-lines: 1
    :linenos:


多线程使用非全局变量
================================================

不共享非全局变量

::

 import threading
 import time

 def test():
  name = threading.current_thread().name
  print("-----thread name is %s------------"%name)
  num = 100
  if name = "Thread-1":
    name += 11
  else:
    time.sleep(2)
  print("------thread is %s-----num=%d----"%(name,num))


线程同步
============================

Lock 
>>>>>>>>>>>>>>>>>>>>

- 如何使用锁

>>> mutex = threading.Lock() # 创建锁
>>> mutex.acquire([blocking])  # 锁定
>>> mutex.release()  # 释放

- 实际应用

.. literalinclude:: ./code/03.多线程编程/04互斥锁.py
    :encoding: utf-8
    :language: python
    :lines: 1-
    :emphasize-lines: 1
    :linenos:

.. literalinclude:: ./code/03.多线程编程/05通过类实现互斥锁.py
    :encoding: utf-8
    :language: python
    :lines: 1-
    :emphasize-lines: 1
    :linenos:

- 影响

  - 用锁会影响性能
  - 锁会引起死锁

死锁
>>>>>>>>>>>>>>>>>>>

在线程间共享多个资源时，如果两个线程分别占用一部分资源并且等待对方资源，就会造成死锁

- 死锁例子

.. literalinclude:: ./code/03.多线程编程/06死锁.py
    :encoding: utf-8
    :language: python
    :lines: 1-
    :emphasize-lines: 1
    :linenos:


避免死锁
>>>>>>>>>>>>>>>>>>>

- 可添加超时时间
- 使用重入锁RLock [1]_

.. [1] 

在同一个线程中,可以连续调用多次acquire,一定要注意acquire的次数要和release的**次数一致**

- 重入锁使用

.. literalinclude:: ./code/03.多线程编程/07重入锁.py
    :encoding: utf-8
    :language: python
    :lines: 1-
    :emphasize-lines: 1
    :linenos:

条件变量(Condition)
>>>>>>>>>>>>>>>>>>>>>>>>>>>

条件变量,用于复杂的线程间同步

Semaphore 
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

用于控制进入数量的锁,文件读写,写一般只是用于一个线程写,读可以允许有多个 



生成者与消费者模式
===================================

1.队列
>>>>>>>>>>>>>>>>>>>>>>

先进先出（fifo:first in first out）




2.栈
>>>>>>>>>>>>>>>>>>>>>>>>>

先进后出(filo:first in last out)


ThreadLocal 的使用
===============================

异步的实现
================================



:ref:`topics-index`
=============================

全局解释器锁

多线程，其实是单线程，尽量使用多进程或使用C语言来实现


