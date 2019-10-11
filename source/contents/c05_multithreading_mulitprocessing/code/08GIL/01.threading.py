import threading
import time

def count(n):
    while n > 0:
        n -= 1

if __name__ == "__main__":
    t1 = time.time()
    count(10000000)
    count(10000000)
    t2 = time.time()
    print(t2-t1)
    a = threading.Thread(target=count, args=(10000000,))
    a.start()
    b = threading.Thread(target=count, args=(10000000,))
    b.start()
    a.join()
    b.join()
    t3 = time.time()
    print(t3-t2)
