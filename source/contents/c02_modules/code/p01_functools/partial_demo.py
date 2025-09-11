from functools import partial

# 原函数
def power(base,exponent):
  return base ** exponent

if __name__ == '__main__':

  # 创建平方函数，（固定exponent=2）
  square = partial(power, exponent=2)
  print(square(5)) # 输出： 25

  # 创建立方函数，（固定exponent=3）
  cube = partial(power, exponent=3)
  print(cube(5)) # 输出： 125


