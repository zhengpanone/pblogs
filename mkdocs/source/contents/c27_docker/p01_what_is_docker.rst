========================================
1. Docker 基本概念
========================================

1.组成
=================

Docker组成：Docker Client 和 Docker Server

Docker组件：
- 镜像（Image）
- 容器（Container）
- 仓库（Repository）


容器
============================

容器（Container）：容器是一种轻量级、可移植、并将应用程序进行的打包的技术，使应用程序可以在几乎任何地方以相同的方式运行，Docker将镜像文件运行起来后，产生的对象就是容器。容器相当于是镜像运行起来的一个实例且容器具备一定的生命周期。

Docker容器和虚拟机的区别
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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
======================================

|image1|


容器创建(docker create)
=================================

命令格式：
docker run [参数] 镜像 [容器执行命令] [执行命令提供的参数]

常用参数：
# -t 分配一个虚拟终端

# -i 保持输入打开

# -d 容器后台运行，并打印容器id

# -rm 容器结束后自动删除容器


推荐使用 docker run -dti 来启动所需容器。

2.使用场景
=========================

1. Simplifying Configuration(简化配置)
#. Developer Productivity(简化开发环境)
#. Server Consolidation(应用隔离)
#. Multi-tenancy(多用户)
#. Code Pipeline Management(快速部署)
#. App Isolation(应用隔离)
#. Debugging Capabilities(开发调试)
#. Repid Deployment(交付方式改变)


docker 基本使用
==============================

::

 docker version # 查看Docker版本

 docker search centos #查看搜索镜像

 docker pull centos:latest # 下载镜像

 docker images # 查看当前系统中的images信息

 docker run -it centos:latest  #运行docker容器

 winpty docker run -it zhengpanone/centos-python  # **在windows下使用git bash 使用**

 docker ps -a # 查看docker容器中运行的容器

 docker commit -m '' CONTAINER ID IMAGE  # 将容器转化为一个镜像

 docker commit -m "安装 net-tools" -a 'zhengpanone'  5301d7c9bc21 zhengpanone/centos-python:V1
 # -m 指定说明信息; 
 # -a 指定用户信息 ;5301d7c9bc21代表容器id; 
 zhengpanone/centos-python:V1指定目标镜像的用户名、仓库名和tag信息

 docker rmi -f d0049ff7d6d7 #删除docker容器 docker rmi image_name/image_id

 docker rm container_name/container_id # 删除docker容器

 docker save -o ./centos.tar zhengpanone/centos:git # 保存镜像 -o/--output

 docker load -i ./centos.tar # 加载镜像 -i/--input 

利用Dockerfile创建镜像
Dockerfile可以理解为一种配置文件,用来告诉docker build命令应该执行那些操作。
一个简易的Dockerfile文件如下所示

::

 # 说明该镜像以那个镜像为基础
 FROM centos:latest 

 # 构建者的基本信息
 MAINTAINER zhengpanone 

 # 在build 这个镜像时执行的操作
 RUN yum update
 RUN yum install -y git

有了Dockerfile 利用build命令构建镜像

::
 
 docker build -f ./Dockerfile  -t "zhengpanone/centos-git:gitdir" .

Docker 基础命令
======================================

.. code::

 
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

.. |image1| image:: ./image/640.webp