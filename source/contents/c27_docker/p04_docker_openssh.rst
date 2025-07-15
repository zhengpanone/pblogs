==============================================
4. Docker 安装CentOS7 并设置SSH远程
==============================================

搜索镜像
=============

.. note::

 docker search centos 

下载镜像
==========================

docker pull 镜像名：TAG

.. note::

 docker pull centos:latest 
 
 docker pull centos:6.7

查看镜像
============================

.. note::

 docker images

启动镜像
============================

.. note::

 docker run --privileged -itd -p 8888:22 --name centos7_ssh 9f38484d220f /usr/sbin/init

 --privileged 启动后让容器具备超级特权

 -itd 交互式、终端、后台运行

 -p 把宿主机的8888端口映射到docker的22端口

 **宿主机就是运行docker的机器，这样访问宿主机IP:8888端口，实际访问的是docker的22端口。**

 \-\-name  给启动的容器命名，方便后续操作

 9f38484d220f 就是IMAGE ID

 **注：\-\-privileged  和/usr/sbin/init是必须的，否则会报错。**
 Failed to get D-Bus connection: Operation not permitted

进入容器并配置ssh服务
============================================

.. note::

  .. code-block:: bash

    进入容器
    docker exec -it centos7_ssh /bin/bash

    ----------------------以下都是在容器内部操作--------------------------
    # 安装openssh
    yum install -y openssh-server openssh-clients

    **修改sshd_config配置**
    vi /etc/ssh/sshd_config

    # 监听端口、监听地址前的 # 号去除

    Port 22
    
    #AddressFamily any

    ListenAddress 0.0.0.0

    ListenAddress ::
    
    # 开启允许远程登录

    PermitRootLogin yes

    # 开启使用用户名密码来作为连接验证

    PubkeyAuthentication yes

    启动openssh

    systemctl start sshd.server

    重启 sshd服务命令 

    systemctl restart sshd.service

    设置服务开启自启命令 

    systemctl enable sshd.service

    **centos解决bash: service: command not found**

    yum list | grep initscripts

    yum install initscripts -y

    此时 service命令可以使用了


    设置root密码
    passwd

    退出容器
    exit

ssh登录
====================================

.. code-block:: shell

    ssh root@localhost -p 8888

宿主机root用户仍然可以直接通过下面命令登录

.. code-block:: shell

    docker exec -it centos7 /bin/bash

添加/更改容器映射端口
===============================

在宿主机修改 /var/lib/docker/containers/[hash_of_the_container]/hostconfig.json / config.v2.json 两个文件

将docker容器提交为镜像
==========================================

.. code-block:: shell

    docker commit 481b2aad8d5f centos_ssh 

    # 481b2aad8d5f 为容器id、centos_ssh为镜像名称

将新的镜像启动，并将docker服务器的50001端口映射到容器的22端口上,给容器命名 

.. code-block:: shell

    docker run --privileged -d -p 50001:22 --name=centos_ssh_servier 371a214b38b5 /usr/sbin/init

 

