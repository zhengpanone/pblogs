=======================
4.2 生成器
=======================

生成器 是将推导式的[] 改成(), 不会将所有的一次性加载到内存中，延迟计算，一次返回一个结果，不会一次生成所有的结果, 处理大数据非常有用

::

 def fun():
    for i in range(1,50):
        yield i
 for i in fun():
    print(i)

生成器函数：一个函数中包含yield关键字, 这个函数是一个生成器函数
调用生成器函数,不会立马执行该函数里的代码,而返回一个生成器

::

 def func():
    print('a')
    yield
    print('b')
    yield
    print('c')
    yield
    print('d')

 generator = func()
 print(generator)
 print(type(generator))
 for i in generator:
    pass


::

 sum(x for x in range(1000000000)) # 占用内存少
 sum([x for x in range(1000000000)]) # 占用内存大

原理: sum 函数是python3内置函数,该函数使用迭代器协议访问对象,而生成器实现了迭代器协议,所以可以直接计算一系列值的和,不用先构造一个列表
