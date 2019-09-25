def w1(func):
    print("------正在进行装饰1-------")

    def inner():
        print("-------------正在进行权限验证1-------------")
        func()
    return inner


def w2(func):
    print("--------正在进行装饰2-------------")

    def inner():
        print("----------正在进行权限验证2------------")
        func()
    return inner

# 在f1调用之前，已经进行装饰了
@w1
@w2
def f1():
    print("--------f1---------")

    f1()
