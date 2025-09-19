=========================
Python 内建的类机制
=========================

对象模型控制
=========================

.. list-table:: 对象模型控制
   :header-rows: 1
   :widths: 20 40 40

   * - 特性
     - 说明
     - 示例
   * - __slots__
     - 限定对象能有哪些属性，节省内存，禁止动态添加新属性
     - __slots__ = ("x", "y")
   * - __dict__
     - 默认存储对象实例属性的字典
     - obj.__dict__
   * - __weakref__
     - 支持弱引用
     - 自动存在于对象中（如不定义 __slots__）
   * - __mro__
     - 类的继承解析顺序 (Method Resolution Order)
     - MyClass.__mro__
   * - __bases__
     - 父类元组
     - MyClass.__bases__
   * - __class__
     - 对象所属的类
     - obj.__class__
  
__slots__
---------

- **作用**: 限制类实例可以拥有的属性集合，从而节省内存、加快属性访问速度。
- **使用方法**::

.. code-block:: python

  class Person:
      __slots__ = ('name', 'age')  # 限定实例只能有这两个属性

      def __init__(self, name, age):
          self.name = name
          self.age = age

  p = Person("Alice", 20)
  p.name  # ✅ 有效
  p.age   # ✅ 有效
  p.address = "Beijing"  # ❌ AttributeError: 'Person' object has no attribute 'address'

- **特点**:
  
  * 禁止动态添加新属性（除非定义在 ``__slots__`` 内）。
  * 移除了 ``__dict__``，减少内存开销。
  * 常用于需要创建大量实例的类。

__dict__
--------

- **作用**: 存储对象的可写属性，通常是一个字典。
- **说明**: 动态类实例默认都有 ``__dict__``，除非使用 ``__slots__`` 限制。

__weakref__
-----------

- **作用**: 允许对象被弱引用，用于缓存和避免循环引用。
- **使用场景**: 当类定义了 ``__slots__`` 时，如果想要支持弱引用，需要显式加入::

.. code-block:: python

    class Node:
        __slots__ = ('value', '__weakref__')

__mro__
-------

- **作用**: 方法解析顺序 (Method Resolution Order)，用于确定多继承情况下方法查找的顺序。
- **示例**::

.. code-block:: python

  class A: pass
  class B(A): pass
  class C(A): pass
  class D(B, C): pass

  print(D.__mro__)  # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)




对象创建与生命周期
=========================

.. list-table:: 对象创建与生命周期
   :header-rows: 1
   :widths: 20 80

   * - 特性
     - 说明
   * - __new__
     - 控制实例创建（返回对象本身），常用于单例、元类
   * - __init__
     - 初始化实例属性
   * - __del__
     - 析构函数（对象销毁时调用，不推荐依赖）

__new__ 与 __init__
-------------------

- **__new__**
  * 作用: 控制对象的创建过程，返回一个实例。
  * 用法: 常用于实现单例模式或继承不可变类型（如 ``int``, ``str``）。

- **__init__**
  * 作用: 初始化对象的属性。
  * 区别: ``__new__`` 在对象创建之前调用，``__init__`` 在对象创建之后调用。



属性访问与管理
=========================

.. list-table:: 属性访问与管理
   :header-rows: 1
   :widths: 20 80

   * - 特性
     - 说明
   * - __getattr__
     - 访问不存在的属性时调用
   * - __getattribute__
     - 所有属性访问都会调用，优先级高于 __getattr__
   * - __setattr__
     - 设置属性时调用
   * - __delattr__
     - 删除属性时调用
   * - __dir__
     - dir(obj) 时调用，返回属性列表

容器类协议
=========================

.. list-table:: 容器类协议
   :header-rows: 1
   :widths: 20 80

   * - 特性
     - 说明
   * - __len__
     - len(obj)
   * - __getitem__
     - obj[key]
   * - __setitem__
     - obj[key] = value
   * - __delitem__
     - del obj[key]
   * - __iter__
     - for x in obj:
   * - __next__
     - next(obj)
   * - __contains__
     - x in obj

可调用与上下文管理
=========================

.. list-table:: 可调用与上下文管理
   :header-rows: 1
   :widths: 20 80

   * - 特性
     - 说明
   * - __call__
     - 让对象可调用：obj()
   * - __enter__
     - with obj as x: 进入上下文
   * - __exit__
     - with 块结束时调用

描述符协议（属性代理机制）
=========================

.. list-table:: 描述符协议（属性代理机制）
   :header-rows: 1
   :widths: 20 80

   * - 特性
     - 说明
   * - __get__
     - 访问属性时调用
   * - __set__
     - 设置属性时调用
   * - __delete__
     - 删除属性时调用

运算符重载
=========================

.. list-table:: 运算符重载
   :header-rows: 1
   :widths: 20 80

   * - 特性
     - 对应运算
   * - __add__
     - +
   * - __sub__
     - -
   * - __mul__
     - *
   * - __truediv__
     - /
   * - __floordiv__
     - //
   * - __mod__
     - %
   * - __pow__
     - \*\*
   * - __eq__
     - ==
   * - __ne__
     - !=
   * - __lt__
     - <
   * - __le__
     - <=
   * - __gt__
     - >
   * - __ge__
     - >=
   * - __hash__
     - hash(obj)
   * - __bool__
     - bool(obj)
   * - __str__
     - str(obj)
   * - __repr__
     - repr(obj)


类对象的内部实现机制 / 类闭包支持
===================================

__classcell__
-------------

- **作用**: 在 Python 3 中用于支持 ``super()`` 调用的内部机制。
- **通常不直接使用**: 由编译器自动生成。

当你在 类定义中 使用 ``@classmethod``、``super()`` 或闭包引用当前类时，Python 会生成一个 “类闭包 cell”。

这个闭包 cell 就被存储在 ``__classcell__`` 中。

它的作用是 确保方法体内可以访问类对象本身，即使类还没有完全创建完成。

简单来说：

.. code-block:: python

  class A:
    def method(self):
        return super()  # 这里会用到 __classcell__

  print(A.__dict__.get('__classcell__'))
  # <cell at 0x101901040: class '__main__.A'>

当你使用 ``super()`` 或类方法时，Python 会用 ``__classcell__`` 传递类引用，保证方法内部可以引用当前类。

说明它是一个 cell 类型对象，存储了类对象。当你创建普通实例或调用方法时，不会直接看到它，也不需要手动赋值。
