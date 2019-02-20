=============================================
5.5 pdb 调试
=============================================

pdb 是基于命令行的调试工具，类似于gnu的gdb(调试C/C++)

执行时调试
==================

::

 python -m pdb some.py

命令

- **l** list 展示当前代码
- **n** next 向下执行一行代码
- **c** continue 继续执行代码
- **b** break 添加断点 b+行数,查看断点
- **clear** clear1 删除断点
- **s** step 进入到一个函数
- **p** print 打印一个变量的值
- **a** arg 打印所有参数
- **r** return 快速执行到函数最后一行
- **q** quit 退出调试

交互调试
=======================

::

 import pdb
 pdb.run('testfun(args)') # 此时会打开pdb调试，先使用s跳转到这个testfun函数中，然后就可以调试

程序里埋点
================================

当程序执行到pdb.set_trace()位置时停下来调试

::

 import pdb
 pdb.set_trace()


日志调试
=============================



PEP8
================================


括号中使用垂直隐式缩进或使用悬挂缩进。后者注意第一行没有参数，后续行要有缩进

::

 # 对准左括号
 foo = long_function_name(var_one,var_tow,
                          var_three,var_four)

 # 不对准左括号，但加多一层缩进，以和后面内容区别
 def foo = long_function_name(
      var_one,var_tow,
      var_three,var_four)
   print(var_one)

 # 悬挂缩进必须多加一层缩进
 foo = long_function_name(
    var_one,var_tow,
    var_three,var_four)

库导入顺序：标准库、相关第三方库、本地库。各组之间要有用空格

::

 import sys
 import os

 import flask
 import flask_mail

 import locallib
 
PEP 257，三个引号都使用双引号
逗号、冒号、分号之前避免空格

::

 if x == 4: print x, y; x, y = y, x


括号里面避免空格

::

 spam(ham[1], {egg: 2})


索引操作中冒号前后有没有空格

::

 ham[1:9], ham[1:9:3]

关键字参数和默认值参数的前后不要加空格

::

 def complex(real, image=0.0):
   return magic(r=real,i=image)
   