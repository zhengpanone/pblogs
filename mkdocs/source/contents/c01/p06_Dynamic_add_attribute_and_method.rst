============================
1.6 动态添加属性和方法
============================

1. 动态给实例和类添加属性
===========================================

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
==============================================

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
===================================================

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

 Persion.addstaticMethod = addstaticMethod
 Persion.addstaticMethod()

 Persion.addclazzMethod = addclazzMethod
 Persion.addclazzMethod()





