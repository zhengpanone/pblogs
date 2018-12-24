===========================
5.4 消息队列(Queue)与进程池(Pool)
===========================

Queue消息队列
=============

1.创建
>>>>>>

::

 import multiprocessing
 queue = multiprocessing.Queue(队列长度)

2.方法
>>>>>>>

+------------------------+-----------+
| 方法                              | 描述          |
+========================+===========+
| body row 1 column 2   | column                                        |
+------------------------ +-----------+
| body row 2 | Cells may span columns.|
+------------------------+-----------+


3.进程通信
>>>>>>>>>>>

   因为进程间不共享全局变量，所以使用Queue进行数据通信，可以在父进程中创建2个子进程，一个往Queue中写数据，一个从Queue中取数据

::

 import multiprocessing
 import time

 def write_queue(queue):
   # 循环写入数据
   for i in range(10):
      if queue.full():
         print('队列已满！')
         break
      # 向队列中放入消息
      queue.put(i)
      print(i)
      time.sleep(0.5)

 def read_queue(queue):
   # 循环读取队列消息
   while True:
      # 队列为空，停止读取
      if queue.empty():
         print(---队列已空---)
         break
      # 读取消息并输出
      result = queue.get()
      print(reslut)

 if __name__ == '__main__':
   # 创建消息队列
   queue = multiprocessing.Queue(3)

   # 创建子进程
   p1 = multiprocessing.Process(target=write_queue, args=(queue,))
   p1.start()

   # 等待p1写入数据进程执行结束后，再往下执行
   p1.join()
   p1.multiprocessing.Process(target=read_queue ,args=(queue,))
   p1.start()

Pool进程池
===========

   初始化Pool时，可以指定一个最大进程数，当有新请求提交到Pool中时，如果池没有满，就会创建一个新的进程执行该请求；如果池中的进程数已经达到指定的最大值，那个该请求就会等待，直到池中有进程结束，才会用之前的进程来执行新的任务

1 创建
>>>>>>>>>

::

 import multiprocessing
 pool = multiprocessing(最大进程数)

2 方法
>>>>>

3 进程池内通信
>>>>>>>>>>>>>>>

::

 import multiprocessing
 Queue:queue = multiprocessing.Manager().Queue()

 # 写入数据的方法
 def write_data(queue):
   # for循环向消息队列中写入值
   for i in range(5):
      # 添加消息
      queue.put(i)
      print(i)
      time.sleep(0.2)
      print("队列已满")


参考文档
==========

CSDN：https://blog.csdn.net/zsh142537/article/details/82556147



