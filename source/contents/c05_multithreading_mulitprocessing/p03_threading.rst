=============================================
3. 多线程编程
=============================================

Thread创建多线程
================================================

::

 import threading
 import time

 def sayHello():
  print("Hello")
  time.sleep()

 if __name__ =="__main__":
  for i in range(5):
    th = threading.Thread(target=sayHello)
    th.start()


Thread子类完成创建多线程
=====================================

::

 import threading
 import time

 class MyThread(threading.Thread):
  def run(self):
    for i in range(3):
      time.sleep(1)
      msg = "I'm"+self.name+"@"+str(i)
      print(msg)

 if __name__ == "__main__":
 t = MyThread()
 t.start()

线程执行顺序
================================

::

 import threading
 import time

 class MyThread(threading.Thread):
  def run(self):
    for i in range(3):
      time.sleep(1)
      msg = "I'm"+self.name+"@"+str(i)
      print(msg)

  def test():
    for i in range(5):
      t = MyThread()
      t.start()

 if __name__ == "__main__":
  test()


线程共享全局变量
==============================================

多线程共享全局变量，多进程各自独有全局变量

::

 from threading import Thread
 import time

 g_num = 100

 def work1():
  global g_num
  for i in range(3):
    g_num += 1
  print("--------in work1,g_num %d----------------"%g_num)

 def work2():
  global g_num
  print("--------in work2,g_num %d----------------"%g_num)

 print("--------线程创建之前g_num is %d----------------"%g_num)
 t1 = Thread(target=work1)
 t1.start()

 time.sleep()

 t2 = Thread(target=work2)
 t2.start()

共享全局变量遇到的问题

::

 from threading import Thread
 import time

 g_num = 0

 def work1():
  global g_num
  for i in range(1000000):
    g_num += 1
  print("--------in work1,g_num %d----------------"%g_num)

 def work2():
  global g_num
  for i in range(1000000):
    g_num += 1
  print("--------in work2,g_num %d----------------"%g_num)

 t1 = Thread(target=work1)
 t1.start()

 #time.sleep(3)

 t2 = Thread(target=work2)
 t2.start()
 print("------g_num=%d---------"%g_num)

避免全局变量修改bug
==================================

互斥锁

::

 mutex = threading.Lock() # 创建锁
 mutex.acquire([blocking])  # 锁定
 mutex.release()  # 释放

::

 
 from threading import Thread
 import time

 g_num = 0

 def work1():
  global g_num
  
  for i in range(1000000):
    mutex.acquire()
    g_num += 1
    mutex.release()
  
  print("--------in work1,g_num %d----------------"%g_num)
  
 def work2():
  global g_num
  
  for i in range(1000000):
    mutex.acquire()
    g_num += 1
    mutex.release()
  print("--------in work2,g_num %d----------------"%g_num)
  

 mutex = Lock() # 创建互斥锁，默认是没有上锁的

 t1 = Thread(target=work1)
 t1.start()

 #time.sleep(3)

 t2 = Thread(target=work2)
 t2.start()
 print("------g_num=%d---------"%g_num)


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

死锁
============================

在线程间共享多个资源时，如果两个线程分别占用一部分资源并且等待对方资源，就会造成死锁

死锁例子

::

 import threading
 import time

 class MyThread1(threading.Thread):
  def run(self):
    if mutexA.acquire():
      print(self.name+"-----do1------up-----")
      time.sleep()

    if mutexB.acquire():
      print(self.name+"-----do1-------down--------")
      mutexB.release()
    mutexA.release()

 class MyThread2(threading.Thread):
  def run(self):
    if mutexB.acquire():
      print(self.name+"-----do2------up-----")
      time.sleep()

    if mutexA.acquire():
      print(self.name+"-----do2-------down--------")
      mutexA.release()
    mutexB.release()

 mutexA = threading.Lock()
 mutexB = threading.Lock()

 if __name__ == "__main__":
  t1 = MyThread1()
  t2 = MyThread2()
  t1.start()
  t2.start()

避免死锁
=================================

可添加超时时间



同步
===================================

::

 from threading import Lock,Thread
 from time import sleep

 class Task1(Thread):
  def run(self):
    while True:
      if lock1.acquire():
        print("------------Task1-------------")
        sleep(0.5)
        lock2.release()

 class Task2(Thread):
  def run(self):
    while True:
      if lock2.acquire():
        print("------------Task1-------------")
        sleep(0.5)
        lock3.release()

 class Task3(Thread):
  def run(self):
    while True:
      if lock3.acquire():
        print("------------Task1-------------")
        sleep(0.5)
        lock1.release()

 lock1 = Lock()
 lock2 = Lock()
 lock2.acquire()
 lock3 = Lock()
 lock3.acquire()

 t1 = Task1()
 t2 = Task2()
 t3 = Task3()

 t1.start()
 t2.start()
 t3.start()

生成者与消费者模式
===================================

1.队列
=======================

先进先出（fifo:first in first out）




2.栈
==========================

先进后出(filo:first in last out)


ThreadLocal 的使用
===============================

异步的实现
================================

GIL
===================================

全局解释器锁

多线程，其实是单线程，尽量使用多进程或使用C语言来实现


