# 事件循环+回调(驱动生成器)+epoll(IO多路复用)
# asyncio 是python用于解决异步io编程的一整套解决方案
# tornado 、gevent、twisted 、scrapy、django channels

import asyncio

'''
async def get_html(url: str):
    print("start get url")
    # time.sleep(10) 这个是同步阻塞
    await asyncio.sleep(2)
    print("end get url")

if __name__ == "__main__":
    import time
    start_time = time.time()
    loop = asyncio.get_event_loop()
    tasks = [get_html('http://www.baidu.com') for i in range(10)]
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time()-start_time)
'''

'''
# 获取返回值
async def get_html(url: str):
    print("start get url")
    # time.sleep(10) 这个是同步阻塞
    await asyncio.sleep(2)
    print("end get url")
    return "get html done"


def callback(url: str,future) -> None:
    print(url)
    print("send email to someone")


if __name__ == "__main__":
    import time
    start_time = time.time()
    loop = asyncio.get_event_loop()

    # 获取返回值
    # asyncio.ensure_future()
    # get_future = asyncio.ensure_future(get_html('http://www.baidu.com'))
    # loop.run_until_complete(get_future)
    # print(get_future.result())

    # loop.create_task()
    task = loop.create_task(get_html('http://www.baidu.com'))
    from functools import partial
    task.add_done_callback(partial(callback, "http://www.baidu.com"))
    loop.run_until_complete(task)
    print(task.result())
'''

# wait gather


async def get_html(url: str):
    print("start get url")
    # time.sleep(10) 这个是同步阻塞
    await asyncio.sleep(2)
    print("end get url")

if __name__ == "__main__":
    import time
    start_time = time.time()
    loop = asyncio.get_event_loop()
    task = [get_html('http://www.baidu.com') for i in range(10)]
    # loop.run_until_complete(asyncio.wait(task))
    # loop.run_until_complete(asyncio.gather(*task))
    # print(time.time()-start_time)

    # gather 和wait的区别
    # gather 更加高层
    task1 = [get_html('http://www.baidu.com') for i in range(10)]
    task2 = [get_html('http://www.baidu.com') for i in range(10)]
    loop.run_until_complete(asyncio.gather(*task1, *task2))
    print(time.time()-start_time)
