================
1.4  Python编程技巧
================

Map
---------

map函数将函数应用于iterable中的每一项 。Map需要2个输入，分别是应用函数和可迭代对象

::

 map(function,iterable)


Lambda
-----------

::

 square = lambda x : x *x
 square(3)
 >>> 9

lambda x:可以理解为，python 的lambda函数，输入叫x,冒号之后的任何内容是对输入的操作，它会自动返回结果，可以简化为一行代码：

::

 x = [1,2,3,4,5]
 print(list(map(lambda num*num , x)))


Reduce
-----------

Reduce 是将迭代变成一个东西的函数。通常可以在列表上使用reduce函数执行计算以将其减少到一个数字

::

 reduce(function, list)

经常使用lambda表达式作为函数

::

 product = 1
 x = [1,2,3,4]
 for num in x:
    product = product * num

reduce 改写：

::

 from functools import reduce
 product = reduce((lambda x ,y : x * y),[1,2,3,4])

Filter
-------

filter函数采用可迭代的方式，并过滤掉可迭代中不需要的内容

::

 filter(function,list)

::

 x = range(-5,5)
 new_list = []
 for num in x:
    if num < 0:
        new_list.append(num)

::

 x = range(-5,5)
 all_less_than_zero = list(filter(lambda num:num<0),x)


高阶函数
-----------

高阶函数可以将函数作为参数并返回函数

高阶函数例子

::

 def summation(nums):
    return sum(nums)

def action(func,numbers):
    return func(numbers)

 print(action(summation,[1,2,3]))


::

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
----------------------

Partial application(闭包)

创建一个函数，它接受2个参数，一个基数和一个指数，并返回指数幂的基数，如下所示：

::

 def power(base,exponent):
    return  base**exponent

::

 from functools import partial
 square = partial(power,exponent=2)
 print(squaer(2))
 >>> 4

使用一个循环来生成一个幂函数，该函数实现从立方体一直到1000的幂。

::

 from functools import partial
 powers = []
 for x in range(2,1001):
    powers.append(partial(power,exponent=x))

 print(powers[0],[3])
 >>> 9

列表推导式
-------------
::

 [function for item in iterable]

 print([x*x for x in range(5)])

 all_less_than_zero = list(filter(lambda num :num <0,x))

 all_less_than_zero = [num for num in x if num < 0]

 all_less_than_zero = list(map(lambda num:num*num, list(filter(lambda num:num<0,x ))))

列表推导仅适用于列表。map,filter适合任何可迭代的对象


三元表达式
---------------------

::

 print("Hello" if True else "World")

打印JSON
----------------

::

 import json
 print(json.dumps(data,indent=2))

同时迭代两个列表
------------------------

::

 nfc = ["Packers", "49ers"]
 afc = ["Ravens", "Patriots"]
 for teama, teamb in zip(nfc, afc):
   print teama + " vs. " + teamb

带索引的列表迭代
-----------------------

::

 teams = ["Packers", "49ers", "Ravens", "Patriots"]
 for index,team in enumerate(teams):
   print(index,team)


初始化列表的值
------------------------

::
 
 items = [0]*3
 print(items)

>>> [0,0,0]


列表转字符串
-------------------------

::

 teams = ["Packers", "49ers", "Ravens", "Patriots"]
 print (", ".join(teams))

字典中获取元素
--------------------

::

 data = { user : 1,  name :  Max ,  three : 4}
 try:
   is_admin = data[ admin ]
 except KeyError:
   is_admin = False

替换为

::

 is_admin = data.get(admin,False)


获取列表的子集
----------------------

::

 x = [1,2,3,4,5,6]
 #前3个
 print x[:3]
 >>> [1,2,3]
 #中间4个
 print x[1:5]
 >>> [2,3,4,5]
 #最后3个
 print x[3:]
 >>> [4,5,6]
 #奇数项
 print x[::2]
 >>> [1,3,5]
 #偶数项
 print x[1::2]
 >>> [2,4,6]
 
迭代工具
------------------------

::

 from itertools import combinations
 teams = ["Packers", "49ers", "Ravens", "Patriots"]
 for game in combinations(teams, 2):
    print game
 >>> ( Packers ,  49ers )
 >>> ( Packers ,  Ravens )
 >>> ( Packers ,  Patriots )
 >>> ( 49ers ,  Ravens )
 >>> ( 49ers ,  Patriots )
 >>> ( Ravens ,  Patriots )