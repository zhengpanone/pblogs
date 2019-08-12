========================
23.1 python 执行系统命令
========================

1. os.system 方法
-----------------------------------------

os.system(cmd)

在子终端运行系统命令，可以获取命令执行后的返回信息以及执行返回的状态

::

 >>> import os
 >>> os.system('date')
 2018年 4月 8日 星期日 19时29分13秒 CST
 0  #运行状态号，0表示正确

执行后返回两行结果，第一行是结果， 第二行是执行状态信息

2. os.popen方法
--------------------------------------------

os.popen(cmd)
不仅执行命令而且返回执行后的信息对象(常用于需要获取执行命令后的返回信息)，是通过一个管道文件将结果返回

::

 >>> import os
 >>> nowtime = os.popen('date')
 >>> print(nowtime.read())
 2018年 4月 8日 星期日 19时30分35秒 CST

3. commands 模块
-------------------------------

方法                            说明
getoutput                   获取执行命令后的返回信息
getstatus                    获取执行命令的状态值(执行命令成功返回数值0，否则返回非0)
getstatusoutput         获取执行命令的状态值以及返回信息

::

 >>> import commands
 >>> status,output = commands.getstatusoutput('date')
 >>> print(status)  #0
 >>> print(output)  #2018年 4月 8日 星期日 19时31分45秒 CST

注意1：在类unix的系统下使用此方法返回的返回值（status）与脚本或命令执行之后的返回值不等，这是因为调用了os.wait()的缘故，具体原因就得去了解下系统wait()的实现了。需要正确的返回值（status），只需要对返回值进行右移8位操作就可以了。
注意2：当执行命令的参数或者返回中包含了中文文字，那么建议使用subprocess。


4. subprocess模块
------------------------------

运用对线程的控制和监控，将返回的结果赋于一变量，便于程序的处理。有丰富的参数可以进行配置，可供我们自定义的选项多，灵活性高。之前我使用os.system的时候遇到文件描述符被子进程继承的问题，后来通过close_fds = False 这个参数来解决的。官方文档：http://python.usyiyi.cn/python_278/library/subprocess.html

::

 >>> import subprocess
 >>> top = subprocess.Popen('date',shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
 >>> print(nowtime.stdout.read())
 2018年 4月 8日 星期日 19时32分41秒 CST



参考文档
----------

- python执行系统命令四种方法比较：https://www.pythontab.com/html/2018/pythonjichu_0408/1273.html