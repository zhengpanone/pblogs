class Data:
    def __init__(self, x):
        self._x = x
        self._cached = None

    @property
    def heavy_calc(self):
        if self._cached is None:
            print("第一次计算...")
            self._cached = self._x ** 2
        return self._cached

if __name__ == '__main__':
  d = Data(10)
  print(d.heavy_calc)  # 第一次计算... → 100
  print(d.heavy_calc)  # 直接返回缓存 → 100