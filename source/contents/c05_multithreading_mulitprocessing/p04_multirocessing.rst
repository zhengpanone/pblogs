===========================
4. 多进程编程
===========================

multiprocessing
=======================

python 中的多线程并不是真正的多线程，如果想要重分利用多核CPU资源，在python中大部分情况使用的是多进程。Python提供了非常好用的多进程包multiprocessing，只需要定义一个函数，Python会完成其他所有事情。借助这个包，可以轻松完成从单进程到并发执行的转换。multiprocessing支持子进程、通信和共享数据、执行不同形式的同步，提供了Process、Queue、Pipe、Lock等组件。

1. Process
=============

**创建进程类**：Process(group[,target[,name[,args[,kwargs]]]]])，target表示调用对象，args表示调用对象的位置参数元组。kwargs表示调用对象的字典。name为别名。group实质上不使用。

**方法**：is_alive()、join([timeout])、run()、start()、terminate()。其中Process以start()启动某个进程。

**属性**：authkey、daemon（要通过start()设置、exitcode(进程在运行是为None、如果为-N，表示被信号N结束)、name、pid。其中daemon是父进程终止后自动终止，且自己不能产生新进程，必须在start()之前设置）

- join([timeout]) 是否等待进程实例执行结束，或等待多少秒
- is_alive() 判断进程实例是否还在执行
- start() 启动进程实例
- run() 如果没有给定target参数，这个对象调用start()方法时，就执行对象中的run()方法
- terminate() 不管任务是否完成，立即终止

1.1 创建函数并将其作为单个进程：
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

::

 from multiprocessing import Process
 import time

 def test():
   while True:
      print("-----test--------")
      time.sleep(1)

 p = Process(target=test)
 p.start()  # 让这个进程开始执行test函数中的代码
 p.join()   # 等待进程实例执行结束后继续执行，即堵塞

 while True:
   print("--------main----------")
   time.sleep(1)

1.2 创建函数并将其作为多个进程
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

::

 import multiprocessing
 import time

 def worker_1(interval):
    print("worker_1")
    time.sleep(interval)
    print("end_worker_1")

 def worker_2(interval):
    print("worker_2")
    time.sleep(interval)
    print("end_worker_2")

 def worker_3(interval):
    print("worker_3")
    time.sleep(interval)
    print("end_worker_3")

 if __name__ == "__main__":
    p1 = multiprocessing.Process(target=worker_1,args=(2,))
    p2 = multiprocessing.Process(target=worker_2,args=(2,))
    p3 = multiprocessing.Process(target=worker_3,args=(4,))

    p1.start()
    p2.start()
    p3.start()

    print("The number of CPU is："+str(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print("child p.name"+ p.name + "\t p.id"+str(p.pid))
    print("END！！！！！")


>>> The number of CPU is:16
    child p.name:Process-1	 p.id9792
    child p.name:Process-3	 p.id9794
    worker_1
    child p.name:Process-2	 p.id9793
    END!!!!
    worker_2
    worker_3
    end worker_1
    end worker_2
    end worker_3

1.3 将进程定义为类
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

继承Process类，重写__init__方法，并且完全初始化一个Process类即：将继承类本身传递为Process.__int__方法，完成初始化，重写Processe类的run()方法

::

 from multiprocessing import Process
 import time

 class ClockProcess(Process):
    def __int__(self,interval):
        Process.__int__(self) 
        self.interval = interval

    def run(self):
         print("子进程(%s)开始执行，父进程为(%s)"%(os.getpid(),os.getppid()))
         t_start = time.time()
         time.sleep(self.interval)
         t_stop = time.time()
         print("(%s)执行结束，耗时%0.2f秒"%(os.getpid(),t_stop-t_start))
      

 if __name__ == "__main__":
   t_start = time.time()
   print("当前程序进程(%s)"%os.getpid())
   p1 = ClockProcess(2)
   # 对一个不包含target属性的Process类执行start()方法，就会运行这个类中的run()方法
   p.start()

dummy
============================





参考文档
==============

博客园：https://www.cnblogs.com/kaituorensheng/p/4445418.html
https://blog.csdn.net/topleeyap/article/details/78981848
https://blog.csdn.net/u014556057/article/details/61616902

 涛哥聊Python_:`_https://mp.weixin.qq.com/s/dlJXV4mmDe2CjFQ_at1_6w`

