class Person(MappingMixin, ReprMixin):

    def __init__(self, name, gender, age):
        
        self.name = name
        self.gender = gender
        self.age = age

# 这样这个子类混入了两种功能：
p = Person("小陈", "男", 18)
print(p['name'])  # "小陈"
print(p)  # Person(name=小陈, gender=男, age=18)