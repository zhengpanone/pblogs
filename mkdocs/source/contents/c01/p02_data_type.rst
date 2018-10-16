=========================
1.2 基本数据类型
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
 -0 和 None 记为 False, 而其他值记为 True；
 - 关键字 True 是 True, False 是 False。

::

 a = 1
 b = '1'
 bool(a == b)  #判断表达式真假
 >>> False

标准数据类型

    Number、String、List、Tuple、Set、Dict
    不可变数据类型(3个)：Number、String、Tuple
    可变数据类型(3个):List、Dict、Set
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

