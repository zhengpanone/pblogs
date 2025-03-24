=========================
re模块操作
=========================

1. re模块操作
=========================

.. code-block:: python
    :linenos:

    import re      # 导入re模块
    result = re.match('正则表达式','要匹配的字符')
    result.group()     # 如果上一步匹配到数据，可以使用group来提取数据

**re.match是用来进行正则匹配检查的方法，若字符串匹配正则表达式，则match方法返回匹配对象（Match Object）,否则返回None（不是空字符串""）**

匹配对象Match Object 具有group方法,用来返回字符串的匹配部分

示例：

.. code-block:: python
    :linenos:

    import re
    result = re.match('itcast','itcast.com')
    result.group()
    >>> itcast

.. csv-table:: 正则对应关系!
   :widths: 50, 70 
   :file: code/01_regx/regx_map.csv
   :encoding: utf-8
   :align: left

贪婪模式和非贪婪模式
----------------------------------

.. literalinclude:: ./code/01_regx/greed_match.py
    :encoding: utf-8
    :language: python
    :emphasize-lines: 5
    :linenos: