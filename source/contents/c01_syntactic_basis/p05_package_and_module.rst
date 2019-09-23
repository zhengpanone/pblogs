=========================
5. 包和模块
=========================

1.  一个模块(module)就是一个py文件,模块名字就是该文件名字

#.  一个包(package)就是一个文件夹,(python2规定文件夹中必须包含一个__init__.py,python3没有要求),包名就是文件夹名

#.  按import进来的对象不同分为4种场景：

::
 
 import <package>  # 导入一个包
 import <module> # 导入一个模块
 from <package> import <module or subpackage or object> # 从一个包中导入模块/子包/对象
 from <module> import <object> # 从模块中导入对象

#.  解释器会按照sys.path 列表的顺序来查找被引入的包或模块名字

 >>> import sys
 >>> import pprint
 >>> pprint.pprint(sys.path)
 ['',
  'C:\\Python\\Python36\\python36.zip',
  'C:\\Python\\Python36\\DLLs',
 ]
 
优先加载当前目录下的模块,如果项目中使用了与内建模块中同名的包或者模块名,就会遇到没有XX属性之类的报错提示

#.  使用sys.path,使得其他路径的文件加入到Path中,使解释器可以发现

::

 test.py
 import sys,os
 # 当前目录没hi模块,报错找不到模块
 import hi
 Traceback (most recent call last):
 ImportError: No module named hi

 # hi模块所在的位置:/data/hi.py
 # 将hi 所在的模块加入sys.path
 sys.path.append('/data')

 # 可以正常工作
 import hi

#. 另外一种加载模块的方法: 如果模块不在sys.path下面,可以使用imp 模块中的imp.load_source

::

 import imp
 imp.load_source('hi', 'C://data/hi.py')
 import hi

 # 可以自己指定模块的名字,相当于import hi as h2
 imp.load_source('h2', 'C://data/hi.py')
 import h2

7. import module时, 模块中所有代码将被执行(类对象,函数对象将被创建,不会被调用),import package 时, __init__.py 文件中的代码也将被执行

8. 模块的__file__ 属性
   导入模块时,可以通过模块的__file__属性查看模块所在的磁盘路径位置

 >>> import requests
 >>> requests.__file__
 'D:\\Programs\\Anaconda3\\envs\\py_test\\lib\\site-packages\\requests\\__init__.py'

9. 永远不要使用 from <module> import \*,有不可预知的风险


