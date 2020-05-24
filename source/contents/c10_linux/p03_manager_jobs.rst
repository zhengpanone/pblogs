====================================
3. Linux任务的前后台管理
====================================

常见的任务管理需求
============================

- 将进程切换到后台
- 将进程切换到前台
- 查看后台任务
- 终止后台任务

.. code:: C 

 #include <stdio.h>

 int main(){
     while (1){
         printf("hello world\n");
         sleep(1);
     }
 }

.. literalinclude:: ./code/p03/manage_job.sh
    :encoding: utf-8
    :language: shell
    :lines: 1-
    :emphasize-lines: 1
    :linenos:


运行上面的脚本,通过jobs -l 查看运行的脚本

查找后台运行程序
>>>>>>>>>>>>>>>>>>>>>

- ps -ef 或 ps -aux 结合grep过滤
- pstree -p 确认复杂进程树结构
- lsof -i 8080 查获端口获得进程号
- netstat -anp | grep 8080 查看端口获得进程号


将正在执行前台任务放到后台
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

1、 ctrl + z  将一个正在前台执行的命令放到后台，并且处于暂停状态

2、jobs -l # 查看任务，返回任务编号 和 进程号

2、bg %jobnumber # 将一个在后台暂停的命令，变成在后台继续执行。如果后台中有多个命令，可以用 bg %jobnumber 将选中的命令调出。

4、fg %jobnumber # 将后台中的命令调至前台继续运行。如果后台中有多个命令，可以用 fg %jobnumber（是命令编号，不是进程号）将选中的命令调出

::

 [alvin@VM_0_16_centos test]$ jobs -l
 [1]   1788 Running                 ./hello1 > test1.txt &
 [2]-  1801 Running                 ./hello2 > test2.txt &
 [3]+  1844 Running                 ./hello3 > test3.txt &

将hello2调至前台运行

::

 [alvin@VM_0_16_centos test]$ fg %2
 ./hello2 > test2.txt

其中，%后面跟的是后台任务的序列，而不是进程ID。如果只有 fg 命令（ bg 命令也一样），而不跟参数，那么将操作的是后台任务列表里的第一个任务，专业名词叫 当前任务 。

我们会发现，这时程序会一直卡在终端。这时，我们可以使用 ctrl+z 将它再次切到后台运行。

::

 ^Z
 [2]+  Stopped                 ./hello2 > test2.txt
 [alvin@VM_0_16_centos test]$ jobs -l
 [1]   1788 Running                 ./hello1 > test1.txt &
 [2]+  1801 Stopped                 ./hello2 > test2.txt
 [3]-  1844 Running                 ./hello3 > test3.txt &


但是，我们会发现，test2 进程变成了 stopped 的状态，我们也可以在后台进程列表里看到它的状态。这也是 ctrl+z 命令的特点：将进程切换到后台，并停止运行。

如果我们想让它恢复运行，我们就可以使用 bg 命令了。

::

 [alvin@VM_0_16_centos test]$ bg %2
 [2]+ ./hello2 > test2.txt &
 [alvin@VM_0_16_centos test]$ jobs -l
 [1]   1788 Running                 ./hello1 > test1.txt &
 [2]-  1801 Running                 ./hello2 > test2.txt &
 [3]+  1844 Running                 ./hello3 > test3.txt &

如果我们想杀死某个后台进程，我们可以使用 kill 命令。kill 命令的用法有两种：

1. kill -9 pid

2. kill -9 %N

例如，我们要杀死 hello2 进程的话，可以这样操作：

1. kill 1801
2. kill %2

执行完毕之后，它的状态将变成 terminated 状态：

::

 [alvin@VM_0_16_centos test]$ kill 1801
 [alvin@VM_0_16_centos test]$ jobs -l
 [1]   1788 Running                 ./hello1 > test1.txt &
 [2]-  1801 Terminated              ./hello2 > test2.txt
 [3]+  1844 Running                 ./hello3 > test3.txt &

ps命令
==================

-A ：所有的进程均显示出来

-a ：不与terminal有关的所有进程

-u ：有效用户的相关进程

-x ：一般与a参数一起使用，可列出较完整的信息

-l ：较长，较详细地将PID的信息列出

ps aux # 查看系统所有的进程数据

ps ax # 查看不与terminal有关的所有进程

ps -lA # 查看系统所有的进程数据

ps axjf # 查看连同一部分进程树状态


nohup和&使用
============================

.. code-block:: shell
    :linenos:

    # 自定义输出文件(标准输出和错误输出合并到main.log)
    nohup python main.py >> main.log 2>&1 &

    # 上一个例子的简化写法
    nohup python main.py &> main.log &

    # 不记录输出信息
    nohup python main.y &> /dev/null &

    # 只保留输出错误信息
    nohup python main.py > /dev/null 2>main.log &

    # 不记录输出信息并将程序进程号写入 pidfile.txt文件中，方便后续杀死进程
    nohup python main.py &> /dev/null & echo $! > pidfile.txt 


公众号：良许Linux_

.. _良许Linux: https://mp.weixin.qq.com/s?__biz=MzU3NTgyODQ1Nw==&mid=2247485143&amp;idx=1&amp;sn=2726e5d4de6abc6e09a2408739cd1593&source=41#wechat_redirect


