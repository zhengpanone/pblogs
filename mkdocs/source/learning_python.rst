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

1.5 yield使用
-------------

带有yield的函数在python中称之为generator(生成器)

如何生成斐波拉契数列

::

 def fab(max):
     n,a,b = 0, 0, 1
     while n < max:
         print(b)
         a, b = b, a+b
         n = n + 1

执行fab(5)

::

 >>> fab(5)
 1
 1
 2
 3
 5

直接在 fab 函数中用 print 打印数字会导致该函数可复用性较差，因为 fab 函数返回 None，其他函数无法获得该函数生成的数列。

要提高 fab 函数的可复用性，最好不要直接打印出数列，而是返回一个 List。以下是 fab函数改写后的第二个版本：

::

 def fab(max):
     n, a, b = 0, 0, 1
     L = []
     while n < max:
         L.append(b)
         a, b = b, a + b
         n = n + 1
     return L

::

 >>> for n in fab(5):
         print(n)

     ...
     ...
     1
     1
     2
     3
     5

函数在运行中占用的内存会随着参数 max 的增大而增大，如果要控制内存占用，最好不要用 List


利用 iterable 我们可以把 fab 函数改写为一个支持 iterable 的 class，以下是第三个版本的 Fab：

::

 class Fab(object):
     def __init__(self, max):
         self.max = max
         self.n, self.a, self.b = 0, 0, 1
     def __iter__(self):
         return self

     def next(self):
         if self.n < self.max:
             r = self.b
             self.a, self.b = self.b, self.a + self.b
             self.n = self.n + 1
             return r
         raise StopIteration()

Fab类通过next()不断返回数列的下一个数,内存占用始终为常数：

::

 >>> for n in Fab(5):
 ...     print(n)
 ...
 1
 1
 2
 3
 5

使用class改写的没有第一版简洁,想要简洁且获得iterable的效果,使用yield:

::

 def fab(max):
     n, a, b = 0, 0, 1
     while n < max:
         yield b
         # print(b)
         a, b = b, a + b
         n = n + 1

::

 >>> for n in fab(5):
 ...     print(n)
 ...
 1
 1
 2
 3
 5

yield 的作用是把函数变成一个generator,带有yield的函数不再是一个普通函数,Python解释器会将其视为一个generator,调用fab(5) 不会执行fab函数,而是返回一个iterable对象！在for循环执行时,每次循环都会执行fab函数内部代码,执行到yield b时,fab函数就返回一个迭代值,下次迭代时,代码从yield b 的下一条语句继续执行,而函数的本地变量看起来和上次中断执行前时完全一样的,于是函数继续执行,直到再次遇到yield.

也可以手动调用 fab(5) 的 next() 方法（因为 fab(5) 是一个 generator 对象，该对象具有 next() 方法），这样我们就可以更清楚地看到 fab 的执行流程：

::

 >>> f = fab(5)
 >>> f.next()
 1
 >>> f.next()
 1
 >>> f.next()
 2
 >>> f.next()
 3
 >>> f.next()
 5
 >>> f.next()
 Traceback(most recent call last):
 File "<stdin>", line 1, in <module>
 StopIteration

当函数执行结束时，generator 自动抛出 StopIteration 异常，表示迭代完成。在 for 循环里，无需处理 StopIteration 异常，循环会正常结束。

我们可以得出以下结论：


    
1.6 包和模块
=============================

1. 一个模块(module)就是一个py文件,模块名字就是该文件名字

2. 一个包(package)就是一个文件夹,(python2规定文件夹中必须包含一个__init__.py,python3没有要求),包名就是文件夹名

3. 按import进来的对象不同分为4种场景：

::
 
 import <package>  # 导入一个包
 import <module> # 导入一个模块
 from <package> import <module or subpackage or object> # 从一个包中导入模块/子包/对象
 from <module> import <object> # 从模块中导入对象

4. 解释器会按照sys.path 列表的顺序来查找被引入的包或模块名字

 >>> import sys
 >>> import pprint
 >>> pprint.pprint(sys.path)
 ['',
  'C:\\Python\\Python36\\python36.zip',
  'C:\\Python\\Python36\\DLLs',
 ]
 
优先加载当前目录下的模块,如果项目中使用了与内建模块中同名的包或者模块名,就会遇到没有XX属性之类的报错提示

5. 使用sys.path,使得其他路径的文件加入到Path中,使解释器可以发现

::
 test.py
 import sys,os
 # 当前目录没hi模块,报错找不到模块
 import hi
 Traceback (most recent call last):
 ImportError: No module named hi

 # hi模块所在的位置:/data/hi.py
 # 将hi 所在的模块加入sys.path
 sys.path.append('/data')

 # 可以正常工作
 import hi

6. 另外一种加载模块的方法: 如果模块不在sys.path下面,可以使用imp 模块中的imp.load_source

::
 import imp
 imp.load_source('hi', 'C://data/hi.py')
 import hi

 # 可以自己指定模块的名字,相当于import hi as h2
 imp.load_source('h2', 'C://data/hi.py')
 import h2

7. import module时, 模块中所有代码将被执行(类对象,函数对象将被创建,不会被调用),import package 时, __init__.py 文件中的代码也将被执行

8. 模块的__file__ 属性
   导入模块时,可以通过模块的__file__属性查看模块所在的磁盘路径位置

 >>> import requests
 >>> requests.__file__
 'D:\\Programs\\Anaconda3\\envs\\py_test\\lib\\site-packages\\requests\\__init__.py'

9. 永远不要使用 from <module> import \*,有不可预知的风险

1.7 装饰器

1. 用类写装饰器
   实现缓存装饰器

::
 def cache(func):
    data = {}
    def wrapper(*args, **kwargs):
        key = f'{func.__name__}-{str(args)}-{str(kwargs)}'
        if key in data:
            result = data.get(key)
            print('cached')
        else:
            result = func(*args, **kwargs)
            data[key] = result
            print('calculated')
        return result
    return wrapper

查看缓存效果

::
 @cache
 def rectangle_area(length, width):
    return length*width

 rectangle_area(2, 3)
 # calculated
 # 6
 rectangle_area(2, 3)
 # cached
 # 6

装饰器的@cache 是语法糖,相当于func = cache(func), 如果这里的cache不是一个函数,而是一个类？
定义一个类 class Cache, 那么调用func = Cache(func) 会得到一个对象, 这时返回的func 其实是Cache的对象. 定义__call__方法可以将类的实例变成可调用对象, 可以像调用函数一样调用对象. 然后在__call__ 方法里调用原本的func函数就能实现装饰器. 所以Cache类也能当作装饰器使用, 并且能以@Cache 的形式使用.

把cache函数改写为Cache类:

::
 class Cache:
    def __init__(self, func):
        self.func = func
        self.data = {}

    def __call__(self, *args, **kwargs):
        func = self.func
        data = self.data
        key = f'{func.__name__}-{str(args)}-{str(kwargs)}'
        if key in data:
            result = data.get(key)
            print('cached')
        else:
            result = func(*args, **kwargs)
            data[key] = result
            print('calculated')
        return result

查看缓存效果

::
 @Cache
 def rectangle_area(length, width):
    return length * width

 rectangle_area(2, 3)
 # calculated
 # 6
 rectangle_area(2, 3)
 # calculated
 # 6

2. 装饰类的方法
   装饰器不止能装饰函数, 也常用来装饰类的方法, 

函数写的装饰器如何装饰类的方法

::
 class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

