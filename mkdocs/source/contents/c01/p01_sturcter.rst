===============================
Python 基础
===============================

基础语法
============================

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
    

 基本数据类型
=========================

多变量赋值

::

 a = b = c = 1

从后向前赋值，三个变量指向一个内存地址
注意赋值语句：

::

 a,b = b,a+b

相当于

::

 t = (b,a+b) # t是tuple
 45  a = t[0]
 b = t[1]

Bool

 - 非空数据结构（列表，字典，元组，字符串，集合）记为 True；
 - 0 和 None 记为 False, 而其他值记为 True；
 - 关键字 True 是 True, False 是 False。

::

 a = 1
 b = '1'
 bool(a == b)  #判断表达式真假
 >>> False

标准数据类型

- Number、String、List、Tuple、Set、Dict
- 不可变数据类型(3个)：Number、String、Tuple
- 可变数据类型(3个):List、Dict、Set


type()和isinstance()来查询变量所指的对象类型
 isinstance（）和type()的区别：
	
::
	
 class A:
    pass
 class B:
	pass

 isinstance(A(),A)
 type(A()) == A
 isinstance(B(),A)
 type(B())== A

