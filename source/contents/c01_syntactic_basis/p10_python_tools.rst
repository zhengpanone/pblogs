=============================
Python小工具
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
    

http://liyangliang.me/posts/2015/06/deploy-applications-using-fabric/


使用 supervisor 管理进程
====================================

http://liyangliang.me/posts/2015/06/using-supervisor/


python自带小型数据库
=========================

https://mp.weixin.qq.com/s/Zw3duGaX2Alr3Nd-fFGMmw

dbm
>>>>>>>>


DBM（DataBase Manager）是一种文件系统，专门用于键值对的存储，最初是在 Unix 平台实现，现在其它平台也可以用。对于 KV 模型，DBM 提供了一个轻量级、高效的存储解决方案。

总的来说，DBM 具有如下特点：

- 简单快速：非常简单易用，读取和写入操作都很快，适合存储少量数据。

- 键值对存储：数据是以键值对形式存储的，你可以像操作 Python 字典一样。

- 文件存储：数据存在具体的文件中，可以轻松地备份和转移。

- 不支持复杂查询：如果需要执行复杂查询或需要关系型数据库的功能，DBM 可能不是一个好选择。


而 Python 标准库提供了一个 dbm 模块，它实现了 DBM 文件系统的功能，来看一下它的用法。

.. literalinclude:: ./code/p10/01_dbm.py
    :encoding: utf-8
    :language: python
    

非常简单，当你需要存储的数据量不适合放在内存中，但又没必要引入数据库，那么不妨试试使用 dbm 模块吧。

当然啦，dbm 虽然很方便，但它只能持久化 bytes 对象，字符串也是转成 bytes 对象之后再存储的。所以除了 dbm 之外，还有一个标准库模块 shelve，它可以持久化任意对象。

shelve
>>>>>>>>>>>

shelve 的使用方式和 dbm 几乎是一致的，区别就是 shelve 的序列化能力要更强，当然速度自然也就慢一些。

.. literalinclude:: ./code/p10/02_shelve.py
    :encoding: utf-8
    :language: python
    

读取出来的就是原始的对象，我们可以直接操作它。

然后自定义类的实例对象也是可以的。

shelve 模块，非常强大，当然它底层也是基于 pickle 实现的。如果你不需要存储复杂的 Python 对象，只需要存储字符串的话，那么还是推荐 dbm。

然后在使用 shelve 的时候，需要注意里面的一个坑。

.. literalinclude:: ./code/p10/03_shelve.py
    :encoding: utf-8
    :language: python
    

第一次打开文件创建两个键值对，第二次打开文件将键值对修改，第三次打开文件查看键值对。但是我们发现 sh["name"] 变了，而 sh["score"] 却没变，这是什么原因？

当我们修改 name 时，采用的是直接赋值的方式，会将原本内存里的值给替换掉。而修改 score 时，是在原有值的基础上做 append 操作，它的内存地址并没有变。

所以可变对象在本地进行修改，shelve 默认是不会记录的，除非创建新的对象，并把原有的对象给替换掉。所以 sh["score"].append(90) 之后，sh["score"] 仍是 [80, 80, 80]，而不是 [80, 80, 80, 90]。

因为 shelve 没有记录对象自身的修改，如果想得到期望的结果，一种方法是把对象整体换掉。也就是让 sh["score"] = [80, 80, 80, 90]，这样等于是创建了一个新的对象并重新赋值，是可行的。

或者你在打开文件的时候，多指定一个参数 writeback。

.. literalinclude:: ./code/p10/04_shelve.py
    :encoding: utf-8
    :language: python
    

可以看到都发生改变了，但这个参数会导致额外的内存消耗。当指定 writeback=True 的时候，shelve 会将读取的对象都放到一个内存缓存当中。比如我们操作了 20 个持久化的对象，但只修改了一个，剩余的 19 个只是查看并没有做修改，但当 sh.close() 的时候，会将这 20 个对象都写回去。

因为 shelve 不知道你会对哪个对象做修改，所以不管你是查看还是修改，都会放到缓存当中，然后再一次性都写回去。这样就会造成两点影响：

shelve 会把我们使用的对象放到内存的另一片空间中，等于是额外拷贝了一份。

虽然操作了 N 个对象，但只修改了 1 个，而 shelve 会把 N 个对象都重新写回去，从而造成性能上的问题，导致效率降低。


因此加不加这个参数，由具体情况决定。