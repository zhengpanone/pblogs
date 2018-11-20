===============================
1.1 基础语法
===============================

1.1 文件编码
---------------------------

**设置编码**

::

 !/usr/bin/python
 _*_ coding:UTF-8 _*_

保留字

::

 import keyword
 keyword.kwlist


1.2  可调用对象
-------------------------------------

可以作为函数直接调用的对象 称为可调用对象
用途：1、简化对象下方法的调用 （a.func()=> a() => 对象下只有一个方法== > 对象下某个方法使用很多的时候 ）
          2、模糊了对象和函数的区别  （统一调用接口）


::

 class A():
    def __call__(self):
        return object()

 class B():
    def run(self):
        return object()

 def func():
    return object()

 def main(callable):  # 可调用对象
    callable()
    # 在main 中调用传入的参数，得到一个对象object
    # b.run()
    # func()
    # ...

    pass

 main(A())
 main(B())
 main(func)


1.3 and 和or 
------------------------------

and 和or的取值顺序：一个or表达式中所有值都为真，Python会选择第一个值，而and表达式则会选择第二个。

::

 >>> (2 or 3) * （5 and 7）
 >>> 14 # 2*7
    

