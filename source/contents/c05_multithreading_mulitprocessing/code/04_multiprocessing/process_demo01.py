from multiprocessing import Process
import time

def test():
    while True:
        print("-----test--------")
        time.sleep(1)


if __name__ == '__main__':
    p = Process(target=test)
    p.start()  # 让这个进程开始执行test函数中的代码
    p.join()   # 等待进程实例执行结束后继续执行，即堵塞

    while True:
        print("--------main----------")
        time.sleep(1)
