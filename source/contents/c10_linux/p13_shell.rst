=========================
shell编程
=========================


echo输出颜色

.. literalinclude:: ./code/shell/echo.sh
    :encoding: utf-8
    :language: shell
    :emphasize-lines: 0,8
    :linenos:

位置参数变量

脚本参数传参： $1 $2 $3 ... ${10}

预先定义变量

- $0 脚本文件名
- $* 所有的参数
- $@ 所有的参数
- $# 参数的个数
- $$ 当前进程的PID
- $! 上一个后台进程的PID
- $? 上一个命令的返回值 0表示成功

>>> sh parameter.sh 1 2 3 4 5 6 7 8 9 10

.. literalinclude:: ./code/shell/parameter.sh
    :encoding: utf-8
    :language: shell
    :emphasize-lines: 0,17
    :linenos:










