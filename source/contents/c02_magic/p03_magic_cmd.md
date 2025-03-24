# [魔法命令行](http://magic.iswbm.com/zh/latest/c02/c02_12.html)

## 最快查看包搜索路径的方式

```python
python -c "print('\n'.join(__import__('sys').path))"
```

```
python3 -m site
```

## 使用 json.tool 来格式化 JSON

```
python -m json.tool demo.json
```

## 命令行式执行 Python 代码

```
$ python -c "import hashlib;print(hashlib.md5('hello').hexdigest())"
5d41402abc4b2a76b9719d911017c592
```

## 用调试模式执行脚本

当你使用 pdb 进行脚本的调试时，你可能会先在目标代码处输入 `import pdb;pdb.set_trace()` 来设置断点。

除此之外，还有一种方法，就是使用 `-m pdb`

```
$ python -m pdb demo.py
> /Users/MING/demo.py(1)<module>()
-> import sys
(Pdb)
```

## 如何快速搭建 FTP 服务器

SimpleHTTPServer是Python 2自带的一个模块，是Python的Web服务器。它在Python 3已经合并到http.server模块中。具体例子如下，如不指定端口，则默认是8000端口。

```
# python2
python -m SimpleHTTPServer 8888

# python3
python3 -m http.server 8888
```

SimpleHTTPServer有一个特性，如果待共享的目录下有index.html，那么index.html文件会被视为默认主页；如果不存在index.html文件，那么就会显示整个目录列表。

## 快速构建 HTML 帮助文档

```
$ python -m pydoc -p 5200
pydoc server ready at http://localhost:5200/
```

## 优雅的装包方法

```
# 在 python2 中安装
$ python -m pip install requests

# 在 python3 中安装
$ python3 -m pip install requests

# 在 python3.8 中安装
$ python3.8 -m pip install requests

# 在 python3.9 中安装
$ python3.9 -m pip install requests
```

## 让脚本报错后立即进入调试模式

```
python -i demo.py
```

## 极简模式执行 Python Shell

```
python -q
```

## 启动 Python Shell 前自动执行某脚本

1. 在任意你喜欢的目录下，新建 一个Python 脚本，名字也随意，比如我叫 `startup.py`

2. 设置一个环境变量 PYTHONSTARTUP，指向你的脚本路径

   ```
   export PYTHONSTARTUP=/Users/MING/startup.py
   ```

   这种方法只适用于 Python Shell ，只不适合 Python 执行脚本的方法

##  把模块当做脚本来执行 7 种方法及原理

### 1. 用法举例

前面的文章里其实分享过不少类似的用法。比如：

1、 快速搭建一个 HTTP 服务

```
# python2
$ python -m SimpleHTTPServer 8888

# python3
$ python3 -m http.server 8888
```

2、快速构建 HTML 帮助文档

```
$ python -m pydoc -p 5200
```

3、快速进入 pdb 调试模式

```
$ python -m pdb demo.py
```

4、最优雅且正确的包安装方法

```
$ python3 -m pip install requests
```

5、快速美化 JSON 字符串

```
$ echo '{"name": "MING"}' | python -m json.tool
```

6、快速打印包的搜索路径

```
$ python -m site
```

7、用于快速计算程序执行时长

```
$ python3 -m timeit '"-".join(map(str, range(100)))'
```

### 2. 原理剖析

上面的诸多命令，都有一个特点，在命令中都含有 `-m` 参数选项，而参数的值，SimpleHTTPServer， http.server， pydoc，pdb，pip， json.tool，site ，timeit这些都是模块或者包。

那这是如何实现的呢？

最好的学习方式，莫过于模仿，直接以 pip 和 json 模块为学习对象，看看目录结构和代码都有什么特点。

先看一下 `pip` 的源码目录，发现在其下有一个 `__main__.py` 的文件，难道这是 `-m` 的入口？

再看一下 `json.tool` 的源码文件，json 库下面却没有 `__main__.py` 的文件。

这就很奇怪了。

不对，再回过头看，我们调用的不是 json 库，而是 json 库下的 tool 模块。

查看 tool 模块的源代码，有一个名为 main 的函数

但它这不是关键，main 函数是在模块中直接被调用的。

只有当 `__name__` 为 `__main___` 时，main 函数才会被调用

```
if __name__ == '__main__':
    main()
```

当模块被导入时，`__name__` 的值为模块名，

而当模块被直接执行，`__name__` 的值就变成了 `__main__`。

想要使用 `-m` 的方式执行模块，有两种方式：

- 第一种：以 `-m <package>` 的方式执行，只要在 package 下写一个 `__main__.py` 的文件即可。
- 第二种：以 `-m <package.module>` 的方式执行，只要在 module 的代码中，定义一个 main 函数，然后在最外层写入下面这段固定的代码

```
if __name__ == '__main__':
    main()
```

上面我将 `-m` 的使用情况分为两种，但是实际上，只有一种，对于第一种，你完全可以将 `-m <package>` 理解为 `-m <package.__main__>` 的简写形式。

