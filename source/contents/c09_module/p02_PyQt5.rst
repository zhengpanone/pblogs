==================
1. PyQt5使用
==================

.. code:: python

 # 导入模块
 import sys
 from PyQt5.Qt import *

 # 1. 创建一个应用程序对象
 app = QApplication(sys.argv)



 # 2. 控件操作
 # 创建控件，设置控件大小，位置，样式，事件，信号处理
 # 2.1 创建控件
 window = QWidget()

 # 2.2 设置控件
 # 当创建一个控件后，如果说这个控件没有父控件，则把它当作顶层控件（窗口）
 # 系统会自动给窗口添加一些装饰（标题栏），窗口控件具备一些特性（标题，图标）

 # 2.3 展示控件
 # 刚创建好一个控件后，（这个控件没有父控件），默认情况下不会被展示，只有手动调用show()
 # 如果这个控件，有父控件，一般情况下，父控件展示后，子控件会自动展示
 window.show()



 # 3. 应用程序执行，进入到消息循环
 sys.exit(app.exec_())
 

QOBject
===========================


