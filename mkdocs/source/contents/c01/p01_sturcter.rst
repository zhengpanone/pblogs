===============================
1.1 基础语法
===============================

**设置编码**

::

 !/usr/bin/python
 _*_ coding:UTF-8 _*_

保留字


::

 import keyword
 keyword.kwlist


 1.使用.join()进行字符串拼接
------------------------------

::

 strings = ['how','to','use','.join']
 ' '.join(strings)
 >>> 'how to use .join'

 type(' '.join(strings))
 >>> str

 'b'.join(['a'])
 >>> 'a'


.join()方法只是在想要加入的可迭代字符串之间插入“连接符”，而不是在可迭代的每个字符串的末尾添加连接符。 这意味着如果传递的是一个大小为1的迭代器，您将看不到连接符
