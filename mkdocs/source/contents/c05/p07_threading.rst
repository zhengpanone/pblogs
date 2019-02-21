=============================================
5.7 Threading 多线程
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
