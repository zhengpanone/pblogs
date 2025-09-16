==================
property
==================

基础用法
==================

只读属性
----------------------

最简单的就是只提供 ``getter``，不给 ``setter``，这样属性就是只读的。

.. literalinclude:: ./code/03_property/circle_demo1.py
    :encoding: utf-8
    :language: python

带有 ``setter`` 的属性
----------------------

.. literalinclude:: ./code/03_property/circle_demo2.py
    :encoding: utf-8
    :language: python

带有 ``deleter`` 的属性
----------------------------

.. literalinclude:: ./code/03_property/circle_demo3.py
    :encoding: utf-8
    :language: python

延迟计算 & 缓存
--------------------

有些属性计算成本高，可以用 property 包装，并结合缓存：

.. literalinclude:: ./code/03_property/lazy_calc.py
    :encoding: utf-8
    :language: python

用于 延迟计算，类似 @functools.cached_property。

模拟只读/保护字段（如密码）
-------------------------------

.. literalinclude:: ./code/03_property/private_attr.py
    :encoding: utf-8
    :language: python

衍生的其他用法
==================
.. literalinclude:: ./code/03_property/rectangle.py
    :encoding: utf-8
    :language: python
