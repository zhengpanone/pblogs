========================================
1.5 动态添加属性和方法
========================================

1. 动态给实例和类添加属性
---------------------------------------

::

 class Person:
  def __init__(self,name):
    self.name=name

 p = Person("张三")

 # 给实例添加属性
 p.age = 18
 # 给类添加属性
 Person.age = 20

2.给实例添加方法
--------------------------------------

::

 class Person:
  def __init__(self,name):
    self.name=name

 def run(self):
  print("在跑")
 
 p = Person("张三")
 
 import types0

 # 给实例添加方法
 p.run = types.MethodTypes(run,p) # p相当于self = p
 p.run()

3.给类添加类方法和静态方法
----------------------------------------------

::

 class Person:
  def __init__(self,name):
    self.name = name

 @staticmethod
 def addstaticMethod():
  print("动态添加静态方法")

 @classmethod
 def addclazzMethod(cls):
  print("动态添加类方法")

 Person.addstaticMethod = addstaticMethod
 Person.addstaticMethod()

 Person.addclazzMethod = addclazzMethod
 Person.addclazzMethod()

4.禁止添加额外属性
--------------------------------------------

定义一个特殊的__slots__变量，来限制该class实例能添加的属性

::

 class Person:

  __slots__ = ("name","age")

 p = Person()
 p.name = "张三"
 p.age = 20
 p.score = 100

>>> AttributeError                            Traceback (most recent call last)
>>> <ipython-input-23-91c47bf50c73> in <module>
>>> ----> 1 p.score = 100
>>> AttributeError: 'Person' object has no attribute 'score'

**使用__slots__定义的属性仅对当前类的实例起作用，对继承的子类是不起作用的**







