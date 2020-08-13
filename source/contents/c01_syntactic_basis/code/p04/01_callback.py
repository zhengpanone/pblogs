class A():
    def __call__(self):
        return object()


class B():
    def run(self):
        return object()


def func():
    return object()


def main(callable):  # 可调用对象
    print(callable())
    # 在main 中调用传入的参数，得到一个对象object
    # b.run()
    # func()
    # ...


if __name__ == "__mian__":
    print("====")
    main(A())
    main(B())
    main(func)
