import operator as op

if __name__ == "__main__":
  
  text = "Hello World"

  # 调用字符串方法
  upper_caller = op.methodcaller("upper")
  print(upper_caller(text))  # "HELLO WORLD"

  # 带参数的方法调用
  split_caller = op.methodcaller("split", " ")
  print(split_caller(text))  # ['Hello', 'World']