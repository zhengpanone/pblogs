from collections.abc import Iterator


class Descend(Iterator):

    def __init__(self, N):
        self.N = N
        self.a = 0

    def __next__(self):
        while self.a < self.N:
            self.N -= 1
            return self.N

        raise StopIteration


if __name__ == "__main__":
    descend_iter = Descend(10)

    for i in descend_iter:
        print(i)
