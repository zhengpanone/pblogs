===============================
Python安装
===============================

1.安装依赖环境
-----------------

Python3在安装的过程中可能会用到各种依赖库，所以在正式安装Python3之前，需要将这些依赖库先行安装好。

::

 yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel

2. 下载Python3源代码
-------------------------

下载Python3的源代码有两种方式，一种是在它的官网下载，网址如下：

::

 https://www.python.org/downloads/source/

另外一种方式是通过wget直接下载，如以下命令：

::

 wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tgz

3. 创建安装目录
-------------------

安装目录可依个人喜好创建，比如在此创建在 /usr/local/python3 ：

::

 mkdir -p /usr/local/python3

4. 解压源码包
------------------

将第2步下载到的源码包进行解压，命令为：

::
 
 tar -zxvf Python-3.6.1.tgz

5. 编译源码
--------------

先进入解压后源码包的目录，再进行配置：

::

 cd Python-3.6.1
 ./configure --prefix=/usr/local/python3

之后再编译，然后再安装：

::

 make
 make install

6. 建立Python3的软链接
-----------------------------

::
 
 ln -s /usr/local/python3/bin/python3 /usr/bin/python3

7.  将/usr/local/python3/bin加入PATH
-------------------------------------------

编辑bash_profile进行修改环境变量：

::

 vim ~/.bash_profile

在PATH变量下将Python3的启动目录添加进去：

::

 # .bash_profile

 # Get the aliases and functions
 if [ -f ~/.bashrc ]; then
        . ~/.bashrc
 fi

 # User specific environment and startup programs

 PATH=$PATH:$HOME/bin:/usr/local/python3/bin

 export PATH

改动完毕之后，按Esc，再输入:wq进行保存退出。

8. 检查Python3及Pip3是否正常可用
----------------------------------------

执行如下命令（注意：V是大写的V），如果看到的结果一致的话，说明Python3已经成功安装。

::

 [alvin@VM_0_16_centos ~]$ python3 -V
 Python 3.6.1
 [alvin@VM_0_16_centos ~]$ pip3 -V
 pip 9.0.1 from /usr/local/lib/python3.6/site-packages (python 3.6)

避坑指南
--------------

其实，对于Python3的安装，网络上有太多的帖子了，步骤其实都大同小异。但是，在真正动手安装之后，或多或少都会遇到一些麻烦，特别是对新手而言。下面良许就列举一些常见的坑：

坑1：configure: error: no acceptable C compiler found in $PATH
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

这个问题就比较简单，就是缺少gcc编译环境。将gcc安装上即可：

::

 yum install -y gcc

当然除此之外，采用源码安装的方式也可以。

坑2：zipimport.ZipImportError: can’t decompress data
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

这种问题就是因为缺少zlib 的相关工具包导致的，将相关依赖包装上即可：

::
 
 yum -y install zlib*

安装之后再重新编译源码，即可解决。

坑3：pip3: Can't connect to HTTPS URL because the SSL module is not available
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

这个问题是因为在./configure过程中，如果没有加上–with-ssl参数时，默认安装的软件涉及到ssl的功能不可用，刚好pip3过程需要ssl模块，而由于没有指定，所以该功能不可用。解决办法如下：

::

 cd Python-3.6.2
 ./configure --with-ssl
 make
 sudo make install

坑4：Multilib version problems
>>>>>>>>>>>>>>>>>>>>>

这个很明显了，就是同一个库有多个版本。把多余的版本删除了就好。
首先查询已有的版本（以openssl为例，冲突哪个查哪个）

::

 # rpm -qa | grep openssl
 openssl-devel-1.0.0-27.el6_4.2.x86_64
 openssl-1.0.0-27.el6_4.2.x86_64
 openssl-1.0.0-27.el6_4.2.i686

可以看到系统里安装了openssl-1.0.0-27.el6_4.2.x86_64和openssl-1.0.0-27.el6_4.2.i686两个版本的openssl，我们留下x86的版本即可：

::

 rpm --erase --nodeps openssl-1.0.0-27.el6_4.2.i686

再更新一下openssl：

::

 # yum update "openssl*"

再查询一下openssl，问题解决！

::
 # rpm -qa | grep openssl
 openssl-devel-1.0.1e-16.el6_5.7.x86_64
 openssl-1.0.1e-16.el6_5.7.x86_64


参考
-------

公众号：良许  良许Linux https://mp.weixin.qq.com/s/PYl8cI7tV83Pqjw35JsWRg