第一章 python基础
======================

1.1 基础语法
---------------------

设置编码
::

 !/usr/bin/python
 _*_ coding:UTF-8 _*_
 

保留字
::

 import keyword
 keyword.kwlist


1.2 基本数据类型
---------------------

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
 a = t[0]
 b = t[1]
 
Bool
 - 非空数据结构（列表，字典，元组，字符串，集合）记为 True；
 - 0 和 None 记为 False, 而其他值记为 True；
 - 关键字 True 是 True, False 是 False。
