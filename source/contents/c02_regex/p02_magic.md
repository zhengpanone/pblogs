# 2.python 魔法知识

## 连接多个列表

```python
a = [1,2]
b = [3,4]
c = [5,6]

sum((a,b,c),[])
```
## 如何查找python安装目录

```python
from distutils.sysconfig import get_python_lib
print(get_python_lib())
```

## 直接运行zip包

![](.\image\p02_magic\20200812194811.png)

```python
python -m zipfile -c demo.zip demo/*
```

## /usr/bin/env python有什么用

### \#!/usr/bin/python



而当你在可执行文件头里使用 `#!` + `/usr/bin/python` ，意思就是说你得用哪个软件 （python）来执行这个文件。

### #!/usr/bin/env python

当你执行 `env python` 时，它其实会去 `env | grep PATH` 里（也就是 /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin ）这几个路径里去依次查找名为python的可执行文件。

应该优先使用 `#!/usr/bin/env python`，因为不是所有的机器的 python 解释器都是 `/usr/bin/python`

## dict() 与 {} 生成空字典有什么区别

在运行效率上，{} 会比 dict() 快三倍左右。

```python
python -m timeit -n 1000000 -r 5 -v "dict()"
```

```python
python -m timeit -n 1000000 -r 5 -v "{}"
```

### why

```
{}
$
$ python -m dis demo.py
  1           0 BUILD_MAP                0
              2 POP_TOP
              4 LOAD_CONST               0 (None)
              6 RETURN_VALUE
```

```
dict()
$
$ python -m dis demo.py
  1           0 LOAD_NAME                0 (dict)
              2 CALL_FUNCTION            0
              4 POP_TOP
              6 LOAD_CONST               0 (None)
              8 RETURN_VALUE
```

可以发现使用 dict()，会多了个调用函数的过程，而这个过程会有进出栈的操作，相对更加耗时。

## return不一定都是函数的终点

```
>>>def func():
...     try:
...         return 'try'
...     finally:
...         return 'finally'
...
>>> func()
'finally'
```

从输出中，我们可以发现：在try…finally…语句中，try中的 return 会被直接忽视（这里的 return 不是函数的终点），因为要保证 finally 能够执行。

### **如果 try 里的 return 真的是直接被忽视吗？**

```
>>> def func():
...     try:
...         return 'try'
...     finally:
...         print('finally')
...
>>>
>>> func()
finally
'try'
>>>
```

从结果来看，当 finally 下没有 reutrn ，其实 try 里的 return 仍然还是有效的。

那结论就出来了，如果 finally 里有显式的 return，那么这个 return 会直接覆盖 try 里的 return，而如果 finally 里没有 显式的 return，那么 try 里的 return 仍然有效。

## 去除Counter中的负数

```
>>> from collections import Counter
>>> ct = Counter('abcdbcaa')
>>> ct
Counter({'a': 3, 'b': 2, 'c': 2, 'd': 1})
>>> ct['c'] = 0
>>> ct['d'] = -2
>>>
>>> ct
Counter({'a': 3, 'b': 2, 'c': 0, 'd': -2})
>>>
>>> +ct
Counter({'a': 3, 'b': 2})
```

## += 不等同于=+

对列表 进行`+=` 操作相当于 extend，而使用 `=+` 操作是新增了一个列表。

因此会有如下两者的差异。

```
# =+
>>> a = [1, 2, 3, 4]
>>> b = a
>>> a = a + [5, 6, 7, 8]
>>> a
[1, 2, 3, 4, 5, 6, 7, 8]
>>> b
[1, 2, 3, 4]


# +=
>>> a = [1, 2, 3, 4]
>>> b = a
>>> a += [5, 6, 7, 8]
>>> a
[1, 2, 3, 4, 5, 6, 7, 8]
>>> b
[1, 2, 3, 4, 5, 6, 7, 8]
```

## break /continue 和 上下文管理器哪个优先级高

但如果把上下文管理器放在一个循环体中，而在这个上下文管理器中执行了 break ，是否会直接跳出循环呢？

换句话说，上下文管理器与 break/continue 这两个规则哪一个优先级会更高一些？

这个问题其实不难，只要做一下试验都能轻易地得出答案，难就难在很多对这个答案都是半猜半疑，无法肯定的回答。

试验代码如下：

```python
import time
import contextlib

@contextlib.contextmanager
def runtime(value):
    time.sleep(1)
    print("start: a = " + str(value))
    yield
    print("end: a = " + str(value))


a = 0
while True:
    a+=1
    with runtime(a):
        if a % 2 == 0:
            break
```

从输出的结果来看，当 a = 2 时执行了 break ，此时的并不会直接跳出循环，依然要运行上下文管理器里清理释放资源的代码（示例中，我使用 print 来替代）。

```
start: a = 1
end: a = 1
start: a = 2
end: a = 2
```

另外还有几个与此类似的问题，我这里也直接给出答案，不再细说了

1. continue 与 break 一样，如果先遇到上下文管理器会先进行资源的释放
2. 上面只举例了 while 循环体，而 for 循环也是同样的。