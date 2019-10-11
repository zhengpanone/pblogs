import threading
import time


def sayHello(name):
    print("Hello %s" % (name))
    time.sleep(2)
    print("执行")


if __name__ == "__main__":
    start = time.time()
    for i in range(5):
        th = threading.Thread(target=sayHello, args=("张三",))
        th.setDaemon(True) # 设置th为守护进程,当主进程退出,子进程也退出
        th.start()
    th.join() # 等待线程执行完才能向下继续执行
    # 当主线程退出时：子线程kill掉
    print("last time:{}".format(time.time()-start))
