第三章 Python编程技巧
=========================

1.1 交换赋值

::

 #不推荐
 temp = a
 a = b
 b = a

 #推荐
 a, b = b, a  # 先生成一个元组对象(tuple),然后unpack

1.2 Unpacking

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

::
 
 ## 不推荐
 if fruit == 'apple' or fruit == 'orange' or fruit == 'berry':
    # 多次判断
 ## 推荐
 if fruit in ['apple','orange','berry']:
    # 使用in更加简洁

1.4 字符串操作

::

 # 不推荐
 colors = ['red','blue','green','yellow']
 result = ''
 for s in colors:
    result += s # 每次赋值都丢弃以前的对象,生成新对象


 ##
 colors = ['red','blue','green','yellow']
 result = ''.join(colors) # 没有额外的内存分配

