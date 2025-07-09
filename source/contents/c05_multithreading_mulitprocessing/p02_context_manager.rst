===========================
`上下文与出入栈`__
===========================

.. __ : http://python.jobbole.com/87317/


**上下文管理协议**

那么在Python中怎么实现一个上下文管理器呢？这里，又要提到两个”魔术方法”，__enter__和__exit__，下面就是关于这两个方法的具体介绍。


 __enter__(self) Defines what the context manager should do at the beginning of the block created by the with statement. Note that the return value of __enter__ is bound to the target of the with statement, or the name after the as.
 __exit__(self, exception_type, exception_value, traceback) Defines what the context manager should do after its block has been executed (or terminates). It can be used to handle exceptions, perform cleanup, or do something always done immediately after the action in the block. If the block executes successfully, exception_type, exception_value, and traceback will be None. Otherwise, you can choose to handle the exception or let the user handle it; if you want to handle it, make sure __exit__ returns True after all is said and done. If you don’t want the exception to be handled by the context manager, just let it happen.

也就是说，当我们需要创建一个上下文管理器类型的时候，就需要实现__enter__和__exit__方法，这对方法就称为上下文管理协议（Context Manager Protocol），定义了一种运行时上下文环境。


**with语句**

在Python中，可以通过with语句来方便的使用上下文管理器，with语句可以在代码块运行前进入一个运行时上下文（执行__enter__方法），并在代码块结束后退出该上下文（执行__exit__方法）。

with语句的语法如下：

.. code-block:: shell
    
  with context_expr [as var]:
      with_suite

context_expr是支持上下文管理协议的对象，也就是上下文管理器对象，负责维护上下文环境
as var是一个可选部分，通过变量方式保存上下文管理器对象
with_suite就是需要放在上下文环境中执行的语句块

在Python的内置类型中，很多类型都是支持上下文管理协议的，例如file，thread.LockType，threading.Lock等等。这里我们就以file类型为例，看看with语句的使用。

**with语句简化文件操作**

当需要写一个文件的时候，一般都会通过下面的方式。代码中使用了try-finally语句块，即使出现异常，也能保证关闭文件句柄。

.. code-block:: python

  logger = open("log.txt", "w")
  try:
    logger.write('Hello ')
    logger.write('World')
  finally:
    logger.close()
    
    print (logger.closed)

其实，Python的内置file类型是支持上下文管理协议的，可以直接通过内建函数dir()来查看file支持的方法和属性：


>>> print dir(file)

>>> ['__class__', '__delattr__', '__doc__', '__enter__', '__exit__', '__format__',

>>> '__getattribute__', '__hash__', '__init__', '__iter__', '__new__', '__reduce__',

>>> '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',

>>> 'close', 'closed', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 

>>> 'mode', 'name', 'newlines', 'next', 'read', 'readinto', 'readline', 'readlines',

>>> 'seek', 'softspace', 'tell', 'truncate', 'write', 'writelines', 'xreadlines']


所以，可以通过with语句来简化上面的代码，代码的效果是一样的，但是使用with语句的代码更加的简洁：

.. code-block:: python

  with open("log.txt", "w") as logger:
      logger.write('Hello ')
          logger.write('World')
            
          print logger.closed


**自定义上下文管理器**

对于自定义的类型，可以通过实现__enter__和__exit__方法来实现上下文管理器。

看下面的代码，代码中定义了一个MyTimer类型，这个上下文管理器可以实现代码块的计时功能：

.. code-block:: shell
    

    import time
    
    class MyTimer(object):
      def __init__(self, verbose = False):
        self.verbose = verbose
              
      def __enter__(self):
        self.start = time.time()
        return self
                              
      def __exit__(self, *unused):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000
        if self.verbose:
            print ("elapsed time: %f ms" %self.msecs)



下面结合with语句使用这个上下文管理器：

.. code-block:: shell
    
    def fib(n):
      if n in [1, 2]:
          return 1
      else:
          return fib(n-1) + fib(n-2)
                            
    with MyTimer(True):
        print (fib(30))


1、上下文管理器常用于一些资源的操作,需要获取资源与释放资源的相关操作 

.. code-block:: shell
    
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

.. code-block:: shell
 
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

.. code-block:: python
 
  class Database(object):
      ...
      def __enter__(self):
          self.connect()
          return self
      def __exit__(self,exc_type,exc_val,exc_tb):
          self.close()

修改handle_query 函数

.. code-block:: python
 
  def handle_query():
      with Database() as db:
          print('handle ---', db.query())


实现了迭代协议的函数/对象即为迭代器。实现了上下文协议的函数/对象即为上下文管理器。迭代器协议是实现了__iter__方法。上下文管理协议则是__enter__和__exit__。

.. code-block:: python

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

.. code-block:: text

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

.. code-block:: python
 
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

.. code-block:: shell
 
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

.. code-block:: python

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

>>> run async task
>>> Error.root:Exception in callback
>>> Traceback(most recent call last):
>>>     ...
>>>       raise ValueError('except in callback')
>>> ValueError:except in callback

主函数中main中，定义了异步任务函数async_task的调用。async_task中异常，在except中很容易catch，可是callback中出现的异常，则无法捕捉。原因就是定义的时候上下文为当前的线程执行环境，而使用了tornado的ioloop.add_callback方法，注册了一个异步的调用。当callback异步执行的时候，他的上下文已经和async_task的上下文不一样了。因此在main的上下文，无法catch异步中callback的异常。

下面使用上下文管理器包装如下：

.. code-block:: python

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

运行main之后结果如下：

>>> run async task

>>> handler except

>>> run callback

>>> handler except

>>> exception except in callback


可见，callback的函数的异常，在上下文管理器Contextor中被处理了，也就是说callback调用的时候，把之前main的上下文保存并传递给了callback。当然，上述的代码也可以改写如下：

.. code-block:: python

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


效果类似。当然，也许有人会对StackContext这个tornado的模块感到迷惑。其实他恰恰应用上下文管理器的魔法的典范。查看StackContext的源码，实现非常精秒，非常佩服tornado作者的编码设计能力。至于StackContext究竟如何神秘，已经超出了本篇的范围，将会在介绍 `tonrado异步上下文管理器`__  中介绍

.. __: https://github.com/zhengpanone/blogs/blob/master/mkdocs/source/Tornado_Source.rst 

