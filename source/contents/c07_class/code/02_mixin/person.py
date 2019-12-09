class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

# 我们可以通过调用实例属性的方式来访问：

p = Person("小陈", "男", 18)
print(p.name)  # "小陈"