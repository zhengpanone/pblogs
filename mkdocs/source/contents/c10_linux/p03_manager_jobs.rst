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

运行上面的脚本,通过jobs -l查看运行的脚本

.. note::

 jobs -l 

::

 [alvin@VM_0_16_centos test]$ jobs -l
 [1]   1788 Running                 ./hello1 > test1.txt &
 [2]-  1801 Running                 ./hello2 > test2.txt &
 [3]+  1844 Running                 ./hello3 > test3.txt &

将hello2调至前台运行

::

 alvin@VM_0_16_centos test]$ fg %2
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

1. kill pid
2. kill %N

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


公众号：`良许Linux`__

.. _Linux: https://mp.weixin.qq.com/s?__biz=MzU3NTgyODQ1Nw==&mid=2247485143&amp;idx=1&amp;sn=2726e5d4de6abc6e09a2408739cd1593&source=41#wechat_redirect
__ Linux

