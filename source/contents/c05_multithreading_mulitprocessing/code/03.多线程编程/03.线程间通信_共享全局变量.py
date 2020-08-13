from threading import Thread
import time
# from . import 03.多个线程共享一个全局变量
# 坑, 不可以直接导入变量,这样的话当其他线程修改全局变量,实际导入的变量没有同步,导致变量不一致
# 通过导包来.变量的话就不会存在这个问题

# detail_url_list = 03.多个线程共享一个全局变量.detail_url_list

detail_url_list =[]
def get_detail_html(detail_url_list):
    # global detail_url_list
    while True:
        if len(detail_url_list):
            url = detail_url_list.pop()
            print("get detail html started")
            time.sleep(2)


def get_detail_url(detail_url_list):
    while True:
        # global detail_url_list
        print("get detail url started")
        time.sleep(4)
        for i in range(20):
            detail_url_list.append("http://projectsedu.com/{id}".format(id=i))
        print("get detail url end")


if __name__ == "__main__":
    start_time = time.time()
    thread_detail_url = Thread(target=get_detail_url, args=(detail_url_list,))
    thread_detail_url.start()
    for i in range(10):
        html_thread = Thread(target=get_detail_html, args=(detail_url_list,))
        html_thread.start()

    print("last time: {}".format(time.time()-start_time))
