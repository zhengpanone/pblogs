===============
3. Buffer
===============

概念
===========
Buffer意为缓冲区，是一个类似Array的对象，用于表示固定长度的字节序列。Buffer是一段固定长度的内存空间，用于处理二进制数据

特点
=========

1. Buffer大小固定且无法调整
#. Buffer性能较好，可以直接对计算机内存进行操作
#. 每个元素的大小为1字节（byte）

使用
==========

1、创建Buffer示例

.. literalinclude:: ./code/p03_buffer/01_创建buffer.js
    :encoding: utf-8
    :language: js
    :linenos:

2、操作Buffer示例

.. literalinclude:: ./code/p03_buffer/02_操作buffer.js
    :encoding: utf-8
    :language: js
    :linenos: