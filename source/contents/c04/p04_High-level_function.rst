===============================
高阶函数
===============================

Map,Filter和Reduce

Map
===========================

map将函数应用于可迭代对象内每一个元素之上 。Map需要2个输入，分别是应用函数和可迭代对象

.. code-block:: python
    

    map(function_to_apply,iterable)

.. literalinclude:: ./code/p04_High_level_function/map_demp.py
    :encoding: utf-8
    :language: python
    

Filter
====================================

filter函数采用可迭代的方式，并过滤掉可迭代中不需要的内容

.. code-block:: python
    

    filter(function,list)

.. code-block:: python
    

    x = range(-5,5)
    all_less_than_zero = list(filter(lambda num:num<0),x)

Reduce
====================================

Reduce 是将迭代变成一个东西的函数。通常可以在列表上使用reduce函数执行计算以将其减少到一个数字

.. code-block:: python
    

    reduce(function, list)

经常使用lambda表达式作为函数

.. code-block:: python
    

    product = 1
    x = [1,2,3,4]
    for num in x:
        product = product * num

reduce 改写：

.. code-block:: python
    

    from functools import reduce
    product = reduce((lambda x ,y : x * y),[1,2,3,4])

