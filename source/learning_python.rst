第一章 python基础
======================

1.1 基础语法
---------------------

**设置编码**
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

1.3文件处理
------------------

读文件

::

 f = open('/opt/work/user/zhengpanone/test.txt','r')

标识符'r',标识只读;
如果文件不存在,open()函数会抛出异常IOError的错误

::
 >>> f=open('/Users/michael/notfound.txt', 'r')
 Traceback (most recent call last):
   File "<stdin>", line 1, in <module>
 FileNotFoundError: [Errno 2] No such file or directory: '/Users/michael/notfound.txt'

如果文件打开成功,调用read()方法可以一次读取文件全部内容,python把文件内容读到内存,用一个str对象表示：

::
 >>f.read()
 'hello python!'

最后一步调用close()方法关闭文件。文件使用完毕必须关闭,因为文件对象会占用系统资源,且操作系统同时能打开的文件数量也是有限的：

::
 >>f.close()

由于文件读写都有可能产生IOError,一旦文件出错,后面的f.close就不会调用。所以,为了保证无论是否出错都能正确的关闭文件,使用try... finally 实现：

::
 try:
    f = open('path/file','r')
    print(f.read())
 finally:
    if f:
        f.close()

1.4 推导式
----------------

推导式是将所有的值一次性加载到内存



1.5 生成器
----------------

生成器 是将推导式的[] 改成(), 不会将所有的一次性加载到内存中，延迟计算，一次返回一个结果，不会一次生成所有的结果, 处理大数据非常有用

::
 def fun():
    for i in range(1,50):
        yield i
 for i in fun():
    print(i)

生成器函数：一个函数中包含yield关键字, 这个函数是一个生成器函数
调用生成器函数,不会立马执行该函数里的代码,而返回一个生成器

::
 def func():
    print('a')
    yield
    print('b')
    yield
    print('c')
    yield
    print('d')

 generator = func()
 print(generator)
 print(type(generator))
 for i in generator:
    pass


::
 sum(x for x in range(1000000000)) # 占用内存少
 sum([x for x in range(1000000000)]) # 占用内存大


原理: sum 函数是python3内置函数,该函数使用迭代器协议访问对象,而生成器实现了迭代器协议,所以可以直接计算一系列值的和,不用先构造一个列表


