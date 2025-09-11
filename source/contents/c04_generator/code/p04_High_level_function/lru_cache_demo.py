from functools import lru_cache
import time

@lru_cache(maxsize=128) # 缓存最近128个结果
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
  
if __name__ == '__main__':
  
  # 首次计算（慢）
  start = time.time()
  print(fibonacci(300))
  print(f'首次计算耗时：{time.time() - start:.4f}s')
  
  # 再次计算（快）
  start = time.time()
  print(fibonacci(300))
  print(f'再次计算耗时：{time.time() - start:.4f}s')