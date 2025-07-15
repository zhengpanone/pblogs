# 装饰器使用

## 1、日志打印器

- 在函数执行前，先打印一行日志告知一下主人，我要执行函数了。

- 在函数执行完，也不能拍拍屁股就走人了，咱可是有礼貌的代码，再打印一行日志告知下主人，我执行完啦。

```python
# 这是装饰器函数，参数 func 是被装饰的函数
def logger(func):
    def wrapper(*args, **kw):
        print('主人，我准备开始执行：{} 函数了:'.format(func.__name__))

        # 真正执行的是这行。
        func(*args, **kw)

        print('主人，我执行完啦。')
    return wrapper
```

假如，我的业务函数是，计算两个数之和。写好后，直接给它带上帽子。

```python
@logger
def add(x, y):
    print('{} + {} = {}'.format(x, y, x+y))
```

然后执行一下 add 函数。

```python
add(200, 50)
```

来看看输出了什么？

```text
主人，我准备开始执行：add 函数了:
200 + 50 = 250
主人，我执行完啦。
```

## 2、时间计时器

再来看看 **时间计时器** 实现功能：顾名思义，就是计算一个函数的执行时长。

```python
# 这是装饰函数
def timer(func):
    def wrapper(*args, **kw):
        t1=time.time()
        # 这是函数真正执行的地方
        func(*args, **kw)
        t2=time.time()

        # 计算下时长
        cost_time = t2-t1
        print("花费时间：{}秒".format(cost_time))
    return wrapper
```

假如，我们的函数是要睡眠10秒。这样也能更好的看出这个计算时长到底靠不靠谱。

```python
import time

@timer
def want_sleep(sleep_time):
    time.sleep(sleep_time)

want_sleep(10)
```

来看看输出，如预期一样，输出10秒。

```text
花费时间：10.0073800086975098秒
```

## 3、带参数的函数装饰器

比如我们要实现一个可以定时发送邮件的任务（一分钟发送一封），定时进行时间同步的任务（一天同步一次），就可以自己实现一个 periodic_task （定时任务）的装饰器，这个装饰器可以接收一个时间间隔的参数，间隔多长时间执行一次任务。

可以这样像下面这样写，由于这个功能代码比较复杂，不利于学习，这里就不贴了。

```python
@periodic_task(spacing=60)
def send_mail():
     pass

@periodic_task(spacing=86400)
def ntp()
    pass
```

那我们来自己创造一个伪场景，可以在装饰器里传入一个参数，指明国籍，并在函数执行前，用自己国家的母语打一个招呼。

```python
# 小明，中国人
@say_hello("china")
def xiaoming():
    pass

# jack，美国人
@say_hello("america")
def jack():
    pass
```

那我们如果实现这个装饰器，让其可以实现 `传参` 呢？

会比较复杂，需要两层嵌套。

```python
def say_hello(contry):
    def wrapper(func):
        def deco(*args, **kwargs):
            if contry == "china":
                print("你好!")
            elif contry == "america":
                print('hello.')
            else:
                return

            # 真正执行函数的地方
            func(*args, **kwargs)
        return deco
    return wrapper
```

来执行一下

```python
xiaoming()
print("------------")
jack()
```

看看输出结果。

```bash
你好!
------------
hello.
```

## 4、不带参数的类装饰器

以上都是基于函数实现的装饰器，在阅读别人代码时，还可以时常发现还有基于类实现的装饰器。

基于类装饰器的实现，必须实现 `__call__` 和 `__init__`两个内置函数。 `__init__` ：接收被装饰函数 `__call__` ：实现装饰逻辑。

还是以日志打印这个简单的例子为例

```python
class logger(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("[INFO]: the function {func}() is running..."\
            .format(func=self.func.__name__))
        return self.func(*args, **kwargs)

@logger
def say(something):
    print("say {}!".format(something))

say("hello")
```

执行一下，看看输出

```bash
[INFO]: the function say() is running...
say hello!
```

## 5、带参数的类装饰器

上面不带参数的例子，你发现没有，只能打印`INFO`级别的日志，正常情况下，我们还需要打印`DEBUG` `WARNING`等级别的日志。 这就需要给类装饰器传入参数，给这个函数指定级别了。

带参数和不带参数的类装饰器有很大的不同。

`__init__` ：不再接收被装饰函数，而是接收传入参数。 `__call__` ：接收被装饰函数，实现装饰逻辑。

```python
class logger(object):
    def __init__(self, level='INFO'):
        self.level = level

    def __call__(self, func): # 接受函数
        def wrapper(*args, **kwargs):
            print("[{level}]: the function {func}() is running..."\
                .format(level=self.level, func=func.__name__))
            func(*args, **kwargs)
        return wrapper  #返回函数

@logger(level='WARNING')
def say(something):
    print("say {}!".format(something))

say("hello")
```

我们指定`WARNING`级别，运行一下，来看看输出。

```bash
[WARNING]: the function say() is running...
say hello!
```

## 6、使用偏函数与类实现装饰器

绝大多数装饰器都是基于函数和闭包实现的，但这并非制造装饰器的唯一方式。

事实上，Python 对某个对象是否能通过装饰器（ `@decorator`）形式使用只有一个要求：**decorator 必须是一个“可被调用（callable）的对象**。

对于这个 callable 对象，我们最熟悉的就是函数了。

除函数之外，类也可以是 callable 对象，只要实现了`__call__` 函数（上面几个例子已经接触过了）。

还有容易被人忽略的偏函数其实也是 callable 对象。

接下来就来说说，如何使用 类和偏函数结合实现一个与众不同的装饰器。

如下所示，`DelayFunc` 是一个实现了 `__call__` 的类，delay 返回一个偏函数，在这里 delay 就可以做为一个装饰器。（以下代码摘自 Python工匠：使用装饰器的小技巧）

```python
import time
import functools

class DelayFunc:
    def __init__(self,  duration, func):
        self.duration = duration
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'Wait for {self.duration} seconds...')
        time.sleep(self.duration)
        return self.func(*args, **kwargs)

    def eager_call(self, *args, **kwargs):
        print('Call without delay')
        return self.func(*args, **kwargs)

def delay(duration):
    """
    装饰器：推迟某个函数的执行。
    同时提供 .eager_call 方法立即执行
    """
    # 此处为了避免定义额外函数，
    # 直接使用 functools.partial 帮助构造 DelayFunc 实例
    return functools.partial(DelayFunc, duration)
```

我们的业务函数很简单，就是相加

```python
@delay(duration=2)
def add(a, b):
    return a+b
```

来看一下执行过程

```python
>>> add    # 可见 add 变成了 Delay 的实例
<__main__.DelayFunc object at 0x107bd0be0>
>>>
>>> add(3,5)  # 直接调用实例，进入 __call__
Wait for 2 seconds...
8
>>>
>>> add.func # 实现实例方法
<function add at 0x107bef1e0>
```

## 7、如何写能装饰类的装饰器？

用 Python 写单例模式的时候，常用的有三种写法。其中一种，是用装饰器来实现的。

以下便是我自己写的装饰器版的单例写法。

```python
instances = {}

def singleton(cls):
    def get_instance(*args, **kw):
        cls_name = cls.__name__
        print('===== 1 ====')
        if not cls_name in instances:
            print('===== 2 ====')
            instance = cls(*args, **kw)
            instances[cls_name] = instance
        return instances[cls_name]
    return get_instance

@singleton
class User:
    _instance = None

    def __init__(self, name):
        print('===== 3 ====')
        self.name = name
```

可以看到我们用singleton 这个装饰函数来装饰 User 这个类。装饰器用在类上，并不是很常见，但只要熟悉装饰器的实现过程，就不难以实现对类的装饰。在上面这个例子中，装饰器就只是实现对类实例的生成的控制而已。![image1](./image/p05/20190512113917.png)

## 8、wraps 装饰器有啥用

在 `functools` 标准库中有提供一个 wraps 装饰器，你应该也经常见过，那他有啥用呢？

先来看一个例子

```python
def wrapper(func):
    def inner_function():
        pass
    return inner_function

@wrapper
def wrapped():
    pass

print(wrapped.__name__)
#inner_function
```

为什么会这样子？不是应该返回 `func` 吗？

这也不难理解，因为上边执行`func` 和下边 `decorator(func)` 是等价的，所以上面 `func.__name__` 是等价于下面`decorator(func).__name__` 的，那当然名字是 `inner_function`

```python
def wrapper(func):
    def inner_function():
        pass
    return inner_function

def wrapped():
    pass

print(wrapper(wrapped).__name__)
#inner_function
```

那如何避免这种情况的产生？方法是使用 `functools.wraps` 装饰器，它的作用就是将 **被修饰的函数(wrapped)** 的一些属性值赋值给 **修饰器函数(wrapper)** ，最终让属性的显示更符合我们的直觉。

```python
from functools import wraps

def wrapper(func):
    @wraps(func)
    def inner_function():
        pass
    return inner_function

@wrapper
def wrapped():
    pass

print(wrapped.__name__)
# wrapped
```

准确点说，wraps 其实是一个偏函数对象（partial），源码如下

```python
def wraps(wrapped,
          assigned = WRAPPER_ASSIGNMENTS,
          updated = WRAPPER_UPDATES):
    return partial(update_wrapper, wrapped=wrapped,
                   assigned=assigned, updated=updated)
```

可以看到wraps其实就是调用了一个函数`update_wrapper`，知道原理后，我们改写上面的代码，在不使用 wraps的情况下，也可以让 `wrapped.__name__` 打印出 wrapped，代码如下：

```python
from functools import update_wrapper

WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__qualname__', '__doc__',
                       '__annotations__')

def wrapper(func):
    def inner_function():
        pass

    update_wrapper(inner_function, func, assigned=WRAPPER_ASSIGNMENTS)
    return inner_function

@wrapper
def wrapped():
    pass

print(wrapped.__name__)
```