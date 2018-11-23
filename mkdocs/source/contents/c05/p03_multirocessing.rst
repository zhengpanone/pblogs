===========================
5.3 多进程编程
===========================

multiprocessing
=============

python 中的多线程并不是真正的多线程，如果想要重分利用多核CPU资源，在python中大部分情况使用的是多进程。Python提供了非常好用的多进程包multiprocessing，只需要定义一个函数，Python会完成其他所有事情。借助这个包，可以轻松完成从单进程到并发执行的转换。multiprocessing支持子进程、通信和共享数据、执行不同形式的同步，提供了Process、Queue、Pipe、Lock等组件。

1.Process
==========

**创建进程类**：Process(group[,target[,name[,args[,kwargs]]]]])，target表示调用对象，args表示调用对象的位置参数元组。kwargs表示调用对象的字典。name为别名。group实质上不使用。

**方法**：is_alive()、join([timeout])、run()、start()、terminate()。其中Process以start()启动某个进程。

**属性**：authkey、daemon（要通过start()设置、exitcode(进程在运行是为None、如果为-N，表示被信号N结束)、name、pid。其中daemon是父进程终止后自动终止，且自己不能）