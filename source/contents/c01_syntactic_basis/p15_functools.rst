=========================
15. functools模块
=========================

偏函数partial用法
==========================

.. code-block:: python
    :linenos:

    functools.partial(func[,*args][, **kwargs])

如何使用
>>>>>>>>>>>>>>>>>>

假设有如下函数：

.. code-block:: python
    :linenos:

    def multiply(x, y):
        return x * y

现在，我们想返回某个数的双倍，即

.. code-block:: python
    :linenos:

    multiply(3, y=2)
    multiply(4, y=2)
    multiply(5, y=2)

上面的调用有点繁琐，每次都要传入 y=2，我们想到可以定义一个新的函数，把 y=2 作为默认值，即：

.. code-block:: python
    :linenos:

    def double(x, y=2):
        return multiply(x,y)

现在，我们可以这样调用了：

.. code-block:: python
    :linenos:

    double(3)
    double(4)
    double(5)

事实上，我们可以不用自己定义 double，利用 partial，我们可以这样：

.. code-block:: python
    :linenos:

    from functools import partial 

    double = partial(multiply, y=2)

partial 接收函数 multiply 作为参数，固定 multiply 的参数 y=2，并返回一个新的函数给 double，这跟我们自己定义 double 函数的效果是一样的。所以，简单而言，partial 函数的功能就是：把一个函数的某些参数给固定住，返回一个新的函数。需要注意的是，我们上面是固定了 multiply 的关键字参数 y=2，如果直接使用：

.. code-block:: python
    :linenos:

    double = partial(multiply, 2)

则 2 是赋给了 multiply 最左边的参数 x

