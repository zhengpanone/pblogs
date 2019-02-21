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

 