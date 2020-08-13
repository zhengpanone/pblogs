# 4、魔法操作

## 1、9中连接列表的方式

### 1、+

使用 `+` 对多个列表进行相加

```
>>> list01 = [1,2,3]
>>> list02 = [4,5,6]
>>> list03 = [7,8,9]
>>>
>>> list01 + list02 + list03
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
```

### 2、借助 itertools

itertools 在 Python 里有一个非常强大的内置模块，它专门用于操作可迭代对象。

使用 `itertools.chain()` 函数先可迭代对象（在这里指的是列表）串联起来，组成一个更大的可迭代对象。

最后你再利用 list 将其转化为 列表。

```
>>> from itertools import chain
>>> list01 = [1,2,3]
>>> list02 = [4,5,6]
>>> list03 = [7,8,9]
>>>
>>> list(chain(list01, list02, list03))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
```

### 3、使用 * 解包

使用 `*` 可以解包列表，解包后再合并。

示例如下：

```
>>> list01 = [1,2,3]
>>> list02 = [4,5,6]
>>>
>>> [*list01, *list02]
[1, 2, 3, 4, 5, 6]
>>>
```

### 4、使用 extend

在字典中，使用 update 可实现原地更新，而在列表中，使用 extend 可实现列表的自我扩展。

```
>>> list01 = [1,2,3]
>>> list02 = [4,5,6]
>>>
>>> list01.extend(list02)
>>> list01
[1, 2, 3, 4, 5, 6]
```

### 5、使用列表推导式

Python 里对于生成列表、集合、字典，有一套非常 Pythonnic 的写法。

那就是列表解析式，集合解析式和字典解析式，通常是 Python 发烧友的最爱，那么今天的主题：列表合并，列表推导式还能否胜任呢？

当然可以，具体示例代码如下：

```
>>> list01 = [1,2,3]
>>> list02 = [4,5,6]
>>> list03 = [7,8,9]
>>>
>>> [x for l in (list01, list02, list03) for x in l]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
```

### 6、使用 heapq

heapq 是 Python 的一个标准模块，它提供了堆排序算法的实现。

该模块里有一个 merge 方法，可以用于合并多个列表，如下所示

```
>>> list01 = [1,2,3]
>>> list02 = [4,5,6]
>>> list03 = [7,8,9]
>>>
>>> from heapq import merge
>>>
>>> list(merge(list01, list02, list03))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
```

要注意的是，heapq.merge 除了合并多个列表外，它还会将合并后的最终的列表进行排序。

```
>>> list01 = [2,5,3]
>>> list02 = [1,4,6]
>>> list03 = [7,9,8]
>>>
>>> from heapq import merge
>>>
>>> list(merge(list01, list02, list03))
[1, 2, 4, 5, 3, 6, 7, 9, 8]
>>>
```

它的效果等价于下面这行代码：

```
sorted(itertools.chain(*iterables))
```

如果你希望得到一个始终有序的列表，那请第一时间想到 heapq.merge，因为它采用堆排序，效率非常高。但若你不希望得到一个排过序的列表，就不要使用它了。

### 7、借助魔法方法

有一个魔法方法叫 `__add__`，当我们使用第一种方法 list01 + list02 的时候，内部实际上是作用在 `__add__` 这个魔法方法上的。

所以以下两种方法其实是等价的

```
>>> list01 = [1,2,3]
>>> list02 = [4,5,6]
>>>
>>> list01 + list02
[1, 2, 3, 4, 5, 6]
>>>
>>>
>>> list01.__add__(list02)
[1, 2, 3, 4, 5, 6]
>>>
```

借用这个魔法特性，我们可以 reduce 这个方法来对多个列表进行合并，示例代码如下

```
>>> list01 = [1,2,3]
>>> list02 = [4,5,6]
>>> list03 = [7,8,9]
>>>
>>> from functools import reduce
>>> reduce(list.__add__, (list01, list02, list03))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
```

### 8. 使用 yield from

在 yield from 后可接一个可迭代对象，用于迭代并返回其中的每一个元素。

因此，我们可以像下面这样自定义一个合并列表的工具函数。

```
>>> list01 = [1,2,3]
>>> list02 = [4,5,6]
>>> list03 = [7,8,9]
>>>
>>> def merge(*lists):
...   for l in lists:
...     yield from l
...
>>> list(merge(list01, list02, list03))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>
```

### 9、sum

```
a = [1,2]
b = [3,4]
c = [5,6]

sum((a,b,c),[])
```

## 2、合并字典的 8 种方法

### 1、update

字典对象内置了一个 update 方法，用于把另一个字典更新到自己身上。

```
>>> profile = {"name": "xiaoming", "age": 27}
>>> ext_info = {"gender": "male"}
>>>
>>> profile.update(ext_info)
>>> print(profile)
{'name': 'xiaoming', 'age': 27, 'gender': 'male'}
```

如果想使用 update 这种最简单、最地道原生的方法，但又不想更新到自己身上，而是生成一个新的对象，那请使用深拷贝。

```
>>> profile = {"name": "xiaoming", "age": 27}
>>> ext_info = {"gender": "male"}
>>>
>>> from copy import deepcopy
>>>
>>> full_profile = deepcopy(profile)
>>> full_profile.update(ext_info)
>>>
>>> print(full_profile)
{'name': 'xiaoming', 'age': 27, 'gender': 'male'}
>>> print(profile)
{"name": "xiaoming", "age": 27}
```

### 2、先解包再合并字典

使用 `**` 可以解包字典，解包完后再使用 dict 或者 `{}` 就可以合并。

```
>>> profile = {"name": "xiaoming", "age": 27}
>>> ext_info = {"gender": "male"}
>>>
>>> full_profile01 = {**profile, **ext_info}
>>> print(full_profile01)
{'name': 'xiaoming', 'age': 27, 'gender': 'male'}
>>>
>>> full_profile02 = dict(**profile, **ext_info)
>>> print(full_profile02)
{'name': 'xiaoming', 'age': 27, 'gender': 'male'}
```

若你不知道 `dict(**profile, **ext_info)` 做了啥，你可以将它等价于

```
>>> dict((("name", "xiaoming"), ("age", 27), ("gender", "male")))
{'name': 'xiaoming', 'age': 27, 'gender': 'male'}
```

### 3、借助 itertools

在 Python 里有一个非常强大的内置模块，它专门用于操作可迭代对象。

正好我们字典也是可迭代对象，自然就可以想到，可以使用 `itertools.chain()` 函数先将多个字典（可迭代对象）串联起来，组成一个更大的可迭代对象，然后再使用 dict 转成字典。

```
>>> import itertools
>>>
>>> profile = {"name": "xiaoming", "age": 27}
>>> ext_info = {"gender": "male"}
>>>
>>>
>>> dict(itertools.chain(profile.items(), ext_info.items()))
{'name': 'xiaoming', 'age': 27, 'gender': 'male'}
```

### 4、借助 ChainMap

如果可以引入一个辅助包，那我就再提一个， `ChainMap` 也可以达到和 `itertools` 同样的效果。

```
>>> from collections import ChainMap
>>>
>>> profile = {"name": "xiaoming", "age": 27}
>>> ext_info = {"gender": "male"}
>>>
>>> dict(ChainMap(profile, ext_info))
{'name': 'xiaoming', 'age': 27, 'gender': 'male'}
```

使用 ChainMap 有一点需要注意，当字典间有重复的键时，只会取第一个值，排在后面的键值并不会更新掉前面的（使用 itertools 就不会有这个问题）。

```
>>> from collections import ChainMap
>>>
>>> profile = {"name": "xiaoming", "age": 27}
>>> ext_info={"age": 30}
>>> dict(ChainMap(profile, ext_info))
{'name': 'xiaoming', 'age': 27}
```

### 5、使用dict.items() 合并

在 Python 3.9 之前，其实就已经有 `|` 操作符了，只不过它通常用于对集合（set）取并集。

利用这一点，也可以将它用于字典的合并，只不过得绕个弯子，有点不好理解。

你得先利用 `items` 方法将 dict 转成 dict_items，再对这两个 dict_items 取并集，最后利用 dict 函数，转成字典。

```
>>> profile = {"name": "xiaoming", "age": 27}
>>> ext_info = {"gender": "male"}
>>>
>>> full_profile = dict(profile.items() | ext_info.items())
>>> full_profile
{'gender': 'male', 'age': 27, 'name': 'xiaoming'}
```

当然了，你如果嫌这样太麻烦，也可以简单点，直接使用 list 函数再合并（示例为 Python 3.x ）

```
>>> profile = {"name": "xiaoming", "age": 27}
>>> ext_info = {"gender": "male"}
>>>
>>> dict(list(profile.items()) + list(ext_info.items()))
{'name': 'xiaoming', 'age': 27, 'gender': 'male'}
```

若你在 Python 2.x 下，可以直接省去 list 函数。

```
>>> profile = {"name": "xiaoming", "age": 27}
>>> ext_info = {"gender": "male"}
>>>
>>> dict(profile.items() + ext_info.items())
{'name': 'xiaoming', 'age': 27, 'gender': 'male'}
```

### 6、最酷炫的字典解析式

Python 里对于生成列表、集合、字典，有一套非常 Pythonnic 的写法。

那就是列表解析式，集合解析式和字典解析式，通常是 Python 发烧友的最爱，那么今天的主题：字典合并，字典解析式还能否胜任呢？

当然可以，具体示例代码如下：

```
>>> profile = {"name": "xiaoming", "age": 27}
>>> ext_info = {"gender": "male"}
>>>
>>> {k:v for d in [profile, ext_info] for k,v in d.items()}
{'name': 'xiaoming', 'age': 27, 'gender': 'male'}
```

### 7、Python 3.9 新特性

在 2 月份发布的 Python 3.9.04a 版本中，新增了一个抓眼球的新操作符操作符： `|`， PEP584 将它称之为合并操作符（Union Operator），用它可以很直观地合并多个字典。

```
>>> profile = {"name": "xiaoming", "age": 27}
>>> ext_info = {"gender": "male"}
>>>
>>> profile | ext_info
{'name': 'xiaoming', 'age': 27, 'gender': 'male'}
>>>
>>> ext_info | profile
{'gender': 'male', 'name': 'xiaoming', 'age': 27}
>>>
>>>
```

除了 `|` 操作符之外，还有另外一个操作符 `|=`，类似于原地更新。

```
>>> ext_info |= profile
>>> ext_info
{'gender': 'male', 'name': 'xiaoming', 'age': 27}
>>>
>>>
>>> profile |= ext_info
>>> profile
{'name': 'xiaoming', 'age': 27, 'gender': 'male'}
```

## 3、花式导包的八种方法

### 1. 直接 import

人尽皆知的方法，直接导入即可

```
>>> import os
>>> os.getcwd()
'/home/wangbm'
```

与此类似的还有，不再细讲

```
import ...
import ... as ...
from ... import ...
from ... import ... as ...
```

一般情况下，使用 `import` 语句导入模块已经够用的。

但是在一些特殊场景中，可能还需要其他的导入方式。

下面我会一一地给你介绍。

### 2. 使用 __import__

`__import__` 函数可用于导入模块，import 语句也会调用函数。其定义为：

```
__import__(name[, globals[, locals[, fromlist[, level]]]])
```

参数介绍：

- name (required): 被加载 module 的名称
- globals (optional): 包含全局变量的字典，该选项很少使用，采用默认值 global()
- locals (optional): 包含局部变量的字典，内部标准实现未用到该变量，采用默认值 - local()
- fromlist (Optional): 被导入的 submodule 名称
- level (Optional): 导入路径选项，Python 2 中默认为 -1，表示同时支持 absolute import 和 relative import。Python 3 中默认为 0，表示仅支持 absolute import。如果大于 0，则表示相对导入的父目录的级数，即 1 类似于 ‘.’，2 类似于 ‘..’。

使用示例如下：

```
>>> os = __import__('os')
>>> os.getcwd()
'/home/wangbm'
```

如果要实现 `import xx as yy` 的效果，只要修改左值即可

如下示例，等价于 `import os as myos`：

```
>>> myos = __import__('os')
>>> myos.getcwd()
'/home/wangbm'
```

上面说过的 `__import__` 是一个内建函数，既然是内建函数的话，那么这个内建函数必将存在于 `__buildins__` 中，因此我们还可以这样导入 os 的模块：

```
>>> __builtins__.__dict__['__import__']('os').getcwd()
'/home/wangbm'
```

### 3. 使用 importlib 模块

importlib 是 Python 中的一个标准库，importlib 能提供的功能非常全面。

它的简单示例：

```
>>> import importlib
>>> os=importlib.import_module("os")
>>> os.getcwd()
'/home/wangbm'
```

如果要实现 `import xx as yy`效果，可以这样

```
>>> import importlib
>>>
>>> myos = importlib.import_module("os")
>>> myos.getcwd()
'/home/wangbm'
```

### 4. 使用 imp 模块

`imp` 模块提供了一些 import 语句内部实现的接口。例如模块查找（find_module）、模块加载（load_module）等等（模块的导入过程会包含模块查找、加载、缓存等步骤）。可以用该模块来简单实现内建的 `__import__` 函数功能：

```
>>> import imp
>>> file, pathname, desc = imp.find_module('os')
>>> myos = imp.load_module('sep', file, pathname, desc)
>>> myos
<module 'sep' from '/usr/lib64/python2.7/os.pyc'>
>>> myos.getcwd()
'/home/wangbm'
```

从 python 3 开始，内建的 reload 函数被移到了 imp 模块中。而从 Python 3.4 开始，imp 模块被否决，不再建议使用，其包含的功能被移到了 importlib 模块下。即从 Python 3.4 开始，importlib 模块是之前 imp 模块和 importlib 模块的合集。

### 5. 使用 execfile

在 Python 2 中有一个 execfile 函数，利用它可以用来执行一个文件。

语法如下：

```
execfile(filename[, globals[, locals]])
```

参数有这么几个：

- filename：文件名。
- globals：变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
- locals：变量作用域，局部命名空间，如果被提供，可以是任何映射对象。

```
>>> execfile("/usr/lib64/python2.7/os.py")
>>>
>>> getcwd()
'/home/wangbm'
```

### 6. 使用 exec 执行

`execfile` 只能在 Python2 中使用，Python 3.x 里已经删除了这个函数。

但是原理值得借鉴，你可以使用 open … read 读取文件内容，然后再用 exec 去执行模块。

示例如下：

```
>>> with open("/usr/lib64/python2.7/os.py", "r") as f:
...     exec(f.read())
...
>>> getcwd()
'/home/wangbm'
```

### 7. import_from_github_com

有一个包叫做 **import_from_github_com**，从名字上很容易得知，它是一个可以从 github 下载安装并导入的包。为了使用它，你需要做的就是按照如下命令使用pip 先安装它。

```
$ python3 -m pip install import_from_github_com
```

这个包使用了PEP 302中新的引入钩子，允许你可以从github上引入包。这个包实际做的就是安装这个包并将它添加到本地。你需要 Python 3.2 或者更高的版本，并且 git 和 pip 都已经安装才能使用这个包。

pip 要保证是较新版本，如果不是请执行如下命令进行升级。

```
$ python3 -m pip install --upgrade pip
```

确保环境 ok 后，你就可以在 Python shell 中使用 import_from_github_com

示例如下

```
>>> from github_com.zzzeek import sqlalchemy
Collecting git+https://github.com/zzzeek/sqlalchemy
Cloning https://github.com/zzzeek/sqlalchemy to /tmp/pip-acfv7t06-build
Installing collected packages: SQLAlchemy
Running setup.py install for SQLAlchemy ... done
Successfully installed SQLAlchemy-1.1.0b1.dev0
>>> locals()
{'__builtins__': <module 'builtins' (built-in)>, '__spec__': None,
'__package__': None, '__doc__': None, '__name__': '__main__',
'sqlalchemy': <module 'sqlalchemy' from '/usr/local/lib/python3.5/site-packages/\
sqlalchemy/__init__.py'>,
'__loader__': <class '_frozen_importlib.BuiltinImporter'>}
>>>
```

看了 import_from_github_com的源码后，你会注意到它并没有使用importlib。实际上，它的原理就是使用 pip 来安装那些没有安装的包，然后使用Python的`__import__()`函数来引入新安装的模块。

### 8、远程导入模块

我在这篇文章里（[深入探讨 Python 的 import 机制：实现远程导入模块](http://mp.weixin.qq.com/s?__biz=MzIzMzMzOTI3Nw==&mid=2247484838&idx=1&sn=1e6fbf5d7546902c6965c60383f7b639&chksm=e8866544dff1ec52e01b6c9a982dfa150b8e34ad472acca35201373dc51dadb5a8630870982a&scene=21#wechat_redirect)），深入剖析了导入模块的内部原理，并在最后手动实现了从远程服务器上读取模块内容，并在本地成功将模块导入的导入器。

具体内容非常的多，你可以点击这个[链接](http://mp.weixin.qq.com/s?__biz=MzIzMzMzOTI3Nw==&mid=2247484838&idx=1&sn=1e6fbf5d7546902c6965c60383f7b639&chksm=e8866544dff1ec52e01b6c9a982dfa150b8e34ad472acca35201373dc51dadb5a8630870982a&scene=21#wechat_redirect)进行深入学习。

示例代码如下：

```
# 新建一个 py 文件（my_importer.py），内容如下
import sys
import importlib
import urllib.request as urllib2

class UrlMetaFinder(importlib.abc.MetaPathFinder):
    def __init__(self, baseurl):
        self._baseurl = baseurl


    def find_module(self, fullname, path=None):
        if path is None:
            baseurl = self._baseurl
        else:
            # 不是原定义的url就直接返回不存在
            if not path.startswith(self._baseurl):
                return None
            baseurl = path

        try:
            loader = UrlMetaLoader(baseurl)
            return loader
        except Exception:
            return None

class UrlMetaLoader(importlib.abc.SourceLoader):
    def __init__(self, baseurl):
        self.baseurl = baseurl

    def get_code(self, fullname):
        f = urllib2.urlopen(self.get_filename(fullname))
        return f.read()

    def get_data(self):
        pass

    def get_filename(self, fullname):
        return self.baseurl + fullname + '.py'

def install_meta(address):
    finder = UrlMetaFinder(address)
    sys.meta_path.append(finder)
```

并且在远程服务器上开启 http 服务（为了方便，我仅在本地进行演示），并且手动编辑一个名为 my_info 的 python 文件，如果后面导入成功会打印 `ok`。

```
$ mkdir httpserver && cd httpserver
$ cat>my_info.py<EOF
name='wangbm'
print('ok')
EOF
$ cat my_info.py
name='wangbm'
print('ok')
$
$ python3 -m http.server 12800
Serving HTTP on 0.0.0.0 port 12800 (http://0.0.0.0:12800/) ...
...
```

一切准备好，验证开始。

```
>>> from my_importer import install_meta
>>> install_meta('http://localhost:12800/') # 往 sys.meta_path 注册 finder
>>> import my_info  # 打印ok，说明导入成功
ok
>>> my_info.name  # 验证可以取得到变量
'wangbm'
```

## 4、条件语句的七种写法

### 第一种：原代码

这是一段非常简单的通过年龄判断一个人是否成年的代码，由于代码行数过多，有些人就不太愿意这样写，因为这体现不出自己多年的 Python 功力。

```
if age > 18:
    return "已成年"
else:
    return "未成年"
```

下面我列举了六种这段代码的变异写法，一个比一个还 6 ，单独拿出来比较好理解，放在工程代码里，没用过这些学法的人，一定会看得一脸懵逼，理解了之后，又不经意大呼：**卧槽，还可以这样写？**，而后就要开始骂街了：**这是给人看的代码？** （除了第一种之外）

### 第二种

语法：

```
<on_true> if <condition> else <on_false>
```

例子

```
>>> age1 = 20
>>> age2 = 17
>>>
>>>
>>> msg1 = "已成年" if age1 > 18 else "未成年"
>>> print msg1
已成年
>>>
>>> msg2 = "已成年" if age2 > 18 else "未成年"
>>> print msg2
未成年
>>>
```

### 第三种

语法

```
<condition> and <on_true> or <on_false>
```

例子

```
>>> msg1 = age1 > 18 and "已成年" or "未成年"
>>> msg2 = "已成年" if age2 > 18 else "未成年"
>>>
>>> print(msg1)
已成年
>>>
>>> print(msg2)
未成年
```

### 第四种

语法

```
(<on_false>, <on_true>)[condition]
```

例子

```
>>> msg1 = ("未成年", "已成年")[age1 > 18]
>>> print(msg1)
已成年
>>>
>>>
>>> msg2 = ("未成年", "已成年")[age2 > 18]
>>> print(msg2)
未成年
```

### 第五种

语法

```
(lambda: <on_false>, lambda:<on_true>)[<condition>]()
```

例子

```
>>> msg1 = (lambda:"未成年", lambda:"已成年")[age1 > 18]()
>>> print(msg1)
已成年
>>>
>>> msg2 = (lambda:"未成年", lambda:"已成年")[age2 > 18]()
>>> print(msg2)
未成年
```

### 第六种

语法：

```
{True: <on_true>, False: <on_false>}[<condition>]
```

例子：

```
>>> msg1 = {True: "已成年", False: "未成年"}[age1 > 18]
>>> print(msg1)
已成年
>>>
>>> msg2 = {True: "已成年", False: "未成年"}[age2 > 18]
>>> print(msg2)
未成年
```

### 第七种

语法

```
((<condition>) and (<on_true>,) or (<on_false>,))[0]
```

例子

```
>>> msg1 = ((age1 > 18) and ("已成年",) or ("未成年",))[0]
>>> print(msg1)
已成年
>>>
>>> msg2 = ((age2 > 18) and ("已成年",) or ("未成年",))[0]
>>> print(msg2)
未成年
```

## 5、判断是否包含子串的七种方法

### 1、使用 in 和 not in

`in` 和 `not in` 在 Python 中是很常用的关键字，我们将它们归类为 `成员运算符`。

使用这两个成员运算符，可以很让我们很直观清晰的判断一个对象是否在另一个对象中，示例如下：

```
>>> "llo" in "hello, python"
True
>>>
>>> "lol" in "hello, python"
False
```

### 2、使用 find 方法

使用 字符串 对象的 find 方法，如果有找到子串，就可以返回指定子串在字符串中的出现位置，如果没有找到，就返回 `-1`

```
>>> "hello, python".find("llo") != -1
True
>>> "hello, python".find("lol") != -1
False
>>
```

### 3、使用 index 方法

字符串对象有一个 index 方法，可以返回指定子串在该字符串中第一次出现的索引，如果没有找到会抛出异常，因此使用时需要注意捕获。

```
def is_in(full_str, sub_str):
    try:
        full_str.index(sub_str)
        return True
    except ValueError:
        return False

print(is_in("hello, python", "llo"))  # True
print(is_in("hello, python", "lol"))  # False
```

### 4、使用 count 方法

利用和 index 这种曲线救国的思路，同样我们可以使用 count 的方法来判断。

只要判断结果大于 0 就说明子串存在于字符串中。

```
def is_in(full_str, sub_str):
    return full_str.count(sub_str) > 0

print(is_in("hello, python", "llo"))  # True
print(is_in("hello, python", "lol"))  # False
```

### 5、通过魔法方法

在第一种方法中，我们使用 in 和 not in 判断一个子串是否存在于另一个字符中，实际上当你使用 in 和 not in 时，Python 解释器会先去检查该对象是否有 `__contains__` 魔法方法。

若有就执行它，若没有，Python 就自动会迭代整个序列，只要找到了需要的一项就返回 True 。

示例如下；

```
>>> "hello, python".__contains__("llo")
True
>>>
>>> "hello, python".__contains__("lol")
False
>>>
```

这个用法与使用 in 和 not in 没有区别，但不排除有人会特意写成这样来增加代码的理解难度。

### 6、借助 operator

operator模块是python中内置的操作符函数接口，它定义了一些算术和比较内置操作的函数。operator模块是用c实现的，所以执行速度比 python 代码快。

在 operator 中有一个方法 `contains` 可以很方便地判断子串是否在字符串中。

```
>>> import operator
>>>
>>> operator.contains("hello, python", "llo")
True
>>> operator.contains("hello, python", "lol")
False
>>>
```

### 7、使用正则匹配

说到查找功能，那正则绝对可以说是专业的工具，多复杂的查找规则，都能满足你。

对于判断字符串是否存在于另一个字符串中的这个需求，使用正则简直就是大材小用。

```
import re

def is_in(full_str, sub_str):
    if re.findall(sub_str, full_str):
        return True
    else:
        return False

print(is_in("hello, python", "llo"))  # True
print(is_in("hello, python", "lol"))  # False
```

## 6、海象运算符的三种用法

它的英文原名叫 `Assignment Expressions`，翻译过来也就是 `赋值表达式`，不过现在大家更普遍地称之为海象运算符，就是因为它长得真的太像海象了

### 第一个用法：if/else

可能有朋友是第一次接触这个新特性，所以还是简单的介绍一下这个海象运算符有什么用？

在 Golang 中的条件语句可以直接在 if 中运算变量的获取后直接对这个变量进行判断，可以让你少写一行代码

```
import "fmt"

func main() {
    if age := 20;age > 18 {
        fmt.Println("已经成年了")
    }
}
```

若在 Python 3.8 之前，Python 必须得这样子写

```
age = 20
if age > 18:
    print("已经成年了")
```

但有了海象运算符之后，你可以和 Golang 一样（如果你没学过 Golang，那这里要注意，Golang 中的 `:=` 叫短变量声明，意思是声明并初始化，它和 Python 中的 `:=` 不是一个概念）

```
if (age:= 20) > 18:
    print("已经成年了")
```

### 第二个用法：while

在不使用 海象运算符之前，使用 while 循环来读取文件的时候，你也许会这么写

```
file = open("demo.txt", "r")
while True:
    line = file.readline()
    if not line:
        break
    print(line.strip())
```

但有了海象运算符之后，你可以这样

```
file = open("demo.txt", "r")
while (line := file.readline()):
    print(line.strip())
```

使用它替换以往的无限 while 循环写法更为惊艳

比如，实现一个需要命令行交互输入密码并检验的代码，你也许会这样子写

```
while True:
   p = input("Enter the password: ")
   if p == "youpassword":
      break
```

有了海象运算符之后，这样子写更为舒服

```
while (p := input("Enter the password: ")) != "youpassword":
   continue
```

### 第三个用法：推导式

如下这段代码中，我会使用列表推导式得出所有会员中过于肥胖的人的 bmi 指数

```
members = [
    {"name": "小五", "age": 23, "height": 1.75, "weight": 72},
    {"name": "小李", "age": 17, "height": 1.72, "weight": 63},
    {"name": "小陈", "age": 20, "height": 1.78, "weight": 82},
]

count = 0

def get_bmi(info):
    global count
    count += 1

    print(f"执行了 {count} 次")

    height = info["height"]
    weight = info["weight"]

    return weight / (height**2)

# 查出所有会员中过于肥胖的人的 bmi 指数
fat_bmis = [get_bmi(m) for m in members if get_bmi(m) > 24]

print(fat_bmis)
```

输出如下

```
执行了 1 次
执行了 2 次
执行了 3 次
执行了 4 次
[25.88057063502083]
```

可以看到，会员数只有 3 个，但是 get_bmi 函数却执行了 4 次，原因是在判断时执行了 3 次，而在构造新的列表时又重复执行了一遍。

如果所有会员都是过于肥胖的，那最终将执行 6 次，这种在大量的数据下是比较浪费性能的，因此对于这种结构，我通常会使用传统的for 循环 + if 判断。

```
fat_bmis = []

# 查出所有会员中过于肥胖的人的 bmi 指数
for m in members:
    bmi = get_bmi(m)
    if bmi > 24:
        fat_bmis.append(bmi)
```

在有了海象运算符之后，你就可以不用在这种场景下做出妥协。

```
# 查出所有会员中过于肥胖的人的 bmi 指数
fat_bmis = [bmi for m in members if (bmi := get_bmi(m)) > 24]
```

最终从输出结果可以看出，只执行了 3 次

```
执行了 1 次
执行了 2 次
执行了 3 次
[25.88057063502083]
```