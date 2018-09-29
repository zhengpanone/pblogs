第三章 Python编程技巧
=========================

1.1 交换赋值
-------------------

::

 #不推荐
 temp = a
 a = b
 b = a

 #推荐
 a, b = b, a  # 先生成一个元组对象(tuple),然后unpack

1.2 Unpacking
-----------------

::

 #不推荐
 a = ['David,'Pythonista', '+1-514-55-1234'']
 first_name = a[0]
 last_name = a[1]
 phone_number = a[2]

 #推荐
 a = ['David,'Pythonista', '+1-514-55-1234'']
 first_name,last_name,phone_number = a
 # Python3 Only
 first, *middle,last = another_last

1.3 使用操作符in
-----------------

::
 
 ## 不推荐
 if fruit == 'apple' or fruit == 'orange' or fruit == 'berry':
    # 多次判断
 ## 推荐
 if fruit in ['apple','orange','berry']:
    # 使用in更加简洁

1.4 字符串操作
----------------

::

 # 不推荐
 colors = ['red','blue','green','yellow']
 result = ''
 for s in colors:
    result += s # 每次赋值都丢弃以前的对象,生成新对象


 ##
 colors = ['red','blue','green','yellow']
 result = ''.join(colors) # 没有额外的内存分配

1.5 修改多处的同一标识符名字
-------------------------

按住Ctrl鼠标移动光标同时选中多处编辑位置，启动多行编辑


1.7 多变量赋值
-----------------

::
 a, b, c, d = 0, 1, 2, 3, 4


1.8 链式调用
-------------------

::
 s = "Python $$ is simple, $$readable **and powerful!**"
 s = s.replace('$','').replace('*','')

1.9 三元运算符
------------------

::
 x = -5
 y = x if x >=1 else -x

2.0 判断是否为空列表，空字典，空字符串
----------------------

::
 l, d, s = [1,2,3], {}, ''
 if l:
    print('l is empty!')
 if d:
    print('d is empty!')
 if s:
    print('s is empty!')

2.1 判断多条件是否只是有一个成立
-----------------------

使用any函数

::
 math, physics,computer = 70,40,80
 
 if any([math<60,physics<60,computer<60]):
    print('not pass!')

2.2 判断诸多条件是否全部成立
----------------------

使用and连接多次判断

::
 
 math, physics,computer = 70,40,80
 if all([math>60,physics>60,computer>60]):
    print('pass!')

2.3 推导式

[... for ... in ... if ...]

::
 过滤l中的全部数值并求和
 l = [1,2,3,4,'abc',5,6.0]
 sum(i for i in l if type(i) in [int,float])

2.4 同时遍历序列的元素和元素下标
-------------------

使用enumerate函数生成对应下标和元素对

::
 seasons = ['spring','summer','autumn','winter']
 for i,s in enumerate(seasons):
    print(i,':',s)

2.5 显示循环进度
--------------------

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

2.6 使用lambda 匿名函数实现简单的函数
------------------------

::
 # 一般方法
 l = [1,2,3,'abc',4,5.0]

 def isnumber(x):
    return (isinstance(x,int(int,float)))
    
 sum(filter(isnumber,l))

 # 高级用法

 sum(filter(lambda x : isinstance(x,(int,float))),1)

2.7 使用yield生成器收集系列值
----------------------

::
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

2.8 使用装饰器给函数添加插入日志，性能测试等非核心功能
---------------------------

::
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
