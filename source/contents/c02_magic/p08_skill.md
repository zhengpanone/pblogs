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

```bash
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

## 4、如何流式读取数G超大文件

使用 with…open… 可以从一个文件中读取数据，这是所有 Python 开发者都非常熟悉的操作。

但是如果你使用不当，也会带来很大的麻烦。

比如当你使用了 read 函数，其实 Python 会将文件的内容一次性的全部载入内存中，如果文件有 10 个G甚至更多，那么你的电脑就要消耗的内存非常巨大。

```python
# 一次性读取
with open("big_file.txt", "r") as fp:
    content = fp.read()
```

对于这个问题，你也许会想到使用 `readline` 去做一个生成器来逐行返回。

```python
def read_from_file(filename):
    with open(filename, "r") as fp:
        yield fp.readline()
```

可如果这个文件内容就一行呢，一行就 10个G，其实你还是会一次性读取全部内容。

最优雅的解决方法是，在使用 read 方法时，指定每次只读取固定大小的内容，比如下面的代码中，每次只读取 8kb 返回。

```python
def read_from_file(filename, block_size = 1024 * 8):
    with open(filename, "r") as fp:
        while True:
            chunk = fp.read(block_size)
            if not chunk:
                break

            yield chunk
```

上面的代码，功能上已经没有问题了，但是代码看起来代码还是有些臃肿。

借助偏函数 和 iter 函数可以优化一下代码

```python
from functools import partial

def read_from_file(filename, block_size = 1024 * 8):
    with open(filename, "r") as fp:
        for chunk in iter(partial(fp.read, block_size), ""):
            yield chunk
```

## 5、如何快速计算函数运行时间

计算一个函数的运行时间，你可能会这样子做

```python
import time

start = time.time()

# run the function

end = time.time()
print(end-start)
```

你看看你为了计算函数运行时间，写了几行代码了。 有没有一种方法可以更方便的计算这个运行时间呢？  有。  有一个内置模块叫 timeit  使用它，只用一行代码即可

```python
import time
import timeit

def run_sleep(second):
    print(second)
    time.sleep(second)

# 只用这一行
print(timeit.timeit(lambda :run_sleep(2), number=5))
```

运行结果如下

```bash
2
2
2
2
2
10.020059824
```

## 6、没有root如何安装模块

`pip install --user pkg`

