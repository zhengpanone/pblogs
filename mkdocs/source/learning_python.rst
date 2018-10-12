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


使用with 读写文件

 ::
    
    with open('path/file','r') as f, open('path/file2','w') ad f2:
        for l in a:
            f2.write(l.readline())


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

1.6 yield使用
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


    
1.7 包和模块
-------------------------

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

1.8 装饰器
----------------------------------

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

1.8 上下文与出入栈

 1、上下文管理器常用于一些资源的操作,需要获取资源与释放资源的相关操作 


::
 
 class Database(object):
    
    def __init__(self):
        self.connected = False

    def connect(self):
        self.connected = True

    def close(self):
        self.connected = False

    def query(self):
        if self.connected:
            return 'query data'
        else:
            raise ValueError('DB not connected')


 def handle_query():
    db = DataBase()
    db.connect()
    print('handle ---', db.query())
    db.colse()

 def main():
    handle_query()

 if __name__ == '__main__':
    main()

2、使用装饰器处理

::
 
 class Database(object):
    ...
 def dbconn(fn):
    def wrapper(*args, **kwargs):
        db = Database()
        db.connect()
        ret = fn(db, *args, **kwargs)
        db.close()
        return ret
    return wraaper

 @dbconn
 def handle_query(db=None):
    print('handle ---', db.query())

 def main():
    ...

编写一个dbconn的装饰器，然后针对handle_query 进行装饰

3、优雅使用With 语句语法，构建资源创建与释放的语法糖

::
 
 class Database(object):
    ...
    def __enter__(self):
        self.connect()
        return self
    def __exit__(self,exc_type,exc_val,exc_tb):
        self.colse()

修改handle_query 函数

::
 
 def handle_query():
    with Database() as db:
        print('handle ---', db.query())


实现了迭代协议的函数/对象即为迭代器。实现了上下文协议的函数/对象即为上下文管理器。迭代器协议是实现了__iter__方法。上下文管理协议则是__enter__和__exit__。

::

 class Contextor:
    def __enter__(self):
        pass
    def __exit__(self,exc_type,exc_val,exc_tb):
        pass

 contextor = Contextor()

 with contextor as var:
    with_body

Contextor 实现了__enter__和__exit__这两个上下文管理器协议，当Contextor调用/实例化的时候，则创建了上下文管理器contextor。类似于实现迭代器协议类调用生成迭代器一样。
配合with语句使用的时候，上下文管理器会自动调用__enter__方法，然后进入运行时上下文环境，如果有as 从句，返回自身或另一个与运行时上下文相关的对象，值赋值给var。当with_body执行完毕退出with语句块或者with_body代码块出现异常，则会自动执行__exit__方法，并且会把对于的异常参数传递进来。如果__exit__函数返回True。则with语句代码块不会显示的抛出异常，终止程序，如果返回None或者False，异常会被主动raise，并终止程序。

对with语句的执行原理总结Python上下文管理器与with语句:

::

 执行 contextor 以获取上下文管理器
 加载上下文管理器的 exit() 方法以备稍后调用
 调用上下文管理器的 enter() 方法
 如果有 as var 从句，则将 enter() 方法的返回值赋给 var
 执行子代码块 with_body
 调用上下文管理器的 exit() 方法，如果 with_body 的退出是由异常引发的，那么该异常的 type、value 和 traceback 会作为参数传给 exit()，否则传三个 None
 如果 with_body 的退出由异常引发，并且 exit() 的返回值等于 False，那么这个异常将被重新引发一次；如果 exit() 的返回值等于 True，那么这个异常就被无视掉，继续执行后面的代码

了解了with语句和上下文管理协议，或许对上下文有了一个更清晰的认识。即代码或函数执行的时候，调用函数时候有一个环境，在不同的环境调用，有时候效果就不一样，这些不同的环境就是上下文。例如数据库连接之后创建了一个数据库交互的上下文，进入这个上下文，就能使用连接进行查询，执行完毕关闭连接退出交互环境。创建连接和释放连接都需要有一个共同的调用环境。不同的上下文，通常见于异步的代码中。


**上下文管理器工具**
通过实现上下文协议定义创建上下文管理器很方便，Python为了更优雅，还专门提供了一个模块用于实现更函数式的上下文管理器用法。

::
 
 import contextlib
 @contextlib.contextmanager
 def databae():
    db = Database()
    try:
        if not db.connected:
            db.connect()
        yield db
    except Exception as e:
        db.close()
 def handle_query():
    with database() as db:
        print('handle --',db.query())

使用contextlib 定义一个上下文管理器函数，通过with语句，database调用生成一个上下文管理器，然后调用函数隐式的__enter__方法，并将结果通yield返回。最后退出上下文环境的时候，在excepit代码块中执行了__exit__方法。当然我们可以手动模拟上述代码的执行的细节。

::
 
 In [1]: context = database()    # 创建上下文管理器
  
 In [2]: context
  
  
 In [3]: db = context.__enter__() # 进入with语句
  
 In [4]: db                             # as语句，返回 Database实例
 Out[4]: 
  
 In [5]: db.query()       
 Out[5]: 'query data'
  
 In [6]: db.connected
 Out[6]: True
  
 In [7]: db.__exit__(None, None, None)    # 退出with语句
  
 In [8]: db
 Out[8]: 
  
 In [9]: db.connected
 Out[9]: False


**上下文管理器的用法**
既然了解了上下文协议和管理器，当然是运用到实践啦。通常需要切换上下文环境，往往是在多线程/进程这种编程模型。当然，单线程异步或者协程的当时，也容易出现函数的上下文环境经常变动。

异步式的代码经常在定义和运行时存在不同的上下文环境。此时就需要针对异步代码做上下文包裹的hack。看下面一个例子：

::

 import tornado.ioloop

 ioloop = tornado.ioloop.IOLoop.instance()

 def callback():
    print('run callback')
    raise ValueError('except in callback')

 def async_task():
    print('run async task')
    ioloop.add_callback(callback=callback)

 def main():
    
    try:
        async_task()
    except Exception as e:
        print('exception {}'.format(e))
    print ('end')

 main()
 ioloop.start()
 
 # 运行上述代码
 >>
    run async task
    Error.root:Exception in callback
    Traceback(most recent call last):
        ...
        raise ValueError('except in callback')
    ValueError:except in callback

主函数中main中，定义了异步任务函数async_task的调用。async_task中异常，在except中很容易catch，可是callback中出现的异常，则无法捕捉。原因就是定义的时候上下文为当前的线程执行环境，而使用了tornado的ioloop.add_callback方法，注册了一个异步的调用。当callback异步执行的时候，他的上下文已经和async_task的上下文不一样了。因此在main的上下文，无法catch异步中callback的异常。

下面使用上下文管理器包装如下：

::

 class Contextor(object):
    def __enter__(self):
        pass
    def __exit__(self,exc_type,exc_val,exc_tb):
        if all([exc_type,exc_val,exc_tb]):
            print('handler except')
            print('exception {}'.format(exc_val))
        return True

 def main():
    with tornado.stack_context.StackContext(Contextor):
        async_task()

 # 运行main之后结果如下：
 run async task
 handler except
 run callback
 handler except
 exception except in callback


可见，callback的函数的异常，在上下文管理器Contextor中被处理了，也就是说callback调用的时候，把之前main的上下文保存并传递给了callback。当然，上述的代码也可以改写如下：

::

 @contextlib.contextmanager
 def contextor():
    try:
        yield
    except Exception as e:
        print('handle except')
        print('exception {}'.format(e))
    finally:
        print('release')

 def main():
    with tornado.stack_context.StackContext(contextor)
        async_task()


效果类似。当然，也许有人会对StackContext这个tornado的模块感到迷惑。其实他恰恰应用上下文管理器的魔法的典范。查看StackContext的源码，实现非常精秒，非常佩服tornado作者的编码设计能力。至于StackContext究竟如何神秘，已经超出了本篇的范围，将会在介绍`tonrado异步上下文管理器`__中介绍

.. __: https:Tornado_Source.rst



