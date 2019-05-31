=============================
Python小工具
=============================

数据库命令行工具：mycli
==============================

.. note::

 mycli -u root -h 127.0.0.1 -p root --database your_db_name -P 3306

python debug工具：PySnooper
==================================

.. note::

 pip install pysnooper 

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