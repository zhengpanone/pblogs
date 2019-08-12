===============================
4. Python 基础
===============================

保留字

::

 import keyword
 keyword.kwlist

可调用对象
-------------------------------------

可以作为函数直接调用的对象 称为可调用对象

用途： 

 1、简化对象下方法的调用 （a.func()=> a() => 对象下只有一个方法== > 对象下某个方法使用很多的时候 ）
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

and 和or 
------------------------------

and 和or的取值顺序：一个or表达式中所有值都为真，Python会选择第一个值，而and表达式则会选择第二个。

::

 >>> (2 or 3) * （5 and 7）
 >>> 14 # 2*7
    

python中常见的内置类型
==========================

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


基本数据类型
==========================

Python中的字符串（String）、元组（Tuple）、列表（List）都属于序列(Sequence)类型簇。可以将字符串看作由字符组成的序列类型，元祖是任意对象组成的不可修改序列类型，列表是任意对象组成的可修改序列。

多变量赋值
-----------------------

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
----------------------------

 - 非空数据结构（列表，字典，元组，字符串，集合）记为 True；
 - 0 和 None 记为 False, 而其他值记为 True；
 - 关键字 True 是 True, False 是 False。

::

 a = 1
 b = '1'
 bool(a == b)  #判断表达式真假
 >>> False

标准数据类型
----------------------------

- Number、String、List、Tuple、Set、Dict
- 不可变数据类型(3个)：Number、String、Tuple
- 可变数据类型(3个):List、Dict、Set

不能修改元组,可以对元组变量重新赋值

::

 a = (1,2,3,4)
 b = (5,6,7,8)
 a = a + b

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

操作符
===========================================

.. note::

 - +、-、*、/
 + % 取余、** 幂操作、// 整除
 - not 取反;只用于Boolen类型
 - ~A 按二进制取反；按照补码规则，结果数字是-（A+1）
 - A & B 并操作；只有两个比特位都为1时结果中的对应比特位才设1，否则设零
 - A | B 或操作；只要两个比特位有一个为1，结果中的对应位则设1，否则设零
 - A ^ B 异或操作；如果两个比特位相同，则结果中的对应位设零，否则设1
 - A >> B 按比特位右移
 - A << B 按比特位左移