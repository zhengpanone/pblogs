from threading import Thread, Lock
import time

g_num = 0


def work1():
    global g_num
    for i in range(1000000):
        mutex.acquire()
        g_num += 1
        mutex.release()

    print("--------in work1,g_num %d----------------" % g_num)


def work2():
    global g_num
    for i in range(1000000):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("--------in work2,g_num %d----------------" % g_num)


mutex = Lock()  # 创建互斥锁，默认是没有上锁的

t1 = Thread(target=work1)
t1.start()
# time.sleep(3)
t2 = Thread(target=work2)
t2.start()
t1.join()
t2.join()
print("------g_num=%d---------" % g_num)
