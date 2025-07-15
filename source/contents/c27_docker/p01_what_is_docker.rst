========================================
Docker 基本概念
========================================

基本概念
=====================

Docker组成
------------------

Docker组成：Docker Client 和 Docker Server

Docker组件：

- 镜像（Image）
 
- 容器（Container）
 
- 仓库（Repository）

容器（Container）：容器是一种轻量级、可移植、并将应用程序进行的打包的技术，使应用程序可以在几乎任何地方以相同的方式运行，Docker将镜像文件运行起来后，产生的对象就是容器。容器相当于是镜像运行起来的一个实例且容器具备一定的生命周期。

Docker容器和虚拟机的区别
-------------------------------

相同点：

- 容器和虚拟机一样，都会对物理硬件资源进行共享使用。
- 容器和虚拟机的生命周期比较相似（创建、运行、暂停、关闭等等）。
- 容器中或虚拟机中都可以安装各种应用，如redis、mysql、nginx等。也就是说，在容器中的操作，如同在一个虚拟机(操作系统)中操作一样。
- 同虚拟机一样，容器创建后，会存储在宿主机上：linux上位于/var/lib/docker/containers下

不同点：

- 虚拟机的创建、启动和关闭都是基于一个完整的操作系统。一个虚拟机就是一个完整的操作系统。而容器直接运行在宿主机的内核上，其本质上以一系列进程的结合。
- 容器是轻量级的，虚拟机是重量级的。首先容器不需要额外的资源来管理(不需要Hypervisor、Guest OS)，虚拟机额外更多的性能消耗；其次创建、启动或关闭容器，如同创建、启动或者关闭进程那么轻松，而创建、启动、关闭一个操作系统就没那么方便了。

也因此，意味着在给定的硬件上能运行更多数量的容器，甚至可以直接把Docker运行在虚拟机上。

容器的生命周期管理
========================

|image1|

Docker内部组件
=====================

1. Namespaces 命名空间，Linux内核提供的一种对进程 **资源隔离** 的机制，例如进程，网络，挂载点等资源。
2. CGroups 控制组，Linux内核提供的一种 **限制进程资源** 的机制；例如cpu,内存等资源。 ls -l /sys/fs/cgroups   主要防止某一个容器资源过多导致宿主机资源紧张
3. UnionFS 联合文件系统，支持将不同位置的目录挂载到同一虚拟文件系统，形成一种分层的模型。  


使用场景
=====================

1. Simplifying Configuration(简化配置)
#. Developer Productivity(简化开发环境)
#. Server Consolidation(应用隔离)
#. Multi-tenancy(多用户)
#. Code Pipeline Management(快速部署)
#. App Isolation(应用隔离)
#. Debugging Capabilities(开发调试)
#. Repid Deployment(交付方式改变)
#. 持续集成：CI(持续集成)、CD(持续部署) ;自动化项目测试流程:构建、部署、部署、测试、发布


UnionFs：联合文件系统
=====================

UnionFs(联合文件系统)：Union文件系统(UnionFs)是一种分层、轻量级并且高性能的文件系统，它支持对文件系统的修改作为一次提交来一层层的叠加，同时可以将不同目录挂载到同一个虚拟文件系统下，UnionFs联合文件系统是Docker镜像的基础，镜像可以通过分层来进行继承，基于基础镜像（没有父镜像），可以制作各种具体的应用镜像。


**特性：** 一次同时加载多个文件系统，但从外面看起来，只能看到一个文件系统，联合加载会把各层文件系统叠加起来，这样最终的文件系统会包含所有底层的文件和目录

Docker镜像加载原理
=====================

Docker的镜像实际上由一层一层的UnionFs文件系统组成
bootfs：主要包含 bootloader和 Kernel，bootloader主要是引导加 kernel，Linux刚启动时会加bootfs文件系统，在 Docker镜像的最底层是bootfs，这一层与我们典型的Linux/Unix系统是一样的，包含bootfs加载器和内核，当bootfs加载完成之后整个内核就都在内存中了，此时内存的使用权已由 bootfs转交给内核，此时系统也会卸载bootfs。


rootfs：在 bootfs之上，包含的就是典型 Linux系统中的/dev、/proc、/bin、/etc等标准目录和文件，rootfs就是各种不同的操作系统发行版，比如：Ubuntu,、CentOS等等

简单理解：

1. 对于Docker安装OS来说：就是Docker使用了Linux本身的bootfs，只需要安装自己所需的rootfs  2. 对于Docker安装普通镜像来说：就是Docker本身是分层下载镜像，所以可以提取出公共层镜像，进行复用
Docker镜像的特点
Docker镜像都是只读的，当容器启动时，一个新的可写层加载到镜像的顶部
这一层就是我们通常说的容器层，容器之下的都叫镜像层

Docker安装与启动
=====================


安装Docker
---------------------

1) yum包更新到最新

>>> sudo yum update

2) 安装需要的软件包， yum-util 提供yum-config-manager功能，另外两个是devicemapper驱动依赖的

>>> sudo yum install -y yum-utils device-mapper-persistent-data lvm2
   
   
3) 设置yum源为阿里云
   
>>> sudo yum-config-manager \
--add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
   
   
4) 安装docker
   
>>> sudo yum install docker-ce
   
5) 安装后查看docker版本
   
.. code-block:: shell
   
  docker -v
  docker version # 查看Docker版本
   
   
设置ustc的镜像
--------------------- 

ustc是老牌的linux镜像服务提供者了，还在遥远的ubuntu 5.04版本的时候就在用。ustc的docker镜像加速器速度很快。ustc docker mirror的优势之一就是不需要注册，是真正的公共服务。

`https://lug.ustc.edu.cn/wiki/mirrors/help/docker <https://lug.ustc.edu.cn/wiki/mirrors/help/docker>`_

编辑该文件：

>>> vi /etc/docker/daemon.json  

在该文件中输入如下内容：

.. code-block:: json

  {
  "registry-mirrors": ["https://docker.mirrors.ustc.edu.cn"]
  }


Docker的启动与停止
>>>>>>>>>>>>>>>>>>>>>>>>>

**systemctl** 命令是系统服务管理器指令
   
启动docker：

>>> systemctl start docker
   
   
停止docker：
   
>>> systemctl stop docker
   
   
重启docker：
   
>>> systemctl restart docker
   
   
查看docker状态：
   
>>> systemctl status docker
   
   
开机启动：
   
>>> systemctl enable docker
   
   
查看docker概要信息
   
>>> docker info
   
   
查看docker帮助文档

>>> docker --help


Docker常用命令
======================

镜像相关命令
---------------------

.. code-block:: shell

  docker search centos -f STARS=2000 #搜索过滤STARS大于2000的镜像
  docker search redis --limit 5 # 默认25个
  docker search --filter=stars=600 mysql # 只显示starts>=600 的镜像
  docker search --no-trunc mysql # 显示镜像完整description描述
  docker search --automated mysql # 只列出automated=ok 的镜像
  docker pull centos:latest # 下载镜像
  docker images # 查看本地的images信息
  docker images -a # 查看含中间映像层
  docker images -q # 只展示镜像ID
  docker images -qa # 含中间映像层
  docker images --digests # 显示镜像摘要信息
  docker images --no-trunc # 显示镜像完整信息
  docker system df 查看镜像/容器/数据卷所占的空间
  docker rmi -f 容器ID/镜像ID/名称  # 删除容器/镜像 -f强制删除镜像
  docker rmi -f $(docker images -q) # 删除全部镜像
  docker build -t express-demo . # 通过当前目录下Dockerfile构建镜像指定镜像名字为express-demo 参数t是tag的意思
  docker tag e6fasc zhengpanone/express-demo:v1.0 # 对镜像进行重命名


查看docker容器中运行的容器
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: shell

  docker ps  # 查看docker容器中运行的容器 ps表示process status的意思
  docker ps -a # 查看所有容器
  docker ps -l # 查看最后一次运行的容器
  docker ps -f status=exited # 查看停止的容器

容器相关命令
---------------------

容器创建(docker create)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

命令格式：
docker run [参数] 镜像 [容器执行命令] [执行命令提供的参数]

.. code-block:: shell

  docker run -itd --name=容器名称 镜像名称:标签 /bin/bash

常用参数：

- ``-i`` 表示interactive交互，保持输入打开
- ``-t`` 表示pseudo-TTY伪终端,分配一个虚拟终端
- ``-d``  detached mode的缩写，守护式容器在后台运行，并打印容器id 
- ``--name`` 为创建的容器命令
- ``-rm`` 容器结束后自动删除容器
- ``/bin/bash`` 表示执行一个新的bash shell

推荐使用 docker run -dti 来启动所需容器。

.. code-block:: shell
  
  docker run -d -v /Users/zhengpanone/Desktop/express-demo:/app -p 3000:3000 \
  --name express-demo-container express-demo-image

  docker run -d -v /Users/zhengpanone/Desktop/express-demo:/app:ro \
  -v /app/node_module -p 3000:3000 \
  --name express-demo-container express-demo-image
  # ro表示容器中的有新增文件,本地不会进行新增,让本地变为只读readonly
  # 表示 容器中的/app/node_module 不进行同步

  docker rm -fv express-demo-container # v表示销毁容器的时候把对应的volume给删掉,不然volume会越来越多

docker-compose启动容器
 
编写docker-compose.yml文件

.. code-block:: yaml

  version: "3.8" # 指定compose版本
  services:
    express-demo-container: # 容器名称
        build: . # 容器是根据哪个镜像构建的，根据当前文件下的Dockerfile构建
        ports:
          - "3000:3000"
        volumes:
          - ./:/app:ro
          - /egg/node_module

运行docker-compose

.. code-block:: shell
  
  # -d 表示后台运行容器 
  # --build 表示如果镜像有修改docker-compose就会重建,不加上--build下次就会使用之前的缓存
  docker-compose up -d --build 

docker-compose清除容器

.. code-block:: shell

  # -v表示清除对应的volume
  docker-compose down -v 


登录守护式容器方式

.. code-block:: shell

  docker exec -it 容器名称/容器ID /bin/bash

停止与启动容器
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: shell
   
  docker stop 容器名称/容器ID   # 停止容器
  docker start 容器名称/容器ID  # 启动容器

文件拷贝
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: shell 
   
  docker cp 需要拷贝的文件或目录  容器名称:容器目录   # 将文件拷贝到容器
  docker cp 容器名称:容器目录   需要拷贝的文件或目录  # 将文件从容器拷贝出来

目录挂载
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

创建容器 -v **宿主目录:容器目录**

.. code-block:: shell
   
  docker run -id -v /usr/local/myhtml:/usr/local/myhtml --name=mycentos7 centos:7

如果共享的是多级目录,可能出现权限不足提示

这是因为Centos7中的安全模块selinux把权限禁用了, 添加参数 **--privileged=true** 来解决挂载的目录没有权限的问题

查看容器IP地址
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: shell
   

  docker inspect 容器名称/容器ID

  # 可以直接执行下面的命令直接输出IP地址
  docker inspect --format='{{.NetworkSettings.IPAddress}}' 容器名称/容器ID

应用部署
====================


MySQL部署
------------------

拉取mysql镜像
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: shell

  docker pull mysql

创建容器 
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: shell

  # -p 表示端口映射,格式为宿主机映射端口:容器运行端口
  # -e 表示添加环境变量 MYSQL_ROOT_PASSWORD 是root用户的登录密码
  docker run --privileged=true --name=centos_mysql  -p 3306:3306 \
  -v $PWD/conf:/etc/mysql/conf.d -v $PWD/logs:/logs -v $PWD/data:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=123456  -d mysql  

tomcat部署
------------------

拉取tomcat镜像
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

>>> docker pull tomcat:7-jre7

.. _tomcat_container_create:

创建容器 
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: bash

  >>> docker run -di --name=mytomcat -p 9000:8080 \
  -v /usr/local/webapps:/usr/local/tomcat/webapps tomcat:7-jre7



Redis部署
------------------

拉取Redis镜像
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

>>> docker pull redis

.. _redis_container_create:

创建容器 
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

>>> docker run -di --name=myredis -p 6379:6379 redis

Nginx部署
------------------

拉取nginx镜像
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

>>> docker pull nginx

.. _nginx_container_create:

创建容器 
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

>>> docker run -di --name=mynginx -p 80:80 nginx

迁移与备份
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: shell
   
  # 容器保存为镜像
  docker commit mynginx mynginx_i 

  # 镜像备份
  docker save -o mynginx.tar mynginx_i

  # 镜像恢复与迁移
  
  docker load -i mynginx.tar


.. code-block::shell
   
  docker run -it centos:latest  #运行docker容器

  winpty docker run -it zhengpanone/centos-python  # **在windows下使用git bash 使用**

  docker commit -m '' CONTAINER ID IMAGE  # 将容器转化为一个镜像

  docker commit -m "安装 net-tools" -a 'zhengpanone'  5301d7c9bc21 zhengpanone/centos-python:V1
  # -m 指定说明信息; 
  # -a 指定用户信息 ;5301d7c9bc21代表容器id; 
  # zhengpanone/centos-python:V1指定目标镜像的用户名、仓库名和tag信息

  docker save -o ./centos.tar zhengpanone/centos:git # 保存镜像 -o/--output

  docker load -i ./centos.tar # 加载镜像 -i/--input 

利用Dockerfile创建镜像
Dockerfile可以理解为一种配置文件,用来告诉docker build命令应该执行那些操作。
一个简易的Dockerfile文件如下所示

.. code-block::shell

  # 说明该镜像以那个镜像为基础
  FROM centos:latest 

  # 构建者的基本信息
  MAINTAINER zhengpanone 

  # 在build 这个镜像时执行的操作
  RUN yum update
  RUN yum install -y git

有了Dockerfile 利用build命令构建镜像

.. code-block:: shell
 
  docker build -f ./Dockerfile  -t "zhengpanone/centos-git:gitdir" .

Docker 基础命令
------------------------------------

.. code-block:: text

  Usage:
  docker [OPTIONS] COMMAND [arg...]
        docker daemon [ --help | ... ]
        docker [ --help | -v | --version ]
  
  Options:
  --config=~/.docker              Location of client config files  #客户端配置文件的位置
  -D, --debug=false               Enable debug mode  #启用Debug调试模式
  -H, --host=[]                   Daemon socket(s) to connect to  #守护进程的套接字（Socket）连接
  -h, --help=false                Print usage  #打印使用
  -l, --log-level=info            Set the logging level  #设置日志级别
  --tls=false                     Use TLS; implied by--tlsverify  #
  --tlscacert=~/.docker/ca.pem    Trust certs signed only by this CA  #信任证书签名CA
  --tlscert=~/.docker/cert.pem    Path to TLS certificate file  #TLS证书文件路径
  --tlskey=~/.docker/key.pem      Path to TLS key file  #TLS密钥文件路径
  --tlsverify=false               Use TLS and verify the remote  #使用TLS验证远程
  -v, --version=false             Print version information and quit  #打印版本信息并退出

  Commands:
    attach    Attach to a running container  #当前shell下attach连接指定运行镜像
    build     Build an image from a Dockerfile  #通过Dockerfile定制镜像
    commit    Create a new image from a container's changes  #提交当前容器为新的镜像
    cp    Copy files/folders from a container to a HOSTDIR or to STDOUT  #从容器中拷贝指定文件或者目录到宿主机中
    create    Create a new container  #创建一个新的容器，同run 但不启动容器
    diff    Inspect changes on a container's filesystem  #查看docker容器变化
    events    Get real time events from the server#从docker服务获取容器实时事件
    exec    Run a command in a running container#在已存在的容器上运行命令
    export    Export a container's filesystem as a tar archive  #导出容器的内容流作为一个tar归档文件(对应import)
    history    Show the history of an image  #展示一个镜像形成历史
    images    List images  #列出系统当前镜像
    import    Import the contents from a tarball to create a filesystem image  #从tar包中的内容创建一个新的文件系统映像(对应export)
    info    Display system-wide information  #显示系统相关信息
    inspect    Return low-level information on a container or image  #查看容器详细信息
    kill    Kill a running container  #kill指定docker容器 
    load    Load an image from a tar archive or STDIN  #从一个tar包中加载一个镜像(对应save)
    login    Register or log in to a Docker registry#注册或者登陆一个docker源服务器
    logout    Log out from a Docker registry  #从当前Docker registry退出
    logs    Fetch the logs of a container  #输出当前容器日志信息
    pause    Pause all processes within a container#暂停容器
    port    List port mappings or a specific mapping for the CONTAINER  #查看映射端口对应的容器内部源端口
    ps    List containers  #列出容器列表
    pull    Pull an image or a repository from a registry  #从docker镜像源服务器拉取指定镜像或者库镜像
    push    Push an image or a repository to a registry  #推送指定镜像或者库镜像至docker源服务器
    rename    Rename a container  #重命名容器
    restart    Restart a running container  #重启运行的容器
    rm    Remove one or more containers  #移除一个或者多个容器
    rmi    Remove one or more images  #移除一个或多个镜像(无容器使用该镜像才可以删除，否则需要删除相关容器才可以继续或者-f强制删除)
    run    Run a command in a new container  #创建一个新的容器并运行一个命令
    save    Save an image(s) to a tar archive#保存一个镜像为一个tar包(对应load)
    search    Search the Docker Hub for images  #在docker
  hub中搜索镜像
    start    Start one or more stopped containers#启动容器
    stats    Display a live stream of container(s) resource usage statistics  #统计容器使用资源
    stop    Stop a running container  #停止容器
    tag         Tag an image into a repository  #给源中镜像打标签
    top       Display the running processes of a container #查看容器中运行的进程信息
    unpause    Unpause all processes within a container  #取消暂停容器
    version    Show the Docker version information#查看容器版本号
    wait         Block until a container stops, then print its exit code  #截取容器停止时的退出状态值

  Run 'docker COMMAND --help' for more information on a command.  #运行docker命令在帮助可以获取更多信息
  docker search  hello-docker  # 搜索hello-docker的镜像
  docker search centos # 搜索centos镜像
  docker pull hello-docker # 获取centos镜像
  docker run  hello-world   #运行一个docker镜像，产生一个容器实例（也可以通过镜像id前三位运行）
  docker image ls  # 查看本地所有镜像
  docker images  # 查看docker镜像
  docker image rmi hello-docker # 删除centos镜像
  docker ps  #列出正在运行的容器（如果创建容器中没有进程正在运行，容器就会立即停止）
  docker ps -a  # 列出所有运行过的容器记录
  docker save centos > /opt/centos.tar.gz  # 导出docker镜像至本地
  docker load < /opt/centos.tar.gz   #导入本地镜像到docker镜像库
  docker stop  `docker ps -aq`  # 停止所有正在运行的容器
  docker  rm `docker ps -aq`    # 一次性删除所有容器记录
  docker rmi  `docker images -aq`   # 一次性删除所有本地的镜像记录

|image1|


Docker 磁盘空间清理报告
===================================


**清理 Docker 未使用的资源**
--------------------------------------


  - 执行了以下命令清理未使用的资源： \ ``docker system prune``\
  - 停止的容器、未使用的镜像、未挂载的卷和未使用的网络已被删除。

  - 若要删除所有未使用的镜像（包括有标签的镜像），使用： \ ``docker system prune -a``\

**清理 Docker Build Cache**
--------------------------------------

  - 执行了以下命令清理未使用的构建缓存： \ ``docker builder prune``\
  - 已删除所有未使用的 Build Cache。

  - 为了强制清理 Build Cache，跳过确认，使用： \ ``docker builder prune -f``\

**查看 Docker 磁盘使用情况**
--------------------------------------

  - 使用以下命令查看 Docker 资源的磁盘使用情况： \ ``docker system df``\

.. |image1| image:: ./image/p01/640.png


https://www.cnblogs.com/521football/p/10483980.html