def w1(func):
    print("----------正在装饰---------------")

    def inner():
        print("--------验证权限--------------")
        return func()
    return inner


@w1
def f1():
    print("--------f1-------------")
