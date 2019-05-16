========================================
Docker
========================================

1.组成
=================

Docker组成：Docker Client 和 Docker Server

Docker组件：镜像（Image）、容器（Container）、仓库（Repository）


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
 -t 分配一个虚拟终端
 -i 保持输入打开
 -d 容器后台运行，并打印容器id
 --rm 容器结束后自动删除容器


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
 # -m 指定说明信息; -a 指定用户信息 ;5301d7c9bc21代表容器id; zhengpanone/centos-python:V1指定目标镜像的用户名、仓库名和tag信息
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






.. |image1| image:: ./image/640.webp