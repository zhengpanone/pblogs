==========================
生成器(Generators)
==========================

⽣成器也是⼀种迭代器，但是你只能对其迭代⼀次。这是因为它们并没有把所有的值存在内存中，⽽是在运⾏时⽣成值。不会将所有的一次性加载到内存中，延迟计算，一次返回一个结果，不会一次生成所有的结果, 处理大数据非常有用

- 可迭代对象(Iterable)
- 迭代器(Iterator)
- 迭代(Iteration)

可迭代对象(Iterable)
====================================

Python任意对象,只要它定义了可以返回一个迭代器的__iter__方法,或者定义了可以支持下标索引的__getitem__方法,那么1它就是一个可迭代对象。即可迭代对象就是能提供迭代器的任意对象

迭代器(Iterator)
====================================

任意对象定义了__next__方法,他就是一个迭代器

实现一个递减迭代器
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

编写一个迭代器，通过循环语句，实现对某个正整数的依次递减1，直到0.

.. literalinclude:: ./code/p02_generator/descend.py
    :encoding: utf-8
    :language: python
    


迭代(Iteration)
======================================

使⽤⼀个循环来遍历某个东西时，这个过程本⾝就叫迭代


1.将推导式的[] 改成()
========================================

.. code-block:: python

  L = [x*2 for x in range(10)]
  G = (x*2 for x in range(10)) # 生成器

  next(G)
 
.. code-block:: python

  def fun():
      for i in range(1,50):
          yield i

  for i in fun():
      print(i)

  
1. yield 创建生成器
========================================

生成器函数：一个函数中包含yield关键字, 这个函数是一个生成器函数调用生成器函数,不会立马执行该函数里的代码,而返回一个生成器


.. code-block:: python

  def createNum():
    print("--------start---------")
    a,b = 0,1
    for i in range(10):
      print("-------1-------")
      yield b 
      print('-------2--------')
      a,b = b,a+b
      print('-------3---------')
    print('--------stop------------')

  a = createNum()
  for i in a:
    print(i)

>>> import createNum
>>> n = next(createNum)  # 返回值为b的值

.. code-block:: python

  sum(x for x in range(1000000000)) # 占用内存少
  sum([x for x in range(1000000000)]) # 占用内存大

原理: sum 函数是python3内置函数,该函数使用迭代器协议访问对象,而生成器实现了迭代器协议,所以可以直接计算一系列值的和,不用先构造一个列表


3.send
==========================

.. code-block:: python

  def test():
    i = 0
    while i < 5:
        temp = yield i
        print(temp)
        i +=1

  t = test()
  t.__next__()
  t.send("haha")

4.多任务（协程）
==================================

.. code-block:: python

  def test1():
    while True:
      print('-------1---------')
      yield 

  def test2():
    while True:
      print('-------2---------')
      yield

  t1 = test1()
  t2 = test2()
  while True:
    t1.__next__()
    t2.__next__()


在yield掉所有的值后，next()触发了⼀个StopIteration的异常。基本上这个异常告诉我们，所有的值都已经被yield完了。你也许会奇怪，为什么我们在使⽤for循环时没有这个异常呢？啊哈，答案很简单。for循环会⾃动捕捉到这个异常并停⽌调⽤next()。

5.内置函数iter
================================

iter。它将根据⼀个可迭代对象返回⼀个迭代器对象。

.. code-block:: python

  my_string = "Baidu"
  my_iter = iter(my_string)
  next(my_iter)
 