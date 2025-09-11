import operator as op

if __name__ == "__main__":
  
  # 列表原地扩展
  my_list = [1, 2, 3]
  op.iconcat(my_list, [4, 5])
  print(my_list)  # [1, 2, 3, 4, 5]

  # 字典原地合并
  d1 = {"a": 1}
  d2 = {"b": 2}
  op.ior(d1, d2)
  print(d1)  # {'a': 1, 'b': 2}