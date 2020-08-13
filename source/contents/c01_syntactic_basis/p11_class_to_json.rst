==============================
11. 类对象的JSON序列化处理
==============================

Python 内置的json模块提供Python对象到JSON格式的转换


**json.dumps()**    将Python中的对象转换为JSON中的字符串对象
**json.loads()**       将JSON的字符串对象转换为Python中的对象


dict、list、float、bool  to json
=========================================

::

 p_obj1 = {'name':'Tom','age':30}
 j_obj1 = json.dumps(p_obj1)

class to json
====================

如果是类对象，不可以直接转换为Json对象，运行是会报错TypeError。错误原因是类对象不是一个可序列化为JSON的对象，查看dumps()方法

::

 help(json.dumps)

 dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, encoding='utf-8', default=None, sort_keys=False, **kw)

这些可选参数就是让我们来定制JSON序列化。前面的代码之所以无法把Man类实例序列化为JSON，是因为默认情况下，dumps()方法不知道如何将Man实例变为一个JSON的{}对象。

可选参数default就是把任意一个对象变成一个可序列化为JSON的对象，需要为类专门写一个转换函数，再把函数传入即可


::

 import json
 class Man(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

 def obj_2_json(obj):
    return {"name":obj.name,"age":obj.age}

 m = Man('tom',29)
 print(json.dumps(m,default=obj_2_json))
    


https://blog.csdn.net/jerry_1126/article/details/76409042