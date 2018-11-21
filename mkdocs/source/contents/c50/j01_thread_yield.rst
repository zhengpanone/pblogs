========================
50.1 Thread.yield
========================

1. 概念
---------

start() 方法是启动线程，让线程变成就绪状态等待 CPU 调度后执行。
yield 即 "谦让"，也是 Thread 类的方法。它让掉当前线程 CPU 的时间片，使正在运行中的线程重新变成就绪状态，并重新竞争 CPU 的调度权。它可能会获取到，也有可能被其他线程获取到。

::

 package com.zp;

 /**
 * 引用公众号： Java技术栈
 * url:https://mp.weixin.qq.com/s/INwudC6IWFj0mKmqqU_eJg
 * 多线程 Thread.yield 方法
 */

 public class ThreadYieldTest {
    public static void main(String[] args) {
        Runnable runnable = () -> {
            for (int i = 0; i <= 100; i++) {
                System.out.println(Thread.currentThread().getName() + "-------------" + i);
                if (i % 20 == 0) {
                    Thread.yield();
                }
            }

        };
 /*        new Thread(runnable, "栈长").start();
        new Thread(runnable, "小密").start();*/
        Thread thread1 = new Thread(runnable, "栈长");
        Thread thread2 = new Thread(runnable, "小密");
        thread1.setPriority(Thread.MIN_PRIORITY);
        thread2.setPriority(Thread.MAX_PRIORITY);

        thread2.start();
        thread1.start();


    }
 }

这个示例每当执行完 20 个之后就让出 CPU，每次谦让后就会马上获取到调度权继续执行。
如果我们把两个线程加上线程优先级，那输出的结果又不一样。

::

 thread1.setPriority(Thread.MIN_PRIORITY);
 thread2.setPriority(Thread.MAX_PRIORITY);

因为给小蜜加了最高优先权，栈长加了最低优先权，即使栈长先启动，那小蜜还是有很大的概率比栈长先会输出完的

2. yield 和sleep的异同
-----------------------------

1. yield, sleep 都能暂停当前线程，sleep 可以指定具体休眠的时间，而 yield 则依赖 CPU 的时间片划分。
#. yield, sleep 两个在暂停过程中，如已经持有锁，则都不会释放锁资源。
#. yield 不能被中断，而 sleep 则可以接受中断。

3. 结论
---------

yield 方法可以很好的控制多线程，如执行某项复杂的任务时，如果担心占用资源过多，可以在完成某个重要的工作后使用 yield 方法让掉当前 CPU 的调度权，等下次获取到再继续执行，这样不但能完成自己的重要工作，也能给其他线程一些运行的机会，避免一个线程长时间占有 CPU 资源。

参考文档
------------

Java技术栈：https://mp.weixin.qq.com/s/INwudC6IWFj0mKmqqU_eJg
github: https://github.com/zhengpanone/SpringBootLearn/blob/master/MyBlogs/src/test/java/com/zp/ThreadYieldTest.java





