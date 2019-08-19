=========================
8. Python GIL
=========================

GIL(Global Interpreter Lock)
原理
============

Python是动态解释性语言，即解释运行。运行Python代码时都会通过Python解释器解释执行，Python官方默认的解释器是Cython,当然你也可以选择自己的Python解释器(PyPy,JPython),其中JPython就没有GIL的限制。在解释器解释执行任何Python代码时，首先都需要they acquire GIL when running，release GIL when blocking for I/O。如果没有涉及I/O操作，只是CPU密集型操作或者，解释器会每隔100 ticks(低级的解释器指令)就释放GIL(通过 sys.setcheckinterval来修改)。GIL是实现Python解释器(Cython)时所引入的一个概念。GIL不是Python的特性。 

三个线程”协作式“执行，当Thread1执行时它获得GIL，其它线程一直在等待；当遇到I/O处理时，Thread1会释放GIL，Thread2得到GIL，Thread2开始运行，如此反复直到任务完成。当任一个线程正在运行时，它控制着GIL，并且在处理I/O(read,write,send,recv,etc.)时释放GIL。CPU密集型(不提供I/O操作)的线程作为特殊的情况被处理，即每运行100个低级的解释器指令进行检查并根据线程优先级进行释放/重新获取或者释放GIL。

::

 import threading
 import time

 def count(n):
    while n>0:
        n-=1

 if __name__ == "__main__":
    t1 = time.time()
    count(10000000)
    count(10000000)
    t2 = time.time()
    print t2-t1
    a = threading.Thread(target=count,args=(10000000,))
    a.start()
    b = threading.Thread(target=count,args=(10000000,))
    b.start()
    a.join()
    b.join()
    t3 = time.time()
    print t3-t2

 # 输出结果
 11.5187261105
 18.4223148823

上述的例子是一个很典型的CPU密集任务，threading是Python高级别的线程库，Count只是普通的函数运行在一个主线程内。这就是为什么Python多线程的并不是真正意义上的多线程。Python的Thread是真实操作系统的Thread，两者没有差别。在Linux下是由pthreads实现的，而在windows下是由Windows threads实现的，并通过操作系统调度算法进行调度。为了充分利用CPU，python计算当前已执行了多少数量的指令达到阈值就会立即(100 ticks)来释放GIL。
我们分析一下程序问题：
count函数里面主要做的是计算,I/O操作一直没有触发，那么就会一直等待知道100 ticks才会释放GIL。从release GIL到acquire GIL之间几乎是没有间隙的。所以在其他核心上的线程被唤醒时，大部分情况下主线程已经又再一次获取到GIL了。这个时候被唤醒执行的线程只能白白的浪费CPU时间，看着另一个线程拿着GIL欢快的执行着。然后达到切换时间后进入待调度状态，再被唤醒，再等待，以此往复恶性循环。

如何避免GIL影响
===================================

- CPU密集型下的任务尽量采用多进程处理(multiprocessing).

- 如果你不想使用Cython解释器，就没有这个限制，同样很多Cython的特性你也放弃了。

- 利用 ctypes 绕过 GIL.ctypes会在调用C函数前释放GIL,可以通过ctypes和C动态库来让 python充分利用物理内核的计算能力。
