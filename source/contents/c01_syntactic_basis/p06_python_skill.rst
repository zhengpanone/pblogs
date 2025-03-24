====================================
Python编程技巧
====================================

字符串操作
-----------------

format_map()函数
>>>>>>>>>>>>>>>>>>>>>>>

多个占位符格式化字符串

.. code-block:: python
   :linenos:

   s6 = {'name': '张三', 'age': 18}
   "my name is {name}, my age is {age}".format_map(s6)

partition()函数
>>>>>>>>>>>>>>>>>>>>>>>>

搜索指定字符串,并将该字符串拆分为包含三个元素的元组

.. code-block:: python 
   :linenos:

   s1 = "'my name is zhang san'"
   s1.partition("is")

rindex()函数
>>>>>>>>>>>>>>>>>>>>

查找指定值的最后一次出现的索引

.. code-block:: python
   :linenos:

   s2 = "1_a_b_a_1_a_1_c"
   s2.rindex('1')
   s2.rindex('a')

swapcase()函数
>>>>>>>>>>>>>>>>>>>>>>

返回一个字符串,其中所有大写字母均为小写字母,反之亦然

.. code-block:: python
   :linenos:

   s3 = "mY name is zhang san"
   s3.swapcase()


center()函数
>>>>>>>>>>>>>>>>>>>>>

使用指定字符(默认空格)作为填充字符使字符串居中对齐

.. code-block:: python
   :linenos:

   s4 = "ABCD"
   s4.center(10,"*")

capitalize()函数
>>>>>>>>>>>>>>>>>>>>>>>>>

返回一个字符串,其中第一个字符串为大写

.. code-block:: python
   :linenos:

   s3 = "mY name is zhang san"
   s3.capitalize()


Lambda
-----------------

.. code-block:: python 
   :linenos:

   square = lambda x : x *x
   square(3)
   # 9

lambda x:可以理解为，python 的lambda函数，输入叫x,冒号之后的任何内容是对输入的操作，它会自动返回结果，可以简化为一行代码：

.. code-block:: python 
   :linenos:

   x = [1,2,3,4,5]
   print(list(map(lambda num*num , x)))

高阶函数
-----------------

高阶函数可以将函数作为参数并返回函数

高阶函数例子

.. code-block:: python 
   :linenos:

   def summation(nums):
      return sum(nums)

   def action(func,numbers):
      return func(numbers)

   print(action(summation,[1,2,3]))


.. code-block:: python 
   :linenos:

   def rtnBrandon():
      return "brandon"

   def rtnJohn():
      return "John"

   def rtnPerson():
      age = int(input("What's your age?"))
      if age == 21:
         return rtnBrandon()
      else:
         return rtnJohn()


Python中的所有函数都具有以下一个或多个特征：
在运行时创建
在数据结构中分配变量或元素
作为函数的参数传递
作为函数的结果返回
Python中的所有函数都可以用作高阶函数。

Partial application
------------------------------

Partial application(闭包)

创建一个函数，它接受2个参数，一个基数和一个指数，并返回指数幂的基数，如下所示：

.. code-block:: python 
   :linenos:

   def power(base,exponent):
      return  base**exponent

.. code-block:: python 
   :linenos:

   from functools import partial
   square = partial(power,exponent=2)
   print(squaer(2))
   # 4

使用一个循环来生成一个幂函数，该函数实现从立方体一直到1000的幂。

.. code-block:: python 
   :linenos:

   from functools import partial
   powers = []
   for x in range(2,1001):
      powers.append(partial(power,exponent=x))

   print(powers[0],[3])
   # 9

列表推导式
-------------------

.. code-block:: python 
   :linenos:

   [function for item in iterable]

   print([x*x for x in range(5)])

   all_less_than_zero = list(filter(lambda num :num <0,x))

   all_less_than_zero = [num for num in x if num < 0]

   all_less_than_zero = list(map(lambda num:num*num, list(filter(lambda num:num<0,x ))))

列表推导仅适用于列表。map,filter适合任何可迭代的对象


三元表达式
====================================

>>> print("Hello" if True else "World")

打印JSON
====================================

.. code-block:: python 
   :linenos:

   import json
   print(json.dumps(data,indent=2))

同时迭代两个列表
====================================

.. code-block:: python
   :linenos:

   nfc = ["Packers", "49ers"]
   afc = ["Ravens", "Patriots"]
   for teama, teamb in zip(nfc, afc):
      print teama + " vs. " + teamb



原理
>>>>>>>>>>>>>

Python3中的zip函数可以把两个或两个以上的迭代器封装成生成器，这种zip生成器会从每个迭代器中获取该迭代器的下一个值,然后把这些值组装成元组。这样zip函数就实现了平行地遍历多个迭代器

注意
>>>>>>>>>>>>>

如果输入的迭代器长度不同，那么，只要有一个迭代器遍历完，zip就不再产生元组了，zip会提前终止，这可能导致意外的结果，不可不察。如果不能确定zip所封装的列表是否等长，可以改用 **itertools** 内置模块中的zip_longest 函数，这个函数不在乎它们的长度是否相等。

在Python2中，zip不是生成器，它平行地遍历这些迭代器，组装元组，并把这些元组所构成的列表一次性完整地返回，这可能会占用大量内存并导致程序崩溃，如果在Python2中要遍历数据量大的迭代器，推荐使用 **itertools** 内置模块中的 izip 函数。


带索引的列表迭代
====================================

.. code-block:: python 
   :linenos:

   teams = ["Packers", "49ers", "Ravens", "Patriots"]
   for index,team in enumerate(teams):
      print(index,team)


初始化列表的值
====================================

.. code-block:: python 
   :linenos:
 
   items = [0]*3
   print(items)
   # [0,0,0]


列表转字符串
====================================

.. code-block:: python 
   :linenos:

   teams = ["Packers", "49ers", "Ravens", "Patriots"]
   print (", ".join(teams))

字典中获取元素
====================================

.. code-block:: python 
   :linenos:

   data = { user : 1,  name :  Max ,  three : 4}
   try:
      is_admin = data[ admin ]
   except KeyError:
      is_admin = False

替换为

.. code-block:: python 
   :linenos:

   is_admin = data.get(admin,False)


获取列表的子集
====================================

.. code-block:: python 
   :linenos:

   x = [1,2,3,4,5,6]
   #前3个
   print x[:3]
   # [1,2,3]
   #中间4个
   print x[1:5]
   # [2,3,4,5]
   #最后3个
   print x[3:]
   # [4,5,6]
   #奇数项
   print x[::2]
   # [1,3,5]
   #偶数项
   print x[1::2]
   # [2,4,6]
 

赋值
====================================


交换赋值
>>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: python 
   :linenos:

   #不推荐
   temp = a
   a = b
   b = a

   #推荐
   a, b = b, a  # 先生成一个元组对象(tuple),然后unpack

多变量赋值
>>>>>>>>>>>>>>>>>>>>>>

>>> a, b, c, d = 0, 1, 2, 3, 4

元组赋值
>>>>>>>>>>>>>>>>>>>>>>>>>>

>>> a,b,c = 1,2,3

同步赋值
>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: python 
   :linenos:

   a,b = 1,2
   a,b = a+b,a    # 同时运行，运算时都利原始值（旧值）

   print("a的值为"+str(a))    #   3
   print("b的值为"+str(b))    #   1

自操做简化
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: python 
   :linenos:

   a+=1 # 自加1
   a-=1 # 自减1
   a*=2 # 自乘2
   a/=2 # 自除2
   a**=2   # 自己的2次方


判断
----------------

使用操作符in
>>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: python
 
   ## 不推荐
   if fruit == 'apple' or fruit == 'orange' or fruit == 'berry':
      # 多次判断
   ## 推荐
   if fruit in ['apple','orange','berry']:
      # 使用in更加简洁


1. 字典键值判断
>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: python

   # 不推荐
   if my_dict.has_key(key):
      # ...do something

   # 推荐
   if key in my_dict:
      # ...do something



1.3 链式
====================================

1. 链式调用
>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: python

   s = "Python $$ is simple, $$readable **and powerful!**"
   s = s.replace('$','').replace('*','')


2. 链式比较
>>>>>>>>>>>>>>>>>>>>>>>>>>>>

::
 
 >>>False == False == True
 False

 >>> 18 < age < 60

 >>> False == False and False == True


1.5 字典键值列表
====================================

.. code-block:: python

   # 不推荐
   for key in my_dict.keys():
      # my_dict[key]...

   for key in my_dict:
      # my_dict[key]...

   # 当循环中需要更改key值的情况下，我们需要使用 my_dict.keys()
   # 生成静态的键值列表。



1.7 字典get和setdefault 方法
====================================

.. code-block:: python 
 
   # 不推荐
   navs = {}
   for(portfolio, equity, position) in data:
      if portfolio not in navs:
         navas[position] = 0
      navas[portfolio] += position * prices[equity]

   # 推荐
   navs = {}
   for (portfolio, equity, position) in data:
      # 使用get方法
      navs[portfolio] = navs.get(portfolio,0) + position* prices[equity]
      # 或者使用setdefault 方法
      navs.setdefault(portfolio,0)
      navs[portfolio] += position * prices[equity]

1.8 列表推导-嵌套
====================================

.. code-block:: python

   # 不推荐
   for sub_list in nested_list:
      if list_condition(sub_list):
         for item in sub_list:
               if item_condition(item):
                  # do something...
   # 推荐

   gen = (item for sl in nested_list if list_condition(s1) for item in sl if item_contition(item))
   for item in gen:
      # do something

1.9 循环嵌套
====================================

.. code-block:: python
 
   # 不推荐
   for x in x_list:
      for y in y_list:
         for z in z_list:
               # do something 

   # 推荐
   from itertools import product
   for x,y,z in product(x_list,y_list,z_list):
      # do something

2.0 尽量用生成器替代列表
====================================

.. code-block:: python
 
   # 不推荐
   def my_range(n):
      i = 0
      result = []
      while i < n:
         result.append(fn(i))
         i += 1
      return result # 返回列表

   # 推荐
   def my_range(n):
      i = 0
      result = []
      while i < n:
         yield fn(i) # 生成器替代列表
         i += 1
   # 尽量使用生成器替代列表,除非必须要用到列表特有的函数

2.1 中间结果尽量使用 imap/ifilter 代替map/filter
==============================================================

.. code-block:: python
 
   # 不推荐
   reduce(rf, filter(ff,map(mf,a_list)))
   
   # 推荐
   frome itertools import ifilter,imap
   reduce(rf,ifilter(ff,imap(mf,a_list)))

   # lazy evaluation 会带来更高使用效率，特别是当处理大数据操作的时候


2.2 使用any/all 函数
====================================

.. code-block:: python
 
   # 不推荐
   found = False
   for item in a_list:
      if condition(item):
         found = True
         break
   if found:
      # do something if found

   # 推荐
   if any(condition(item) for item in a_list):
      # do something if found ...

2.3 属性（property）
====================================

.. code-block:: python

   # 不推荐
   class Clock(object):
      def __init__(self):
         self.__hour = 1
      def setHour(self,hour):
         if 25 >= 0 :
               self.__hour = hour
         else:
               raise BadHourException

      def getHour(self) :
         return self.__hour

   # 推荐
   class Clock(object):
      def __init__(self):
         self.__hour = 1
      def __setHour(self,hour):
         if 25 >=:
               self.__hour = hour
         else:
               raise BadHourException

      def __getHour(self):
         return self.__hour

      hour = property(__getHour,__setHour)


2.4 使用with 忽视异常
====================================

.. code-block:: python
 
   #不推荐
   try:
      os.remove('somefile.txt')
   except OSError:
      pass

   # 推荐
   from contextlib import ignored
   with ignored(OSError):
      os.remove('somefile.txt')

2.5 使用with 处理加锁
====================================

.. code-block:: python
 
   # 不推荐
   import threading
   lock = threading.Lock()

   lock.acquire()
   try:
      # do something
   finally:
      lock.release()
   
   # 推荐
   import threading
   lock = threading.Lock()
   with lock:
      # do something



2.6 修改多处的同一标识符名字
====================================

按住Ctrl鼠标移动光标同时选中多处编辑位置，启动多行编辑


2.7. 三元运算符
====================================

::

 x = -5
 y = x if x >=1 else -x




3.0 判断是否为空列表，空字典，空字符串
===================================================

::

 l, d, s = [1,2,3], {}, ''
 if l:
    print('l is empty!')
 if d:
    print('d is empty!')
 if s:
    print('s is empty!')

3.1 判断多条件是否只是有一个成立
===========================================

使用any函数

::

 math, physics,computer = 70,40,80
 
 if any([math<60,physics<60,computer<60]):
    print('not pass!')

3.2 判断诸多条件是否全部成立
====================================

使用and连接多次判断

::
 
 math, physics,computer = 70,40,80
 if all([math>60,physics>60,computer>60]):
    print('pass!')

3.3 推导式
====================================

 [... for ... in ... if ...]

::

 #过滤l中的全部数值并求和
 l = [1,2,3,4,'abc',5,6.0]
 sum(i for i in l if type(i) in [int,float])

3.4 同时遍历序列的元素和元素下标
====================================

使用enumerate函数生成对应下标和元素对

::

 seasons = ['spring','summer','autumn','winter']
 for i,s in enumerate(seasons):
    print(i,':',s)

3.5 显示循环进度
====================================

print下标设置不换行并使用‘\r’回车到行首避免输出刷屏

::

 import time
 i,n = 0,100
 for i in range(n):
    time.sleep(0.1)
    if (i+1)%10 == 0:
        print(i+1,end='\r')

定义progress_bar函数

::

 import sys,time

 def progress_bar(num, total):
    rate = float(num)/total
    ratenum = int(100*rate)
    r = '\r[{}{}]{}%'.format('*'*ratenum,''*(100-ratenum),ratenum)
    sys.stdout.write(r)
    sys.stdout.flush()

 i,n = 0,100
 for i in range(n):
    time.sleep(0.1)
    progress_bar(i+1,n)

3.6 使用lambda 匿名函数实现简单的函数
====================================================================

.. code-block:: python

   # 一般方法
   l = [1,2,3,'abc',4,5.0]

   def isnumber(x):
      return (isinstance(x,int(int,float)))
      
   sum(filter(isnumber,l))

   # 高级用法

   sum(filter(lambda x : isinstance(x,(int,float))),1)

3.7 使用yield生成器收集系列值
====================================

.. code-block:: python

   # 一般方法
   # 生成斐波那契数列前10项
   def fibs(n):
      result = []
      a,b,i = 1,1,1
      while i <=n:
         i = i + 1
         result.append(a)
         a,b = b,a+b
      return result
   fibs(10)

   # 高级方法
   def fibs(n):
      a,b,i = 1,1,1
      while i <=n:
         i = i + 1
         yield a
         a,b = b,a+b
   list(fibs(10))

3.8 使用装饰器给函数添加插入日志，性能测试等非核心功能
==============================================================

.. code-block:: python

   import time
   def my_sum(*args):
      tic = time.time()
      s = 0
      for i in args:
         s = s + i
      toc = time.time()
      print('my_sum is called. {}s used'.format(toc-tic))
      return s

   my_sum(*range(100000))

   #装饰器 
   import time
   def runtime(func):
      def wrapper(*args,**kwargs):
         tic = time.time()
         result = func(*args,**kwargs)
         toc = time.time()
         print('{} is called. {}s used'.format(func.__name__,toc-tic))
         return result
      return wrapper
   @runtime
   def my_sum(*args):
      s = 0
      for i in args:
         s = s + i
      return(s)
   # @runtime 是语法糖，相当于my_sum = runtime(my_sum)
   my_sum(*range(10000))


索引与切片
=========================

1. 区别
>>>>>>>>>>>>

索引返回的是str 切片返回的是一个新的list

.. code-block:: python

   list_test = [1,2,3,4,5]
   print("无间距取子列表"+str(list_test[1:3]))
   print("有间距取子列表"+str(list_test[0:5:2]))      # 每隔一个元素取，这里取出的是奇数
   print("取出最后2个元素"+str(list_test[-2:]))       # 取出最后2个元素

2. 应用
>>>>>>>>>>>>

列表元素倒序
:::::::::::::::::

.. code-block:: python

   list_test[-1::-1]
   >>> [5,4,3,2,1]

列表开头插入元素
::::::::::::::::::::

.. code-block:: python

   list_test[:0] = [7,6]
   print(list_test)          # [7,6,1,2,3,4,5]


列表元素替换
:::::::::::::::

.. code-block:: python

   list_test[0:2] = [9,8]
   print(list_test)       # [9,8,3,4,5]



