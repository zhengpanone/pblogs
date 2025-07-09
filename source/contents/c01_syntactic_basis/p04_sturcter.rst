===============================
Python 基础
===============================

保留字

>>> import keyword
>>> keyword.kwlist

可调用对象
==========

可以作为函数直接调用的对象 称为可调用对象

用途： 

 1、简化对象下方法的调用 （a.func()=> a() => 对象下只有一个方法== > 对象下某个方法使用很多的时候 ）

 2、模糊了对象和函数的区别  （统一调用接口）

.. literalinclude:: ./code/p04/01_callback.py
    :encoding: utf-8
    :language: python
    :emphasize-lines: 11
    :linenos:

and 和or 
===========

and 和or的取值顺序：一个or表达式中所有值都为真，Python会选择第一个值，而and表达式则会选择第二个。

>>> (2 or 3) * （5 and 7）
>>> 14 # 2*7
    

基本数据类型
===============

python中常见的内置类型
>>>>>>>>>>>>>>>>>>>>>>>>>>>>

- None(全局只有一个)

- 数值

   - int 

   - float

   - complex

   - bool

- 迭代类型

- 序列类型

   - list 

   - bytes、bytearray、memoryview(二进制序列)

   - range

   - tuple 

   - str 

   - array

- 映射类型(dict)

- 集合

   - set 

   - frozenset

- 上下文管理类型(with)

- 其他

   - 模块类型

   - class和类型

   - 函数类型

   - 方法类型

   - 代码类型

   - object对象

   - type类型

   - ellipsis类型

   - notimplemented(类对象)类型




Python中的字符串（String）、元组（Tuple）、列表（List）都属于序列(Sequence)类型簇。可以将字符串看作由字符组成的序列类型，元祖是任意对象组成的不可修改序列类型，列表是任意对象组成的可修改序列。

数值型
>>>>>>>>>>>>>>>>>

- 前缀 **0x** ，创建一个十六进制的整数

.. code-block:: python
   :linenos:

   0xa5 # 等于十进制的165

- 使用 **e** 创建科学计数法表示浮点数

.. code-block:: python
   :linenos:

   1.05e3   # 1050.0

多变量赋值
>>>>>>>>>>>>>>>>

>>> a = b = c = 1

从后向前赋值，三个变量指向一个内存地址
注意赋值语句：



>>> a,b = b,a+b

相当于

.. code-block:: shell
   :linenos: 

   t = (b,a+b) # t是tuple
   a = t[0]
   b = t[1]

Bool
>>>>>>>>>>

 - 非空数据结构（列表，字典，元组，字符串，集合）记为 True；
 - 0 和 None 记为 False, 而其他值记为 True；
 - 关键字 True 是 True, False 是 False。



>>> a = 1
>>> b = '1'
>>> bool(a == b)  #判断表达式真假
>>> False

标准数据类型
>>>>>>>>>>>>>>

- Number、String、List、Tuple、Set、Dict
- 不可变数据类型(3个)：Number、String、Tuple
- 可变数据类型(3个):List、Dict、Set

元组有不可更改 (immutable) 的性质，因此不能直接给元组的元素赋值,但是只要元组中的元素可更改 (mutable)，那么我们可以直接更改其元素，注意这跟赋值其元素不同。

>>> t = ('OK', [1, 2], True)
>>> t[1].append(3)
>>> t 
>>> ('OK', [1, 2, 3], True)

元组大小和内容都不可更改，因此只有 count 和 index 两种内置方法。

>>> t = (1, 10.31, 'python')
>>> print(t.count("python"))
>>> print(t.index(10.31))

- count('python') 是记录在元组 t 中该元素出现几次，显然是 1 次
- index(10.31) 是找到该元素在元组 t 的索引，显然是 1

>>> %timeit [1, 2, 3, 4, 5]
>>> %timeit (1, 2, 3, 4, 5)

>>> lst = [i for i in range(65535)]
>>> tup = tuple(i for i in range(65535))
>>> %timeit for each in lst: pass
>>> %timeit for each in tup: pass

>>> from sys import getsizeof
>>> print( getsizeof(lst) )
>>> print( getsizeof(tup) )

.. code-block:: shell
   :linenos: 

   a = (1,2,3,4)
   b = (5,6,7,8)
   a = a + b

type()和isinstance()来查询变量所指的对象类型

 isinstance（）和type()的区别：


.. code-block:: shell
   :linenos: 

   class A:
      pass
   class B:
      pass

   isinstance(A(),A)
   type(A()) == A
   isinstance(B(),A)
   type(B())== A

操作符
===========================================

.. note::

 - \+、 \-、 \*、 /
 - % 取余、** 幂操作、// 整除
 - not 取反;只用于Boolen类型
 - ~A 按二进制取反；按照补码规则，结果数字是-（A+1）
 - A & B 并操作；只有两个比特位都为1时结果中的对应比特位才设1，否则设零
 - A | B 或操作；只要两个比特位有一个为1，结果中的对应位则设1，否则设零
 - A ^ B 异或操作；如果两个比特位相同，则结果中的对应位设零，否则设1
 - A >> B 按比特位右移
 - A << B 按比特位左移

format
===========================

.. code-block:: python
   :linenos:

   print("test{:03d}.txt".format(2))

   >>> test002.txt


python中一切皆对象
===========================

函数和类也是对象，属于python的一等公民

1、赋值给一个变量

2、可以添加到集合对象中

3、可以作为参数传递给函数

4、可以当做函数的返回值


type、object、class 的关系
========================================

- object是最顶层基类

- type也是一个类,object是type的实例，而type又继承object

- type是自身的实例

- 查看类的父类,使用魔法方法**类.__bases__**