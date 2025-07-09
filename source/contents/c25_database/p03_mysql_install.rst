=====================
mysql安装
=====================

安装MySQL 5.6.13
=======================


下载的zip包有212MB，下载了几分钟就好了。

1、将mysql-5.6.13-winx64.zip 解压到D:\mysql-5.6.13\目录。

2、清理里面的调试文件
打开这个目录，发现里面的文件夹和文件跟一个安装好后的MySQL基本没有区别。可能你会很郁闷，这个MySQL5.6.13居然有1.04GB，呵呵，仔细一看你就会发现，里面有很有调试文件。后缀为.lib或.pdb的，其实可以删除掉。还有一些名为debug的目录，也删除掉吧。这样是不是就小很多了。

3、创建my.ini作为MySQL的配置文件
默认情况下没有my.ini文件，这需要我们手工创建一个。怎么创建呢？有没有像php.ini那样有模板呢？其实在MySQL5.6.13中带了一个my-default.ini，可以算作模板，只是里面的内容实在太少了。于是洪哥带大家手工创建一个my.ini。
直接创建一个文本文件，命名为my.ini。打开它，输入如下内容：

.. code-block:: text
   

   [mysqld]

   #绑定IPv4和3306端口
   bind-address = 0.0.0.0
   port = 3306

   # 设置mysql的安装目录
   basedir=D:/mysql-5.6.13

   # 设置mysql数据库的数据的存放目录
   datadir=D:/mysql-5.6.13/data

   # 允许最大连接数
   max_connections=200

好了，这样一个基本的MySQL环境所需要的参数就够了。

4、将MySQL安装成服务
打开一个cmd.exe，将目录切换到D:\MySQL-5.6.13\bin，运行： mysqld -install ，提示服务安装成功！（win8管理员运行命令行）。运行services.msc一看，确实有一个名为MySQL的服务了，启动它。
删除服务 mysqld -remove

到此，MySQL5.6.13已经可以正常使用了。


非root用户安装
=======================



参考文档
===========

博客：https://www.cnblogs.com/niuniutry/p/3555778.html

