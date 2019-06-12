======================================
2. 压缩和解压文件
======================================


压缩和解压命令gz、tar、zip、bz2
========================================

gzip
----------------

- 压缩后的格式为：*.gz
- 这种压缩方式不能保存原文件；且不能压缩目录

::

 # 压缩
 gzip buodo

 # 解压
 gunzip buodo.gz

tar 
-----------------

- 命令选项

::

 -z(gzip)      用gzip来压缩/解压缩文件
 -j(bzip2)     用bzip2来压缩/解压缩文件
 -v(verbose)   详细报告tar处理的文件信息
 -c(create)    创建新的档案文件
 -x(extract)   解压缩文件或目录
 -f(file)      使用档案文件或设备，这个选项通常是必选的。

::

 # 压缩
 tar -zvcf buodo.tar.gz buodo
 tar -jvcf buodo.tar.bz2 buodo 

 # 解压
 tar -zvxf buodo.tar.gz
 tar -jvxf buodo.bz2

zip
-----------------------

- 与gzip相比：
 1 可以压缩目录；
 * 可以保留原文件

- 命令选项

::

 -r(recursive)    递归压缩目录内的所有文件和目录

::

 zip -r Demo.zip Demo
 unzip Demo.zip

bzip2
-------------------

- 压缩后的格式：.bz2
- 参数

::

 -k 产生压缩文件后保留原文件

::

 # 压缩
 bzip2 Demo
 bzip2 -k Demo

 # 解压
 bunzip2 Demo.bz2



