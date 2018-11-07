========================
7.1 类的定义
========================

1. 什么是类
# 下面代码是定义了一个Human类，继承自object类
# Python类可以继承自多个类，如

::

 class Human(object,orangOutang):
    
    species = "H. sapiens"  # 类属性

    __species = "Other.sapiens" #内部结构，无法被外部直接访问

    # __init__(),初始化函数，python中在对类进行处理时，会先处理以下函数，

    #其实就是系统默认定义了接口，而这个接口是开放给用户去实现的，具体如下：    

    #__init__  构造函数，在生成对象时调用
    # __del__   析构函数，释放对象时使用
    #__repr__ 打印，转换
    #__setitem__按照索引赋值
    #__getitem__按照索引获取值
    #__len__获得长度
    #__cmp__比较运算
    #__call__函数调用
    #__add__加运算
    #__sub__减运算
    #__mul__乘运算
    #__div__除运算
    #__mod__求余运算
    #__pow__称方

    def __init__(self, name):
        #声明类中的属性，并初始化，在初始化的时候同时
        #就是定义了变量类型
        self.name = name        # 对象属性  实例属性
        self.age = 0

    # 在类中所有函数都必须把self作为第一个参数
    #（下面定义的类方法和静态方法除外）
    def say(self, msg):
        return "{0}: {1}".format(self.name, msg)

    # 类方法
    @classmethod
    def get_species(cls):
        return cls.species

    # 静态方法，
    @staticmethod
    def grunt():
        return "*grunt*"

    # A property is just like a getter.
    # It turns the method age() into an read-only attribute
    # of the same name.
    #property属性，相当于getter
    @property
    def age(self):
        return self._age

    # This allows the property to be set
    @age.setter
    def age(self, age):
        self._age = age

    # This allows the property to be deleted
    @age.deleter
    def age(self):
        del self._age

 i = Human(name="Ian")          #类实例化

 dir(i)          # 查看对象 i中的所有属性
 
 print i.say("hi")    # prints out "Ian: hi"

 j = Human("Joel")
 
 print j.say("hello")  # prints out "Joel: hello"

 #调用实例方法用"."
 i.get_species()   # => "H. sapiens"

 # 改变类变量
 Human.species = "H. neanderthalensis"
 i.get_species()   # => "H. neanderthalensis"
 j.get_species()   # => "H. neanderthalensis"

 # 调用静态方法
 Human.grunt()   # => "*grunt*"

 # 给age赋值
 i.age = 42

 i.age # => 42   # 获取age值

 del i.age  # 删除age


类寻找属性或方法的流程：
实例.__dict__  > 类.__dict__ > 类.__getattr__ > 类.__getattribute__

1.2类的练习
----------------------------------

::

 class Foo(object):

    def __init__(self):
        pass

    def __getattr__(self,item):
        print(item)
        return self

    def __getattribute__(self,item):
        pass

    def __str__(self):
        return ""

    def say_hello(self):
        pass

 print(Foo().think.different.itcast)
