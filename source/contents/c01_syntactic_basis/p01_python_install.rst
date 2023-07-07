===============================
1. 安装Python
===============================

linux安装
=========================

1.安装依赖环境
--------------------------

Python3在安装的过程中可能会用到各种依赖库，所以在正式安装Python3之前，需要将这些依赖库先行安装好。



>>> yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel \
    sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel

2. 下载Python3源代码
--------------------------------------

下载Python3的源代码有两种方式，一种是在它的官网下载，网址如下：

::

 https://www.python.org/downloads/source/

另外一种方式是通过wget直接下载，如以下命令：



>>> wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tgz

3. 创建安装目录
------------------------------

安装目录可依个人喜好创建，比如在此创建在 /usr/local/python3 ：

>>> mkdir -p /usr/local/python3

4. 解压源码包
--------------------------------

将第2步下载到的源码包进行解压，命令为：
 
>>> tar -zxvf Python-3.6.1.tgz

5. 编译源码
-------------------------------

先进入解压后源码包的目录，再进行配置：

>>> cd Python-3.6.1 && \
 ./configure --prefix=/usr/local/python3

之后再编译，然后再安装：

>>> make && make install

6. 建立Python3的软链接
------------------------------------------------
 
>>> ln -s /usr/local/python3/bin/python3 /usr/bin/python3

7.  将/usr/local/python3/bin加入PATH
-------------------------------------------------------------------

编辑bash_profile进行修改环境变量：

>>> vim ~/.bash_profile

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
------------------------------------------------------------------

执行如下命令（注意：V是大写的V），如果看到的结果一致的话，说明Python3已经成功安装。

::

 [alvin@VM_0_16_centos ~]$ python3 -V
 Python 3.6.1
 [alvin@VM_0_16_centos ~]$ pip3 -V
 pip 9.0.1 from /usr/local/lib/python3.6/site-packages (python 3.6)

避坑指南
-------------------------------

其实，对于Python3的安装，网络上有太多的帖子了，步骤其实都大同小异。但是，在真正动手安装之后，或多或少都会遇到一些麻烦，特别是对新手而言。下面良许就列举一些常见的坑：

坑1：configure: error: no acceptable C compiler found in $PATH
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

这个问题就比较简单，就是缺少gcc编译环境。将gcc安装上即可：

>>> yum install -y gcc

当然除此之外，采用源码安装的方式也可以。

坑2：zipimport.ZipImportError: can’t decompress data
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

这种问题就是因为缺少zlib 的相关工具包导致的，将相关依赖包装上即可：

::
 
 yum -y install zlib*

安装之后再重新编译源码，即可解决。

坑3：pip3: Can't connect to HTTPS URL because the SSL module is not available
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

这个问题是因为在./configure过程中，如果没有加上–with-ssl参数时，默认安装的软件涉及到ssl的功能不可用，刚好pip3过程需要ssl模块，而由于没有指定，所以该功能不可用。解决办法如下：

::

 cd Python-3.6.2
 ./configure --with-ssl
 make
 sudo make install

坑4：Multilib version problems
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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
----------------

`良许Linux`_

.. _`良许Linux`: https://mp.weixin.qq.com/s?__biz=MzU3NTgyODQ1Nw==&mid=2247485198&amp;idx=1&amp;sn=0792d4da7ca2346ec3282c73bb608198&source=41#wechat_redirect


更改PyPI 镜像（源）
============================

更改pip
------------------

临时设置
>>>>>>>>>>>>>>>>>>>>>


pip临时设置可以通过 -i 选项：

.. code-block:: shell

    pip install -i https://pypi.doubanio.com/simple/ flask

全局设置
>>>>>>>>>>>>>>>>>>>>>

全局设置有不同的层级和文件位置，以用户全局（per-user）为例，在 Linux & macOS 中，配置需要写到 **~/.pip/pip.conf** 文件中；Windows 中，配置文件位置为 **%HOMEPATH%\pip\pip.ini**，%HOMEPATH% 即你的用户文件夹，一般为“**\Users\<你的用户名>**”，具体值可以使用 **echo %HOMEPATH%** 命令查看。

通常你需要手动创建对应的目录和文件，然后写入下面的内容：


.. code-block:: text
    :linenos:

    [global]
    index-url = https://pypi.doubanio.com/simple
    [install]
    trusted-host = pypi.doubanio.com

附注：按照 pip 文档，上面的配置文件位置是旧（legacy）的配置方式，但是因为比较方便设置，这里沿用了。新的建议是 Linux & macOS 放到 $HOME/.config/pip/pip.conf，Windows 则放到 %APPDATA%\pip\pip.ini。具体可以访问 `pip文档配置 <https://pip.pypa.io/en/stable/user_guide/#config-file>`_ 部分查看。

Pipenv
-----------------

类似 pip 的 -i （--index-url）选项，你可以使用 --pypi-mirror 临时设置镜像源地址：


.. code-block:: shell
    
    pipenv install --pypi-mirror https://pypi.doubanio.com/simple flask


如果想对项目全局（per-project）设置，可以修改 Pipfile 中 [[source]] 小节：

.. code-block:: text
    :linenos:

    [[source]]

    url = "https://pypi.doubanio.com/simple"
    verify_ssl = true
    name = "douban"

另外一种方式是使用环境变量 PIPENV_PYPI_MIRROR 设置（Windows 系统使用 set 命令）：

.. code-block:: shell

    export PIPENV_PYPI_MIRROR=https://pypi.doubanio.com/simple

常用的国内 PyPI 镜像列表
-------------------------------------

.. code-block:: text
    :linenos:

    豆瓣 https://pypi.doubanio.com/simple/
    网易 https://mirrors.163.com/pypi/simple/
    阿里云 https://mirrors.aliyun.com/pypi/simple/
    清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
