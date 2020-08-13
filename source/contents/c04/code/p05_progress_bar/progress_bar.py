import time
import sys


def general_progress_bar():
    """
    普通进度条
    """
    for i in range(1, 101):
        print("\r", end="")
        print("Download progress:{}%".format(i), "▋ "*(i//2), end="")
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n"+"执行结束".center(50//2, "-"))


def time_progress_bar():
    # 带时间进度条
    scale = 50
    start = time.perf_counter()
    for i in range(scale+1):
        a = "*"*i
        b = "."*(scale-i)
        c = (i/scale)*100
        dur = time.perf_counter()-start
        print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end="")
        time.sleep(0.1)
    print("\n"+"执行结束".center(scale//2, "-"))


def tpdm_progress_bar():
    # tpdm进度条
    from tqdm import tqdm
    for i in tqdm(range(1, 500)):
        # 模拟任务
        time.sleep(0.01)
    time.sleep(0.5)


def progress_bar():
    # progress进度条
    from progress.bar import IncrementalBar
    mylist = [1, 2, 3, 4, 5, 6, 7, 8]
    bar = IncrementalBar("Countdown", max=len(mylist))
    for item in mylist:
        bar.next()
        time.sleep(1)
        bar.finish()


def alive_progress_bar():
    # alive_progress进度条
    from alive_progress import alive_bar
    items = range(100)
    with alive_bar(len(items)) as bar:
        for item in items:
            # process each item
            bar()
            time.sleep(0.1)


def gui_progress_bart():
    import PySimpleGUI as sg
    mylist = [1, 2, 3, 4, 5, 6, 7, 8]
    for i, item in enumerate(mylist):
        sg.one_line_progress_meter(
            'This is my progress meter!', i+1, len(mylist), '-key-')
        time.sleep(1)


if __name__ == "__main__":
    # general_progress_bar()

    # time_progress_bar()
    # tpdm_progress_bar()
    # progress_bar()
    # alive_progress_bar()
    gui_progress_bart()
