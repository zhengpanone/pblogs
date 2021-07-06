from multiprocessing import Process
import time
import os


class ClockProcess(Process):
    def __int__(self, interval: int):
        super().__init__(self)
        self.interval = interval

    def run(self):
        print("子进程(%s)开始执行，父进程为(%s)" % (os.getpid(), os.getppid()))
        t_start = time.time()
        time.sleep(self.interval)
        t_stop = time.time()
        print("(%s)执行结束，耗时%0.2f秒" % (os.getpid(), t_stop-t_start))


if __name__ == "__main__":
    t_start = time.time()
    print("当前程序进程(%s)" % os.getpid())
    p1 = ClockProcess(interval=2)
    # 对一个不包含target属性的Process类执行start()方法，就会运行这个类中的run()方法
    p1.start()
