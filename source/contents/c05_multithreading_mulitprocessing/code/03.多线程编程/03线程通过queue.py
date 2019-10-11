from threading import Thread
import time
from queue import Queue


def get_detail_html(queue):
    # global detail_url_list
    while True:
        url = queue.get()
        print("get detail html started")
        time.sleep(2)


def get_detail_url(queue):
    while True:
        # global detail_url_list
        print("get detail url started")
        time.sleep(4)
        for i in range(20):
            queue.put("http://projectsedu.com/{id}".format(id=i))
        print("get detail url end")


if __name__ == "__main__":
    detail_url_queue = Queue(maxsize=1000)
    # Queue是线程安全的
    start_time = time.time()
    thread_detail_url = Thread(target=get_detail_url, args=(detail_url_queue,))
    thread_detail_url.start()
    for i in range(10):
        html_thread = Thread(target=get_detail_html, args=(detail_url_queue,))
        html_thread.start()

    # detail_url_queue.task_done() 先调用task_done
    # detail_url_queue.join() 后调用join ,join会阻塞主线程

    print("last time: {}".format(time.time()-start_time))
