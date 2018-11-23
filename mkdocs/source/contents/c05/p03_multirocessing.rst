===========================
5.3 多进程编程
===========================

multiprocessing
=============

python 中的多线程并不是真正的多线程，如果想要重分利用多核CPU资源，在python中大部分情况使用的是多进程。Python提供了非常好用的多进程包multiprocessing，只需要定义一个函数，Python会完成其他所有事情。借助这个包，可以轻松完成从单进程到并发执行的转换。multiprocessing支持子进程、通信和共享数据、执行不同形式的同步，提供了Process、Queue、Pipe、Lock等组件。

1. Process
==========

**创建进程类**：Process(group[,target[,name[,args[,kwargs]]]]])，target表示调用对象，args表示调用对象的位置参数元组。kwargs表示调用对象的字典。name为别名。group实质上不使用。

**方法**：is_alive()、join([timeout])、run()、start()、terminate()。其中Process以start()启动某个进程。

**属性**：authkey、daemon（要通过start()设置、exitcode(进程在运行是为None、如果为-N，表示被信号N结束)、name、pid。其中daemon是父进程终止后自动终止，且自己不能产生新进程，必须在start()之前设置）

1.1 创建函数并将其作为单个进程：
>>>>>>>>>>>>>>>>>>>>>>

::

 import multiprocessing
 import time

 def worker(interval):
    n = 5
    while n > 0:
        print("The time is {0}".format(time.ctime()))
        time.sleep(interval)
        n -= 1

 if __name__ == "__main__":
    p = multiprocessing.Process(target=worker，args = (3,))
    p.start()
    print("p.pid:",p.pid)
    print("p.name:",p.name)
    print("p.is_alive:",p.is_alive)




>>> p.pid 29297
        p.name Process-1
        p.is_alive <bound method BaseProcess.is_alive of <Process(Process-1, started)>>
        The time is Fri Nov 23 18:42:57 2018
        The time is Fri Nov 23 18:43:00 2018
        The time is Fri Nov 23 18:43:03 2018
        The time is Fri Nov 23 18:43:06 2018
        The time is Fri Nov 23 18:43:09 2018

1.2 创建函数并将其作为多个进程
>>>>>>>>>>>>>>>>>>>>>>>

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
>>>>>>>>>>>>>>>

::

 import multiprocessing
 import time

 class ClockProcess(multiprocessing.process):
    def __int__(self,interval):
        multiprocessing.Process.__int__(self)
        self.interval = interval

    def run(self):
        n = 5
        while n > 0:
            print("the time is {0}".formate(time.ctime()))
            time.sleep(self.interval)
            n -= 1

 if __name__ == "__main__":
    p = ClockProcess(3)
    p.start()

>>>



