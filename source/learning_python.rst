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
