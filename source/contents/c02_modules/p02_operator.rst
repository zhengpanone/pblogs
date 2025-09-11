============
operator
============

``operator`` 是Python标准库中提供运算符函数化的工具包，

主要解决：

- 替代简单lambda表达式
- 简化函数式编程操作
- 优化对象比较和属性访问
- 提升代码可读性和性能

算术运算符函数
================

作用：将数学运算符转化为函数

.. code-block:: python

  import operator as op

  print(op.add(10, 5))      # 15 → 10+5
  print(op.sub(20, 7))      # 13 → 20-7
  print(op.mul(3, 4))       # 12 → 3*4
  print(op.truediv(10, 3))  # 3.33 → 10/3
  print(op.floordiv(10, 3)) # 3 → 10//3
  print(op.mod(15, 4))      # 3 → 15%4
  print(op.pow(2, 3))       # 8 → 2**3

比较运算符函数
=================


作用：将比较运算符转化为函数

.. code-block:: python

  import operator as op

  print(op.eq(10, 10))     # True → 10==10
  print(op.ne(10, 20))     # True → 10!=20
  print(op.gt(15, 10))     # True → 15>10
  print(op.lt(5, 10))      # True → 5<10
  print(op.ge(10, 10))     # True → 10>=10
  print(op.le(8, 10))      # True → 8<=10

  # 链式比较示例
  values = [15, 20, 25, 30]
  is_increasing = all(op.lt(a, b) for a, b in zip(values, values[1:]))
  print(f"列表是否递增: {is_increasing}")  # True

序列操作函数
==============

作用：高效处理序列操作

.. code-block:: python

  import operator as op

  # 序列拼接
  print(op.concat([1,2], [3,4]))  # [1,2,3,4]

  # 包含判断
  print(op.contains("Python", "Py"))  # True → "Py" in "Python"

  # 元素计数
  print(op.countOf("mississippi", "i"))  # 4 → 统计'i'出现次数

  # 索引获取
  get_second = op.itemgetter(1)
  print(get_second(["A", "B", "C"]))  # 'B'

属性访问神器
==================

作用：简化对象属性访问

.. literalinclude:: ./code/ p02_operator/operator_attr.py
    :encoding: utf-8
    :language: python

方法调用器
===========

作用：动态调用对象方法

.. literalinclude:: ./code/ p02_operator/operator_methodcall.py
    :encoding: utf-8
    :language: python

原地操作函数
=================

作用：执行就地修改操作

.. literalinclude:: ./code/ p02_operator/operator_opsfunc.py
    :encoding: utf-8
    :language: python

实战应用场景
===================

- 排序简化：用attrgetter/itemgetter替代lambda
- 数据处理：配合map/filter进行高效操作
- 动态调用：根据配置调用不同对象方法
- 数学计算：构建可配置的运算管道
- 对象处理：批量提取对象属性

.. literalinclude:: ./code/ p02_operator/operator_usage.py
    :encoding: utf-8
    :language: python

注意事项
===================
- 基本类型不可变，原地操作对数字/字符串无效
- attrgetter比手动getattr更高效
- 简单操作直接使用运算符更直观
- methodcaller支持任何可调用方法