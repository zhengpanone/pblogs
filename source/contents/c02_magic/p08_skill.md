# 魔法开发小技巧

## 1、嵌套上下文管理的写法

```python
with open(file1) as f1 ,open(file2) as f2:
	pass
```

## 2、嵌套for循环写成单行

我们经常会如下这种嵌套的 for 循环代码

```python
list1 = range(1,3)
list2 = range(4,6)
list3 = range(7,9)
for item1 in list1:
    for item2 in list2:
        for item3 in list3:
              print(item1+item2+item3)
```

这里仅仅是三个 for 循环，在实际编码中，有可能会有更层。

这样的代码，可读性非常的差，很多人不想这么写，可又没有更好的写法。

这里介绍一种我常用的写法，使用 `itertools` 这个库来实现更优雅易读的代码。

```python
from itertools import product
list1 = range(1,3)
list2 = range(4,6)
list3 = range(7,9)
for item1,item2,item3 in product(list1, list2, list3):
    print(item1+item2+item3)
```

输出如下

```
$ python demo.py
12
13
13
14
13
14
14
15
```

## 3、单行实现for死循环

```python
for i in iter(int, 1):pass
```

原来`iter`有两种使用方法。

- 通常我们的认知是第一种，将一个列表转化为一个迭代器。
- 而第二种方法，他接收一个 callable对象，和一个sentinel 参数。第一个对象会一直运行，直到它返回 sentinel 值才结束。

那`int` 呢？

这又是一个知识点，int 是一个内建方法。通过看注释，可以看出它是有默认值0的。你可以在console 模式下输入 `int()` 看看是不是返回0。

由于int() 永远返回0，永远返回不了1，所以这个 for 循环会没有终点。一直运行下去。

## 

