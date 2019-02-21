=============================================
5.7 Threading 多线程
=============================================

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