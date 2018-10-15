========================
5.1 装饰器
========================

1. 用类写装饰器
   实现缓存装饰器

::

 def cache(func):
    data = {}
    def wrapper(*args, **kwargs):
        key = f'{func.__name__}-{str(args)}-{str(kwargs)}'
        if key in data:
            result = data.get(key)
            print('cached')
        else:
            result = func(*args, **kwargs)
            data[key] = result
            print('calculated')
        return result
    return wrapper

查看缓存效果

::

 @cache
 def rectangle_area(length, width):
    return length*width

 rectangle_area(2, 3)
 # calculated
 # 6
 rectangle_area(2, 3)
 # cached
 # 6

装饰器的@cache 是语法糖,相当于func = cache(func), 如果这里的cache不是一个函数,而是一个类？
定义一个类 class Cache, 那么调用func = Cache(func) 会得到一个对象, 这时返回的func 其实是Cache的对象. 定义__call__方法可以将类的实例变成可调用对象, 可以像调用函数一样调用对象. 然后在__call__ 方法里调用原本的func函数就能实现装饰器. 所以Cache类也能当作装饰器使用, 并且能以@Cache 的形式使用.

把cache函数改写为Cache类:

::

 class Cache:
    def __init__(self, func):
        self.func = func
        self.data = {}

    def __call__(self, *args, **kwargs):
        func = self.func
        data = self.data
        key = f'{func.__name__}-{str(args)}-{str(kwargs)}'
        if key in data:
            result = data.get(key)
            print('cached')
        else:
            result = func(*args, **kwargs)
            data[key] = result
            print('calculated')
        return result

查看缓存效果

::

 @Cache
 def rectangle_area(length, width):
    return length * width

 rectangle_area(2, 3)
 # calculated
 # 6
 rectangle_area(2, 3)
 # calculated
 # 6

2. 装饰类的方法
   装饰器不止能装饰函数, 也常用来装饰类的方法, 

函数写的装饰器如何装饰类的方法

::

 class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width