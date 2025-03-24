===========================
多进程编程
===========================


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

.. literalinclude:: ./code/04_multiprocessing/process_demo01.py
    :encoding: utf-8
    :language: python
    :linenos:


1.2 创建函数并将其作为多个进程
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. literalinclude:: ./code/04_multiprocessing/process_demo02.py
    :encoding: utf-8
    :language: python
    :linenos:

1.3 将进程定义为类
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

继承Process类，重写__init__方法，并且完全初始化一个Process类即：将继承类本身传递为Process.__int__方法，完成初始化，重写Processe类的run()方法

.. literalinclude:: ./code/04_multiprocessing/process_demo03.py
    :encoding: utf-8
    :language: python
    :linenos:



dummy
============================





参考文档
==============

博客园：https://www.cnblogs.com/kaituorensheng/p/4445418.html
https://blog.csdn.net/topleeyap/article/details/78981848
https://blog.csdn.net/u014556057/article/details/61616902

涛哥聊Python: https://mp.weixin.qq.com/s/dlJXV4mmDe2CjFQ_at1_6w

