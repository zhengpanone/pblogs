# 描述符

## 1. 为什么要使用描述符？

假想你正在给学校写一个成绩管理系统，并没有太多编码经验的你，可能会这样子写。

```python
class Student:
    def __init__(self, name, math, chinese, english):
        self.name = name
        self.math = math
        self.chinese = chinese
        self.english = english

    def __repr__(self):
        return "<Student: {}, math:{}, chinese: {}, english:{}>".format(
                self.name, self.math, self.chinese, self.english
            )
```

看起来一切都很合理

```python
>>> std1 = Student('小明', 76, 87, 68)
>>> std1
<Student: 小明, math:76, chinese: 87, english:68>
```

但是程序并不像人那么智能，不会自动根据使用场景判断数据的合法性，如果老师在录入成绩的时候，不小心录入了将成绩录成了负数，或者超过100，程序是无法感知的。

聪明的你，马上在代码中加入了判断逻辑。

```python
class Student:
    def __init__(self, name, math, chinese, english):
        self.name = name
        if 0 <= math <= 100:
            self.math = math
        else:
            raise ValueError("Valid value must be in [0, 100]")

        if 0 <= chinese <= 100:
            self.chinese = chinese
        else:
            raise ValueError("Valid value must be in [0, 100]")

        if 0 <= chinese <= 100:
            self.english = english
        else:
            raise ValueError("Valid value must be in [0, 100]")


    def __repr__(self):
        return "<Student: {}, math:{}, chinese: {}, english:{}>".format(
                self.name, self.math, self.chinese, self.english
            )
```

这下程序稍微有点人工智能了，能够自己明辨是非了。

![image1](image/p06_Descriptor.assets/20190425221322-1597300651222.png)

程序是智能了，但在`__init__`里有太多的判断逻辑，很影响代码的可读性。巧的是，你刚好学过 Property 特性，可以很好的应用在这里。于是你将代码修改成如下，代码的可读性瞬间提升了不少

```python
class Student:
    def __init__(self, name, math, chinese, english):
        self.name = name
        self.math = math
        self.chinese = chinese
        self.english = english

    @property
    def math(self):
        return self._math

    @math.setter
    def math(self, value):
        if 0 <= value <= 100:
            self._math = value
        else:
            raise ValueError("Valid value must be in [0, 100]")

    @property
    def chinese(self):
        return self._chinese

    @chinese.setter
    def chinese(self, value):
        if 0 <= value <= 100:
            self._chinese = value
        else:
            raise ValueError("Valid value must be in [0, 100]")

    @property
    def english(self):
        return self._english

    @english.setter
    def english(self, value):
        if 0 <= value <= 100:
            self._english = value
        else:
            raise ValueError("Valid value must be in [0, 100]")

    def __repr__(self):
        return "<Student: {}, math:{}, chinese: {}, english:{}>".format(
                self.name, self.math, self.chinese, self.english
            )
```

程序还是一样的人工智能，非常好。

![image2](image/p06_Descriptor.assets/20190425221322.png)

你以为你写的代码，已经非常优秀，无懈可击了。

没想到，人外有天，你的主管看了你的代码后，深深地叹了口气：类里的三个属性，math、chinese、english，都使用了 Property 对属性的合法性进行了有效控制。功能上，没有问题，但就是太啰嗦了，三个变量的合法性逻辑都是一样的，只要大于0，小于100 就可以，代码重复率太高了，这里三个成绩还好，但假设还有地理、生物、历史、化学等十几门的成绩呢，这代码简直没法忍。去了解一下 Python 的描述符吧。

经过主管的指点，你知道了「描述符」这个东西。怀着一颗敬畏之心，你去搜索了下关于 描述符的用法。

其实也很简单，一个实现了 `描述符协议` 的类就是一个描述符。

什么描述符协议：在类里实现了 `__get__()`、`__set__()`、`__delete__()` 其中至少一个方法。

- `__get__`： 用于访问属性。它返回属性的值，若属性不存在、不合法等都可以抛出对应的异常。
- `__set__`：将在属性分配操作中调用。不会返回任何内容。
- `__delete__`：控制删除操作。不会返回内容。

对描述符有了大概的了解后，你开始重写上面的方法。

如前所述，Score 类是一个描述符，当从 Student 的实例访问 math、chinese、english这三个属性的时候，都会经过 Score 类里的三个特殊的方法。这里的 Score 避免了 使用Property 出现大量的代码无法复用的尴尬。

```python
class Score:
    def __init__(self, default=0):
        self._score = default

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Score must be integer')
        if not 0 <= value <= 100:
            raise ValueError('Valid value must be in [0, 100]')

        self._score = value

    def __get__(self, instance, owner):
        return self._score

    def __delete__(self):
        del self._score

class Student:
    math = Score(0)
    chinese = Score(0)
    english = Score(0)

    def __init__(self, name, math, chinese, english):
        self.name = name
        self.math = math
        self.chinese = chinese
        self.english = english


    def __repr__(self):
        return "<Student: {}, math:{}, chinese: {}, english:{}>".format(
                self.name, self.math, self.chinese, self.english
            )
```

实现的效果和前面的一样，可以对数据的合法性进行有效控制（字段类型、数值区间等）

![image3](image/p06_Descriptor.assets/20190425221233.png)

以上，我举了下具体的实例，从最原始的编码风格到 Property ，最后引出描述符。由浅入深，一步一步带你感受到描述符的优雅之处。

到这里，你需要记住的只有一点，就是描述符给我们带来的编码上的便利，它在实现 `保护属性不受修改`、`属性类型检查` 的基本功能，同时有大大提高代码的复用率。

## 2. 描述符的访问规则

描述符分两种：

- 数据描述符：实现了`__get__` 和 `__set__` 两种方法的描述符
- 非数据描述符：只实现了`__get__` 一种方法的描述符

你一定会问，他们有什么区别呢？网上的讲解，我看过几个，很多都把一个简单的东西讲得复杂了。

其实就一句话，**数据描述器和非数据描述器的区别在于：它们相对于实例的字典的优先级不同**。

如果实例字典中有与描述符同名的属性，如果描述符是数据描述符，优先使用数据描述符，如果是非数据描述符，优先使用字典中的属性。

这边还是以上节的成绩管理的例子来说明，方便你理解。

```python
# 数据描述符
class DataDes:
    def __init__(self, default=0):
        self._score = default

    def __set__(self, instance, value):
        self._score = value

    def __get__(self, instance, owner):
        print("访问数据描述符里的 __get__")
        return self._score

# 非数据描述符
class NoDataDes:
    def __init__(self, default=0):
        self._score = default

    def __get__(self, instance, owner):
        print("访问非数据描述符里的 __get__")
        return self._score


class Student:
    math = DataDes(0)
    chinese = NoDataDes(0)

    def __init__(self, name, math, chinese):
        self.name = name
        self.math = math
        self.chinese = chinese

    def __getattribute__(self, item):
        print("调用 __getattribute__")
        return super(Student, self).__getattribute__(item)

    def __repr__(self):
        return "<Student: {}, math:{}, chinese: {},>".format(
                self.name, self.math, self.chinese)
```

需要注意的是，math 是数据描述符，而 `chinese` 是非数据描述符。从下面的验证中，可以看出，当实例属性和数据描述符同名时，会优先访问数据描述符（如下面的math），而当实例属性和非数据描述符同名时，会优先访问实例属性（`__getattribute__`）

```python
>>> std = Student('xm', 88, 99)
>>>
>>> std.math
调用 __getattribute__
访问数据描述符里的 __get__
88
>>> std.chinese
调用 __getattribute__
99
```

讲完了数据描述符和非数据描述符，我们还需要了解的对象属性的查找规律。

当我们对一个实例属性进行访问时，Python 会按 `obj.__dict__` → `type(obj).__dict__` → `type(obj)的父类.__dict__` 顺序进行查找，如果查找到目标属性并发现是一个描述符，Python 会调用描述符协议来改变默认的控制行为。

## 3. 基于描述符如何实现property

经过上面的讲解，我们已经知道如何定义描述符，且明白了描述符是如何工作的。

正常人所见过的描述符的用法就是上面提到的那些，我想说的是那只是描述符协议最常见的应用之一，或许你还不知道，其实有很多 Python 的特性的底层实现机制都是基于 `描述符协议` 的，比如我们熟悉的`@property` 、`@classmethod` 、`@staticmethod` 和 `super` 等。

先来说说 `property` 吧。

有了前面的基础，我们知道了 property 的基本用法。这里我直接切入主题，从第一篇的例子里精简了一下。

```python
class Student:
    def __init__(self, name):
        self.name = name

    @property
    def math(self):
        return self._math

    @math.setter
    def math(self, value):
        if 0 <= value <= 100:
            self._math = value
        else:
            raise ValueError("Valid value must be in [0, 100]")
```

不防再简单回顾一下它的用法，通过property装饰的函数，如例子中的 math 会变成 Student 实例的属性。而对 math 属性赋值会进入 使用 `math.setter` 装饰函数的逻辑代码块。

为什么说 property 底层是基于描述符协议的呢？通过 `PyCharm` 点击进入 property 的源码，很可惜，只是一份类似文档一样的伪源码，并没有其具体的实现逻辑。

不过，从这份伪源码的魔法函数结构组成，可以大体知道其实现逻辑。

这里我自己通过模仿其函数结构，结合「描述符协议」来自己实现类 `property` 特性。

代码如下：

```python
class TestProperty(object):

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        print("in __get__")
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError
        return self.fget(obj)

    def __set__(self, obj, value):
        print("in __set__")
        if self.fset is None:
            raise AttributeError
        self.fset(obj, value)

    def __delete__(self, obj):
        print("in __delete__")
        if self.fdel is None:
            raise AttributeError
        self.fdel(obj)


    def getter(self, fget):
        print("in getter")
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        print("in setter")
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        print("in deleter")
        return type(self)(self.fget, self.fset, fdel, self.__doc__)
```

然后 Student 类，我们也相应改成如下

```python
class Student:
    def __init__(self, name):
        self.name = name

    # 其实只有这里改变
    @TestProperty
    def math(self):
        return self._math

    @math.setter
    def math(self, value):
        if 0 <= value <= 100:
            self._math = value
        else:
            raise ValueError("Valid value must be in [0, 100]")
```

为了尽量让你少产生一点疑惑，我这里做两点说明：

1. 使用`TestProperty`装饰后，`math` 不再是一个函数，而是`TestProperty` 类的一个实例。所以第二个math函数可以使用 `math.setter` 来装饰，本质是调用`TestProperty.setter` 来产生一个新的 `TestProperty` 实例赋值给第二个`math`。
2. 第一个 `math` 和第二个 `math` 是两个不同 `TestProperty` 实例。但他们都属于同一个描述符类（TestProperty），当对 math 对于赋值时，就会进入 `TestProperty.__set__`，当对math 进行取值里，就会进入 `TestProperty.__get__`。仔细一看，其实最终访问的还是Student实例的 `_math` 属性。

说了这么多，还是运行一下，更加直观一点。

```bash
# 运行后，会直接打印这一行，这是在实例化 TestProperty 并赋值给第二个math
in setter
>>>
>>> s1.math = 90
in __set__
>>> s1.math
in __get__
90
```

对于以上理解 `property` 的运行原理有困难的同学，请务必参照我上面写的两点说明。如有其他疑问，可以加微信与我进行探讨。

## 4. 基于描述符如何实现 staticmethod

说完了 `property` ，这里再来讲讲 `@classmethod` 和 `@staticmethod` 的实现原理。

我这里定义了一个类，用了两种方式来实现静态方法。

```python
class Test:
    @staticmethod
    def myfunc():
        print("hello")

# 上下两种写法等价

class Test:
    def myfunc():
        print("hello")
    # 重点：这就是描述符的体现
    myfunc = staticmethod(myfunc)
```

这两种写法是等价的，就好像在 `property` 一样，其实以下两种写法也是等价的。

```python
@TestProperty
def math(self):
    return self._math

math = TestProperty(fget=math)
```

话题还是转回到 `staticmethod` 这边来吧。

由上面的注释，可以看出 `staticmethod` 其实就相当于一个描述符类，而`myfunc` 在此刻变成了一个描述符。关于 `staticmethod` 的实现，你可以参照下面这段我自己写的代码，加以理解。

![image4](image/p06_Descriptor.assets/20190519001930.png)

调用这个方法可以知道，每调用一次，它都会经过描述符类的 `__get__` 。

```bash
>>> Test.myfunc()
in staticmethod __get__
hello
>>> Test().myfunc()
in staticmethod __get__
hello
```

## 5. 基于描述符如何实现classmethod

同样的 `classmethod` 也是一样。

```python
class classmethod(object):
    def __init__(self, f):
        self.f = f

    def __get__(self, instance, owner=None):
        print("in classmethod __get__")

        def newfunc(*args):
            return self.f(owner, *args)
        return newfunc

class Test:
    def myfunc(cls):
        print("hello")

    # 重点：这就是描述符的体现
    myfunc = classmethod(myfunc)
```

验证结果如下

```python
>>> Test.myfunc()
in classmethod __get__
hello
>>> Test().myfunc()
in classmethod __get__
hello
```

讲完了 `property`、`staticmethod`和`classmethod` 与 描述符的关系。我想你应该对描述符在 Python 中的应用有了更深的理解。对于 super 的实现原理，就交由你来自己完成。

## 6. 所有实例共享描述符

通过以上内容的学习，你是不是觉得自己已经对描述符足够了解了呢？

可在这里，我想说以上的描述符代码都有问题。

问题在哪里呢？请看下面这个例子。

```python
class Score:
    def __init__(self, default=0):
        self._value = default

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if 0 <= value <= 100:
            self._value = value
        else:
            raise ValueError


class Student:
    math = Score(0)
    chinese = Score(0)
    english = Score(0)

    def __repr__(self):
        return "<Student math:{}, chinese:{}, english:{}>".format(self.math, self.chinese, self.english)
```

Student 里没有像前面那样写了构造函数，但是关键不在这儿，没写只是因为没必要写。

然后来看一下会出现什么样的问题呢

```bash
>>> std1 = Student()
>>> std1
<Student math:0, chinese:0, english:0>
>>> std1.math = 85
>>> std1
<Student math:85, chinese:0, english:0>
>>> std2 = Student()
>>> std2 # std2 居然共享了std1 的属性值
<Student math:85, chinese:0, english:0>
>>> std2.math = 100
>>> std1 # std2 也会改变std1 的属性值
<Student math:100, chinese:0, english:0>
```

从结果上来看，std2 居然共享了 std1 的属性值，只要其中一个实例的变量发生改变，另一个实例的变量也会跟着改变。

探其根因，是由于此时 math，chinese，english 三个全部是类变量，导致 std2 和 std1 在访问 math，chinese，english 这三个变量时，其实都是访问类变量。

问题是不是来了？小明和小强的分数怎么可能是绑定的呢？这很明显与实际业务不符。

使用描述符给我们制造了便利，却无形中给我们带来了麻烦，难道这也是描述符的特性吗？

描述符是个很好用的特性，会出现这个问题，是由于我们之前写的描述符代码都是错误的。

描述符的机制，在我看来，只是抢占了访问顺序，而具体的逻辑却要因地制宜，视情况而定。

如果要把 math，chinese，english 这三个变量变成实例之间相互隔离的属性，应该这么写。

```python
class Score:
    def __init__(self, subject):
        self.name = subject

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if 0 <= value <= 100:
            instance.__dict__[self.name] = value
        else:
            raise ValueError


class Student:
    math = Score("math")
    chinese = Score("chinese")
    english = Score("english")

    def __init__(self, math, chinese, english):
        self.math = math
        self.chinese = chinese
        self.english = english

    def __repr__(self):
        return "<Student math:{}, chinese:{}, english:{}>".format(self.math, self.chinese, self.english)
```

引导程序逻辑进入描述符之后，不管你是获取属性，还是设置属性，都是直接作用于 instance 的。

![image5](image/p06_Descriptor.assets/20200812085823-1597300628410.png)

这段代码，你可以仔细和前面的对比一下。

不难看出：

- 之前的错误代码，更像是把描述符当做了存储节点。
- 之后的正确代码，则是把描述符直接当做代理，本身不存储值。

![image5](image/p06_Descriptor.assets/20200812085823.png)