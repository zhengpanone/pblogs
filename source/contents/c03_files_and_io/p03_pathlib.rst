===========================
3. Pathlib使用
===========================

pathlib 是Python内置库，Python 文档给它的定义是 Object-oriented filesystem paths（面向对象的文件系统路径）。pathlib 提供表示文件系统路径的类，其语义适用于不同的操作系统。路径类在纯路径之间划分，纯路径提供纯粹的计算操作而没有I / O，以及具体路径，它继承纯路径但也提供I / O操作。

获取当前文件路径
============================

.. code-block:: python
    :linenos:

    import pathlib
    value1 = pathlib.Path.cwd()
    print(value1)

实现原理
>>>>>>>>>>>>>>>>>

它以 os.getcwd() 的形式将路径返回

源码：

.. code-block:: python
    :linenos:

    @classmethod
    def cwd(cls):
        """Return a new path pointing to the current working directory
            (as returned by os.getcwd()).
        """
        return cls(os.getcwd())

它是对 os 模块中一些对象进行了封装

其他的封装
=======================

pathlib 封装了很多的 os path ，文档中有写明，如：

.. code-block:: python
    :linenos:

    # 关系说明
    os.path.expanduser() --> pathlib.Path.home()
    os.path.expanduser() --> pathlib.Path.expanduser()
    os.stat() --> path.Path.stat()
    os.chmod() --> pathlib.Path.chmod()

## Pathlib 便捷性

获取上上层目录
>>>>>>>>>>>>>>>>>>>>>>>>

os 模块的写法

.. code-block:: python
    :linenos:

    import os
    print(os.path.dirname(os.path.dirname(os.getcwd())))

pathlib的写法

.. code-block:: python
    :linenos:

    import pathlib
    print(pathlib.Path.cwd().parent.parent)

路径拼接
>>>>>>>>>>>>>>>>>>>>>>>

os 模块的写法

.. code-block:: python
    :linenos:

    import os
    print(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),"path1","path2","path3"))

pathlib的写法

.. code-block:: python
    :linenos:

    import pathlib
    parts=["path1","path2","path3"]
    print(pathlib.Path.cwd().parent.parent.joinpath(*parts))

获取绝对路径
>>>>>>>>>>>>>>>>>>>>

.. code-block:: python
    :linenos:

    import pathlib
    print(path.Path('./').resolve())

PurePath
=====================

PurePath 是一个纯路径对象，纯路径对象提供了实际上不访问文件系统的路径处理操作。有三种方法可以访问这些类，我们也称之为flavor。

PurePath.match
>>>>>>>>>>>>>>>>>>>>>>>>>

判断，当前文件路径是否有符合 \*.py 规则的文件

.. code-block:: python
    :linenos: 

    import pathlib
    print(pathlib.PurePath(__file__).match("*.py"))
    
pathlib.PurePath 后面能够跟着 match，那说明它应该是个对象，而不是一个路径字符串。

.. code-block:: python
    :linenos:

    import pathlib
    import os
    os_path = os.path.dirname(__file__)
    pure_path = pathlib.PurePath(__file__)
    print(os_path,type(os_path))
    print(pure_path,type(pure_path))
    print(pathlib.PurePath(__file__).math("*.py"))

打印通过 os.path 获取当前路径的结果，得出一个路径字符串；而通过 pathlib.Pure 则获得的是一个 **PurePosixPath** 对象，并且得到的路径包括了当前文件 coder.py。

PurePosixPath 究竟是什么？

​	pathlib可以操作两种文件系统路径，一种是Windows文件系统，一种非Windows系统，对应的对象是pathlib.PurePosixPath和PureWindowsPath，这些类并非是指定在某些操作系统上运行才能够使用，无论你运行的是哪个系统，都可以实例化所有这些类，因为它们不提供任何进行系统调用的操作。

文档在最开始给出了这么一段描述:

> Pure paths are useful in some special cases; for example:
> If you want to manipulate Windows paths on a Unix machine (or vice versa). You cannot instantiate a WindowsPath when running on Unix, but you can instantiate PureWindowsPath.
> You want to make sure that your code only manipulates paths without actually accessing the OS. In this case, instantiating one of the pure classes may be useful since those simply don’t have any OS-accessing operations.

> 翻译：纯路径在某些特殊情况下很有用; 例如：
> 如果要在Unix计算机上操作Windows路径（反之亦然）。WindowsPath在Unix上运行时无法实例化，但可以实例化PureWindowsPath。
> 您希望确保您的代码仅操作路径而不实际访问操作系统。在这种情况下，实例化其中一个纯类可能很有用，因为那些只是没有任何操作系统访问操作。

|image1|


对应关系
=======================

pathlib不仅封装了 os.path 相关常用方法，还集成了 os 的其他模块，比如创建文件夹 Path.mkdir。

.. csv-table:: 对应关系!
   :header: "os and os.path", "pathlib", "用途"
   :widths: 15, 10, 30
   :file: code/03_pathlib/os_pathlib.csv
   :encoding: utf-8
   :align: left

基本用法
>>>>>>>>>>>>>>>>>>>>>>

Path.iterdir()　　# 遍历目录的子目录或者文件

Path.is_dir()　　# 判断是否是目录

Path.resolve()　　# 返回绝对路径

Path.exists()　　# 判断路径是否存在

Path.unlink()　　# 删除文件或目录(目录非空触发异常)

Path.glob() #过滤目录(返回生成器)

Path.open() # 打开文件(支持with)

基本属性
>>>>>>>>>>>>>>>>>

Path.parts  # 分割路径 类似os.path.split(), 返回元组

Path.drive  # 返回驱动器名称

Path.root   # 返回路径的根目录

Path.anchor # 自动判断返回drive或root

Path.parents    # 返回所有上级目录的列表

Path.name   # 没有任何目录的文件名

Path.parent # 包含该文件的目录,如果path是目录,则是父目录

Path.stem   # 文件名不带后缀

Path.suffix #文件扩展名

改变路径
>>>>>>>>>>>>>>>>>>

Path.with_name()    # 更改路径名称,更改最后一级路径名

Path.with_suffix()  # 更改路径后缀

拼接路径
>>>>>>>>>>>>>>>>>>

Path.joinpath() # 拼接路径

Path.relative_to()  # 计算相对路径

测试路径
>>>>>>>>>>>>>>>>>>>>

Path.match()　　# 测试路径是否符合pattern

Path.is_dir()　　# 是否是文件

Path.is_absolute()　　# 是否是绝对路径

Path.is_reserved()　　# 是否是预留路径

Path.exists()　　# 判断路径是否真实存在

其他方法
>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Path.cwd()　　# 返回当前目录的路径对象

Path.home()　　# 返回当前用户的home路径对象

Path.stat()　　# 返回路径信息, 同os.stat()

Path.chmod()　　# 更改路径权限, 类似os.chmod()

Path.expanduser()　　# 展开~返回完整路径对象

Path.mkdir()　　# 创建目录

Path.rename()　　# 重命名路径

Path.rglob()　　# 递归遍历所有子目录的文件

注意
=====================

1. path.parent不等于pathlib.Path.cwd（），因为path.parent用"."表示。 而pathlib.Path.cwd（）由"/home/gahjelle/realpython/"表示。
#. 将Path转换为str,Python 3.6及更高版本中，如果需要进行显式转换，建议使用os.fspath()而不是str()


/运算符
========================

/运算符由\.__ truediv __()方法定义。 事实上，如果你看看pathlib的源代码，你会看到类似于：

.. code-block:: python
    :linenos:

    class PurePath(object):

        def __truedir__(self, key):
            return self._make_chil((key,))


.. |image1| image:: ./image/640.webp

https://mp.weixin.qq.com/s/4Lf-t_8WrAPYEvfG8sKEtg


pathlib用列
====================


1、基础用例
>>>>>>>>>>>>>>>>>>>>>>>>>>>>

有一个目录里装了很多数据文件，但是它们的后缀名并不统一，既有 .txt，又有 .csv。我们需要把其中以 .txt 结尾的文件都修改为 .csv 后缀名。

.. code-block:: python
    :linenos:

    from pathlib import Path

    def unify_ext_with_path(path):
        for fpath in Path(path).glob('*.txt'):
            fpath.rename(fpath.with_suffix('.csv'))


2、如何流式读取大文件
>>>>>>>>>>>>>>>>>>>>>>>>>>>>

2.1 初步版本
::::::::::::::::::::::::::

.. code-block:: python
    :linenos:

    def count_nine(fnames):
        """
            计算文件中包含多少个数字9
        """
        count = 0
        with open(fname) as file:
            for line in file:
                count += line.count('9')
        return count 

如果被读取的文件里，根本就没有任何换行符。当代码执行到 forlineinfile 时，line 将会变成一个非常巨大的字符串对象，消耗掉非常可观的内存。

2.2 使用 read 方法分块读取
:::::::::::::::::::::::::::::::::::

.. code-block:: python 
    :linenos:

    def count_nine_v2(fname):
        """
        计算文件里包含多少个数字 '9'，每次读取 8kb
        """
        count = 0
        block_size = 1024*8
        with open(fname) as fp:
            while True:
                chunk = fp.read(block_size)
                if not chunk:
                    break
                count += chunk.count('9')
        return count

2.3 利用生成器解耦合
:::::::::::::::::::::::::::::::::::


 count_nine_v2 函数，你会发现在循环体内部，存在着两个独立的逻辑：数据生成（read 调用与 chunk 判断） 与 数据消费。而这两个独立逻辑被耦合在了一起。

我们可以定义一个新的 chunked_file_reader 生成器函数，由它来负责所有与“数据生成”相关的逻辑。这样 count_nine_v3 里面的主循环就只需要负责计数即可。

.. code-block:: python
    :linenos:

    def chunked_file_reader(fp, block_size=1024*8):
        """
        生成器函数：分块读取文件内容
        """

        while True:
            chunk = fp.read(block_size)
            if not chunk:
                break
            yield chunk

    def count_nine_v3(fname):
        count = 0
        with open(fname) as fp:
            for chunk in chunked_file_reader(fp):
                count += chunk.count('9')

        return count

2.4 iter() 函数优化chunk_file_reader()
:::::::::::::::::::::::::::::::::::::::::::::::::::::

iter(iterable) 是一个用来构造迭代器的内建函数，但它还有一个更少人知道的用法。当我们使用 iter(callable,sentinel) 的方式调用它时，会返回一个特殊的对象，迭代它将不断产生可调用对象 callable 的调用结果，直到结果为 setinel 时，迭代终止。

.. code-block:: python
    :linenos:

    from functools import partial

    def chunked_file_reader(file, block_size=1024*8):
        """
        生成器函数：分块读取文件内容，使用 iter 函数
        """
        # 首先使用 partial(fp.read, block_size) 构造一个新的无需参数的函数
        # 循环将不断返回 fp.read(block_size) 调用结果，直到其为 '' 时终止

        for chunk in iter(partial(file.read, block_size),''):
            yield chunk

2.5 设计接受文件对象的函数
:::::::::::::::::::::::::::::::::::

统计完文件里的 “9” 之后，让我们换一个需求。现在，我想要统计每个文件里出现了多少个英文元音字母（aeiou）。只要对之前的代码稍作调整，很快就可以写出新函数 count_vowels。

.. code-block:: python 
    :linenos:

    def count_vowels(filename):
        """
        统计某个文件中，包含元音字母(aeiou)的数量
        """

        VOWELS_LETTERS = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        with open(filename, 'r') as fp:
            for line in fp:
                for char in line:
                    if char.lower() in VOWELS_LETTERS:
                        count += 1
        return count

和之前“统计 9”的函数相比，新函数变得稍微复杂了一些。为了保证程序的正确性，我需要为它写一些单元测试。但当我准备写测试时，却发现这件事情非常麻烦，主要问题点如下：

1. 函数接收文件路径作为参数，所以我们需要传递一个实际存在的文件
#. 为了准备测试用例，我要么提供几个样板文件，要么写一些临时文件
#. 而文件是否能被正常打开、读取，也成了我们需要测试的边界情况

如果，你发现你的函数难以编写单元测试，那通常意味着你应该改进它的设计。上面的函数应该如何改进呢？答案是：让函数依赖“文件对象”而不是文件路径。 

修改后的函数代码如下：

.. code-block:: python
    :linenos:

    def count_vowels_v2(fp):
        """
        统计某个文件中，包含元音字母(aeiou)的数量
        """

        VOWELS_LETTERS = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        for line in fp:
            for char in line:
                if char.lower() in VOWELS_LETTERS:
                    count += 1
        return count

    with open('small_file.txt') as fp:
        print(count_vowels_v2(fp))

这个改动带来的主要变化，在于它提升了函数的适用面。因为 Python 是“鸭子类型”的，虽然函数需要接受文件对象，但其实我们可以把任何实现了文件协议的 “类文件对象（file-like object）” 传入 count_vowels_v2 函数中。

而 Python 中有着非常多“类文件对象”。比如 io 模块内的 StringIO 对象就是其中之一。它是一种基于内存的特殊对象，拥有和文件对象几乎一致的接口设计。

利用 StringIO，我们可以非常方便的为函数编写单元测试。   


.. code-block:: python
    :linenos:

    import pytest
    from io import StringIO
    @pytest.mark.parametrize(
    "content, vowels_count",[
        # 使用 pytest 提供的参数化测试工具，定义测试参数列表    
        # (文件内容, 期待结果)
        ('', 0),
        ('Hello World！', 3),
        ('HELLO WORLD!', 3),
        ('你好，世界', 0),
    ]
    )
    def test_count_vowels_v2(content, vowels_count):
        # 利用 StringIO 构造类文件对象 "file"
        file = StringIO(content)
        assert count_vowels_v2(file) == vowels_count

而让编写单元测试变得更简单，并非修改函数依赖后的唯一好处。除了 StringIO 外，subprocess 模块调用系统命令时用来存储标准输出的 PIPE 对象，也是一种“类文件对象”。这意味着我们可以直接把某个命令的输出传递给 count_vowels_v2 函数来计算元音字母数：

.. code-block:: python 
    :linenos:

    import subprocess
    # 统计 /tmp 下面所有一级子文件名（目录名）有多少元音字母
    p = subprocess.Popen(['ls', '/tmp'], stdout=subprocess.PIPE, encoding='utf-8')
    # p.stdout 是一个流式类文件对象，可以直接传入函数
    print(count_vowels_v2(p.stdout))

将函数参数修改为“文件对象”，最大的好处是提高了函数的 适用面 和 可组合性。通过依赖更为抽象的“类文件对象”而非文件路径，给函数的使用方式开启了更多可能，StringIO、PIPE 以及任何其他满足协议的对象都可以成为函数的客户。

不过，这样的改造并非毫无缺点，它也会给调用方带来一些不便。假如调用方就是想要使用文件路径，那么就必须得自行处理文件的打开操作。

2.6 编写兼容二者的函数
:::::::::::::::::::::::::::::::::::

打开标准库里的 xml.etree.ElementTree 模块，翻开里面的 ElementTree.parse 方法。你会发现这个方法即可以使用文件对象调用，也接受字符串的文件路径。而它实现这一点的手法也非常简单易懂：

.. code-block:: python
    :linenos:

    def parse(self, source, parser=None):
        """
        *source* is a file name or file object, *parser* is an optional parser
        """
        close_source = False
        # 通过判断 source 是否有 "read" 属性来判定它是不是“类文件对象” 
        # 如果不是，那么调用 open 函数打开它并负担起在函数末尾关闭它的责任
        if not hasattr(source, 'read'):
            source = open(source, 'rb')
            close_source = True 

修改可以接受文件对象有可以接受文件路径

.. code-block:: python
    :linenos:

    def count_vowels_v3(fp):
        VOWELS_LETTERS = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        close_source = False
        if not  hasattr(fp, 'read'):
            fp = open(fp, 'r')
            close_source=True
        for line in fp:
            for char in line:
                if char.lower() in VOWELS_LETTERS:
                    count += 1
        if close_source:
            fp.close()

        return count




