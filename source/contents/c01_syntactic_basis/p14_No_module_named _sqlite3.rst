=============================================================
14 ImportError: No module named _sqlite3如何解决方法
=============================================================

有root权限

yum install sqlite-devel

重新编译python


没有root权限

从另一个已安装好的python中复制动态库

.. note::

 find ./ -name _sqlite3.so

 ./lib/python3.6/sqlite3

 ./lib/python3.6/lib-dynload/_sqlite3.cpython-36m-x86_64-linux-gnu.so

 将lib-dynload下的文件复制到缺少动态库的python中就不会报错

