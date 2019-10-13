import threading
from threading import RLock

lock = RLock()
total = 0
def add():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        lock.acquire()
        total += 1
        lock.release()
        lock.release()

def desc():
    global lock
    global total
    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()

thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(total)
