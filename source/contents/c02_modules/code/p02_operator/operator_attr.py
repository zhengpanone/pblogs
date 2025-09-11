import operator as op

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == "__main__":
  
  users = [
      User("Alice", 25),
      User("Bob", 30),
      User("Charlie", 20)
  ]

  # 按年龄排序
  get_age = op.attrgetter("age")
  sorted_users = sorted(users, key=get_age)
  print([u.name for u in sorted_users])  # ['Charlie', 'Alice', 'Bob']

  # 获取多个属性
  get_info = op.attrgetter("name", "age")
  print([get_info(u) for u in users])
  # 输出: [('Alice', 25), ('Bob', 30), ('Charlie', 20)]


