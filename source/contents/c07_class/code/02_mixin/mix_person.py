class Person(MappingMixin):
    def __init__(self, namem, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

# 现在 Person 拥有另一种调用属性方式了：

p = Person("小陈", "男", 18)
print(p['name'])  # "小陈"
print(p['age'])  # 18