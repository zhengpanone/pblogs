=============================
10. Python小工具
=============================

数据库命令行工具：mycli
==============================

>>> mycli -u root -h 127.0.0.1 -p root --database your_db_name -P 3306

python debug工具：PySnooper
==================================

>>> pip install pysnooper 

.. code:: python 

 import pysnooper 

 def number_to_bits(number):
    if number:
        bits = []
        while number:
            number, remainder = divmod(number, 2)
            bits.insert(0, remainder)
        return bits 
    else:
        return [0]
 
 number_to_bits(6)

fabric 实现自动化部署
===========================

.. literalinclude:: ./code/01.fabric_发布项目.py
    :encoding: utf-8
    :language: python
    :emphasize-lines: 3
    :lines: 1-
    :linenos:

http://liyangliang.me/posts/2015/06/deploy-applications-using-fabric/


使用 supervisor 管理进程
====================================

http://liyangliang.me/posts/2015/06/using-supervisor/
