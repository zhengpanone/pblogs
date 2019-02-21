=============================================
5.4 消息队列(Queue)与进程池(Pool)
=============================================

Pool进程池
====================

初始化Pool时，可以指定一个最大进程数，当有新请求提交到Pool中时，如果池没有满，就会创建一个新的进程执行该请求；如果池中的进程数已经达到指定的最大值，那个该请求就会等待，直到池中有进程结束，才会用之前的进程来执行新的任务

1 创建
>>>>>>>>>>>>>>>>>>

::

 from multiprocessing import Pool
 import time
 

 def worker(msg):
   t_start = time.time()
   print("%s开始执行，进程号为%d"%(msg,os.getpid()))
   time.sleep(random.random()*2)
   t_stop = time.time()
   print(msg,"执行完毕，耗时%0.2f"%(t_stop-t_start))

 pool = Pool(3) # 定义一个进程池，最大进程数3

 for i in range(0,10):
   # pool.apply_async(要调用的目标,(传递给目标的参数元组))
   # 每次循环将会用空闲的子进程去调用目标
   # pool.apply(worker,(i,)) 阻塞方式
   pool.apply_async(worker,(i,))

 print("-------------------start--------------")
 pool.close()  # 关闭进程池，关闭后pool不再接收新的请求
 pool.join()   # 等待pool中所有子进程执行完成，必须放在close语句之后
 print("--------------------end-------------")
   

2 方法
>>>>>>>>>>>>>>>

3 进程池内通信
>>>>>>>>>>>>>>>>>>>>>>>>>>

::

 import multiprocessing
 Queue:queue = multiprocessing.Manager().Queue()
 import time

 # 写入数据的方法
 def write_data(queue):
   # for循环向消息队列中写入值
   for i in range(5):
      # 添加消息
      queue.put(i)
      print(i)
      time.sleep(0.2)
      print("队列已满")

 # 读取数据方法
 def read_data(queue):
   # 循环读取数据
   while True:
      # 判断队列是否为空
      if queue.qsize() ==0:
         print('队列为空~')
         break
      # 从队列中读取数据
      result = queue.get()
      print(result)   

 if __name__ == '__main__':
   # 创建进程池
   pool = multiprocessing.Pool(2)
   # 创建进程队列
   queue = multiprocessing.Manager().Queue()
   # 在进程池中的进程间进行通信
   # 使用线程池同步的方式，先写后读
   # pool.apply(write_data, (queue, ))
   # pool.apply(read_data, (queue, ))
   # apply_async()   # 返回ApplyResult对象

   result = pool.apply_async(write_data, (queue))
   # ApplyResult对象wait() 方法，表示后续进程必须等待当前进程执行完再继续
   result.wait()
   pool.apply_async(read_data, (queue))
   pool.close()
   # 异步后，主线程不再等待子进程执行结束，再结束
   # join() 后，表示主进程会等候子进程执行结束后，再结束
   pool.join()

4 案例（文件copy器）
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

::

 import os
 import multiprocessing

 # 拷贝文件函数

 def copy_dir(file_name, source_dir, desk_dir):
   # 要拷贝文件路径
   source_path = source_dir+'/'+file_name
   # 目标路径
   desk_path = desk_dir + '/' + file_name
   # 获取文件大小
   file_size= os.path.getsize(source_path)
   # 纪录拷贝次数
   i = 0
   # 以二进制读取方式打开原文件
   with open(source_path, 'rb') as source_file:
      # 循环写入
      while True:
         # 读取1024字节
         file_data = source_file.read(1024)
         # 如果读到的不为空，则将读到的写入目标文件
         if file_data:
            desk_file.write(file_data)
            # 读取次数+1
            i+ = 1
            # 拷贝百分比进度等于拷贝次数*1024*100/文件大小
            n = i*102400/file_size
            if n >= 100:
               n = 100
            print(file_name, '拷贝进度%.2f%%'%n)
         else:
            print(file_name,"拷贝成功")
            break
 if __name__ == '__main__':
   # 要拷贝的文件夹
   source_dir = 'test'
   desk_dir = 'C:/Users/Administrator/Desktop/'+source_dir
   # 存在文件夹则不创建
   try:
      os.make(desk_dir)
   except:
      print('目标文件夹已存在，未创建')
   # 获取文件夹内文件目录，存到列表
   file_list = os.listdir(source_dir)
   print(file_list)
   # 创建进程池，最多运行3个子进程
   pool = multiprocessing.Pool(3)
   for file_name in file_list:
      # 异步方式添加到进程池内
      pool.apply_async(copy_dir, args=(file_name, source_dir, desk_dir))
   # 关闭进程池（停止添加，已添加的还可以运行）
   pool.close()
   # 让主进程阻塞，等待子进程结束
   pool.join()
   
Queue消息队列
====================

1.创建
>>>>>>>>>>>

::

 from multiprocessing import Queue
 queue = Queue(3) # 初始化Queue对象

2.方法
>>>>>>>>>>>>

- put() 向队列中添加一条消息
- get() 获取队列中的一条消息，然后从队列中移除
- full() 如果队列为满，返回True,反之False
- empty() 如果队列为空，返回True,反之False
- qsize() 返回当前队列包含的消息数量
- get_nowait()
- put_nowait() 如果block 值为False，消息队列如果没有空间可以写入，则立刻抛出Queue.Full异常


3.进程通信
>>>>>>>>>>>>>>>>>>>>>

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
         print('---队列已空---')
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

4.进程池间的通信
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

::

 from multiprocessing import Manager,Pool
 import os,time,random

 def reader(q):
   print("reader 启动(%s),父进程为(%s)"%(os.getpid(),os.getppid()))
   for i in range(q.qsize()):
      print("reader从Queue获取到消息：%s"%q.get(True))

 def writer(q):
   print("writer启动(%s),父进程为(%s)"%(os.getpid(),os.getppid()))
   for i in "DoGet":
      q.put(i)

 if __name__ == "__main__":
   print("(%s) start"%os.getpid())
   q = Manager().Queue()
   po = Pool()
   # 使用阻塞模式创建进程，这样就不需要在reader中使用死循环，可以让writer完全执行完成后，再用reader
   po.apply(writer,(q,))
   po.apply(reader,(q,))
   po.close()
   po.join()
   print("%s End"%os.getpid())

参考文档
====================

CSDN：https://blog.csdn.net/zsh142537/article/details/82556147
Python 基于Readis 的消息队列：https://blog.csdn.net/luoganttcc/article/details/81260015



