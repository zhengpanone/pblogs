==========================
4.2 生成器
==========================

不会将所有的一次性加载到内存中，延迟计算，一次返回一个结果，不会一次生成所有的结果, 处理大数据非常有用

1.将推导式的[] 改成()
========================================

::

 L = [x*2 for x in range(10)]
 G = (x*2 for x in range(10)) # 生成器
 
 next(G)
 
::

 def fun():
    for i in range(1,50):
        yield i
 for i in fun():
    print(i)
2. yield 创建生成器
========================================

生成器函数：一个函数中包含yield关键字, 这个函数是一个生成器函数
调用生成器函数,不会立马执行该函数里的代码,而返回一个生成器

::

 def createNum():
   print("--------start---------")
   a,b = 0,1
   for i in range(10):
      print("-------1-------")
      yield b 
      print('-------2--------')
      a,b = b,a+b
      print('-------3---------')
   print('--------stop------------')

 a = createNum()
 for i in a:
   print(i)

>>> import createNum
>>> n = next(createNum)  # 返回值为b的值

::

 sum(x for x in range(1000000000)) # 占用内存少
 sum([x for x in range(1000000000)]) # 占用内存大

原理: sum 函数是python3内置函数,该函数使用迭代器协议访问对象,而生成器实现了迭代器协议,所以可以直接计算一系列值的和,不用先构造一个列表


3.send
==========================

::

 def test():
   i = 0
   while i < 5:
      temp = yield i
      print(temp)
      i +=1

 t = test()
 t.__next__()
 t.send("haha")

4.多任务（协程）
==================================

::

 def test1():
   while True:
      print('-------1---------')
      yield 

 def test2():
   while True:
      print('-------2---------')
      yield

 t1 = test1()
 t2 = test2()
 while True:
   t1.__next__()
   t2.__next__()