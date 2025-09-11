from functools import wraps

def my_decorator(func):
  @wraps(func) # 保留被装饰函数的元信息
  def wrapper(*args, **kwargs):
    print('函数被调用之前！')
    return func(*args, **kwargs)
  return wrapper

@my_decorator
def example():
  """这是一个示例函数"""
  pass

if __name__ == '__main__':

  print(example.__name__)
  print(example.__doc__)