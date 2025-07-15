========================
yield 使用
========================

带有yield的函数在python中称之为generator(生成器)

如何生成斐波那契数列

.. code-block:: python

  def fab(max):
      n,a,b = 0, 0, 1
      while n < max:
          print(b)
          a, b = b, a+b
          n = n + 1

执行fab(5)

通过命名表达式生成斐波那契数列

>>> (lambda f: f(f, int(input("Input: ")),1,0,1))(lambda f,t,i,a,b: print(f'fib({i})={b}') or t==i or f(f,t,i+1,b,a+b))

基于Raymond Hettinger版本改写

>>> [(t:=(t[1], sum(t)) if i else (0,1))[1] for i in range(10)]

.. code-block:: pycon

  >>> fab(5)
  1
  1
  2
  3
  5

直接在 fab 函数中用 print 打印数字会导致该函数可复用性较差，因为 fab 函数返回 None，其他函数无法获得该函数生成的数列。

要提高 fab 函数的可复用性，最好不要直接打印出数列，而是返回一个 List。以下是 fab函数改写后的第二个版本：


.. code-block:: python

  def fab(max):
      n, a, b = 0, 0, 1
      L = []
      while n < max:
          L.append(b)
          a, b = b, a + b
          n = n + 1
      return L

.. code-block:: pycon

  >>> for n in fab(5):
  >>>   print(n)
  1
  1
  2
  3
  5

函数在运行中占用的内存会随着参数 max 的增大而增大，如果要控制内存占用，最好不要用 List


利用 iterable 我们可以把 fab 函数改写为一个支持 iterable 的 class，以下是第三个版本的 Fab：

.. code-block:: python

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

.. code-block:: pycon

  >>> for n in Fab(5):
        print(n)
 
  1
  1
  2
  3
  5

使用class改写的没有第一版简洁,想要简洁且获得iterable的效果,使用yield:

.. code-block:: python

  def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
      yield b
      # print(b)
      a, b = b, a + b
      n = n + 1


.. code-block:: pycon

  >>> for n in fab(5):
  >>>   print(n)
  1
  1
  2
  3
  5

yield 的作用是把函数变成一个generator,带有yield的函数不再是一个普通函数,Python解释器会将其视为一个generator,调用fab(5) 不会执行fab函数,而是返回一个iterable对象！在for循环执行时,每次循环都会执行fab函数内部代码,执行到yield b时,fab函数就返回一个迭代值,下次迭代时,代码从yield b 的下一条语句继续执行,而函数的本地变量看起来和上次中断执行前时完全一样的,于是函数继续执行,直到再次遇到yield.

也可以手动调用 fab(5) 的 next() 方法（因为 fab(5) 是一个 generator 对象，该对象具有 next() 方法），这样我们就可以更清楚地看到 fab 的执行流程：

.. code-block:: pycon

   >>> f = fab(5)
   >>> next(f)
   1
   >>> next(f)
   1
   >>> next(f)
   2
   >>> next(f)
   3
   >>> next(f)
   5
   >>> next(f)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   StopIteration


当函数执行结束时，generator 自动抛出 StopIteration 异常，表示迭代完成。在 for 循环里，无需处理 StopIteration 异常，循环会正常结束。

我们可以得出以下结论：


yield实现生产者消费者模型
================================

.. literalinclude:: ./code/p03_yield/01_consume_produce.py
    :encoding: utf-8
    :language: python
    