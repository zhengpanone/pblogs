===============================
高阶函数
===============================

Map,Filter
===============================

Map
-------------

map将函数应用于可迭代对象内每一个元素之上 。Map需要2个输入，分别是应用函数和可迭代对象

.. code-block:: python
    
  map(function_to_apply,iterable)

.. literalinclude:: ./code/p04_High_level_function/map_demo.py
    :encoding: utf-8
    :language: python
    

Filter
-------------

filter函数采用可迭代的方式，并过滤掉可迭代中不需要的内容

.. code-block:: python
    
  filter(function,list)

.. code-block:: python
    
  x = range(-5,5)
  all_less_than_zero = list(filter(lambda num:num<0),x)



functools
====================================

``functools`` 是Python标准库中专门用于高阶函数的工具包，主要提供函数式编程支持，能让你：操作或扩展其他函数缓存计算结果实现函数装饰器减少重复代码

partial：冻结参数
---------------------------

作用：固定函数的部分参数，生成新函数

.. literalinclude:: ./code/p04_High_level_function/partial_demo.py
    :encoding: utf-8
    :language: python

lru_cache：智能缓存
---------------------------

作用：自动缓存函数结果，避免重复计算

.. literalinclude:: ./code/p04_High_level_function/lru_cache_demo.py
    :encoding: utf-8
    :language: python

wraps：保留元数据
---------------------------

作用：解决装饰器导致的原函数信息丢失问题

.. literalinclude:: ./code/p04_High_level_function/wraps_demo.py
    :encoding: utf-8
    :language: python

reduce：累积计算
---------------------------

作用：对可迭代对象进行累积操作, Reduce 是将迭代变成一个东西的函数。通常可以在列表上使用reduce函数执行计算以将其减少到一个数字

.. code-block:: python
    
  reduce(function, list)

经常使用lambda表达式作为函数

.. literalinclude:: ./code/p04_High_level_function/reduce_demo.py
    :encoding: utf-8
    :language: python

total_ordering：简化比较操作
----------------------------------

作用：只需定义__eq__和一个比较方法，自动生成全部比较运算符

.. literalinclude:: ./code/p04_High_level_function/total_ordering.py
    :encoding: utf-8
    :language: python


