# 上下文管理器

## 1、what context manager？

**基本语法**

```python
with EXPR as VAR:
    BLOCK
```

先理清几个概念

```text
1. 上下文表达式：with open('test.txt') as f:
2. 上下文管理器：open('test.txt')
3. f 不是上下文管理器，应该是资源对象。
```

## 2、how context manager？

要自己实现这样一个上下文管理，要先知道上下文管理协议。

简单点说，就是在一个类里，实现了`__enter__`和`__exit__`的方法，这个类的实例就是一个上下文管理器。

例如这个示例：

```python
class Resource():
    def __enter__(self):
        print('===connect to resource===')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('===close resource connection===')

    def operate(self):
        print('===in operation===')

with Resource() as res:
    res.operate()
```

我们执行一下，通过日志的打印顺序。可以知道其执行过程。

```text
===connect to resource===
===in operation===
===close resource connection===
```

从这个示例可以很明显的看出，在编写代码时，可以将资源的连接或者获取放在`__enter__`中，而将资源的关闭写在`__exit__` 中。

## 3、why context manager？

学习时多问自己几个为什么，养成对一些细节的思考，有助于加深对知识点的理解。

为什么要使用上下文管理器？

在我看来，这和 Python 崇尚的优雅风格有关。

1. 可以以一种更加优雅的方式，操作（创建/获取/释放）资源，如文件操作、数据库连接；
2. 可以以一种更加优雅的方式，处理异常；

第一种，我们上面已经以资源的连接为例讲过了。

而第二种，会被大多数人所忽略。这里会重点讲一下。

大家都知道，处理异常，通常都是使用 `try...execept..` 来捕获处理的。这样做一个不好的地方是，在代码的主逻辑里，会有大量的异常处理代理，这会很大的影响我们的可读性。

好一点的做法呢，可以使用 `with` 将异常的处理隐藏起来。

仍然是以上面的代码为例，我们将`1/0` 这个`一定会抛出异常的代码`写在 `operate` 里

```python
class Resource():
    def __enter__(self):
        print('===connect to resource===')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('===close resource connection===')
        return True

    def operate(self):
        1/0

with Resource() as res:
    res.operate()
```

运行一下，惊奇地发现，居然不会报错。

这就是上下文管理协议的一个强大之处，异常可以在`__exit__` 进行捕获并由你自己决定如何处理，是抛出呢还是在这里就解决了。在`__exit__` 里返回 `True`（没有return 就默认为 return False），就相当于告诉 Python解释器，这个异常我们已经捕获了，不需要再往外抛了。

在 写`__exit__` 函数时，需要注意的事，它必须要有这三个参数：

- `exc_type`：异常类型
- `exc_val`：异常值
- `exc_tb`：异常的错误栈信息

当主逻辑代码没有报异常时，这三个参数将都为None。

## 4、how contextlib?

在上面的例子中，我们只是为了构建一个上下文管理器，却写了一个类。如果只是要实现一个简单的功能，写一个类未免有点过于繁杂。这时候，我们就想，如果只写一个函数就可以实现上下文管理器就好了。

这个点Python早就想到了。它给我们提供了一个装饰器，你只要按照它的代码协议来实现函数内容，就可以将这个函数对象变成一个上下文管理器。

我们按照 `contextlib` 的协议来自己实现一个打开文件（with open）的上下文管理器。

```python
import contextlib

@contextlib.contextmanager
def open_func(file_name):
    # __enter__方法
    print('open file:', file_name, 'in __enter__')
    file_handler = open(file_name, 'r')

    # 【重点】：yield
    yield file_handler

    # __exit__方法
    print('close file:', file_name, 'in __exit__')
    file_handler.close()
    return

with open_func('/Users/MING/mytest.txt') as file_in:
    for line in file_in:
        print(line)
```

在被装饰函数里，必须是一个生成器（带有yield），而yield之前的代码，就相当于`__enter__`里的内容。yield 之后的代码，就相当于`__exit__` 里的内容。

上面这段代码只能实现上下文管理器的第一个目的（管理资源），并不能实现第二个目的（处理异常）。

如果要处理异常，可以改成下面这个样子。

```python
import contextlib

@contextlib.contextmanager
def open_func(file_name):
    # __enter__方法
    print('open file:', file_name, 'in __enter__')
    file_handler = open(file_name, 'r')

    try:
        yield file_handler
    except Exception as exc:
        # deal with exception
        print('the exception was thrown')
    finally:
        print('close file:', file_name, 'in __exit__')
        file_handler.close()

        return

with open_func('/Users/MING/mytest.txt') as file_in:
    for line in file_in:
        1/0
        print(line)
```

好像只要讲到上下文管理器，大多数人都会谈到打开文件这个经典的例子。

但是在实际开发中，可以使用到上下文管理器的例子也不少。我这边举个我自己的例子。

在`OpenStack`中，给一个虚拟机创建快照时，需要先创建一个临时文件夹，来存放这个本地快照镜像，等到本地快照镜像创建完成后，再将这个镜像上传到Glance。然后删除这个临时目录。

这段代码的主逻辑是`创建快照`，而`创建临时目录`，属于前置条件，`删除临时目录`，是收尾工作。

虽然代码量很少，逻辑也不复杂，但是“`创建临时目录，使用完后再删除临时目录`”这个功能，在一个项目中很多地方都需要用到，如果可以将这段逻辑处理写成一个工具函数作为一个上下文管理器，那代码的复用率也大大提高。

代码是这样的

![image1](image/p07context_manager.assets/20190310172800.png)

总结起来，使用上下文管理器有三个好处：

1. 提高代码的复用率；
2. 提高代码的优雅度；
3. 提高代码的可读性；

