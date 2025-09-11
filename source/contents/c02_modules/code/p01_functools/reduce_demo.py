from functools import reduce

# 计算阶乘
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))
  
# 连接字符串
def join_strings(words):
    return reduce(lambda x, y: x +' '+ y, words)
  
if __name__ == '__main__':
  words = ['Python', 'is', 'awesome']
  sentence =join_strings(words)
  print(sentence)
  print(factorial(5))
  