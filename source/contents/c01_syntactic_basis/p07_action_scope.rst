============================
7. 作用域
============================

globals、locals
============================

查看全局变量使用**globals()**,查看局部变量使用**locals()**,查看内嵌使用**dir(__builtin__)**


LEGB规则
=====================================

python通过LEGB的顺序来查找一个符合对应的对象

::

 locals -> enclosing funcion -> globals -> builtins

- locals 当前所在命名空间（函数、模块），函数的参数也属于命名空间内的变量
- enclosing 外包嵌套的命名空间（闭包中常见）

::

 def fun1():
   a = 10
   def fun2():
      # a 位于外部嵌套函数的命名空间
      print(a)
      
- globals 全局变量，函数定义所在模块的命名空间

::

 a = 1
 def fun():
   # 需要通过global指令来声明全局变量
   global a

   # 修改全局变量，而不是创建一个新的local变量
   a = 2

     






