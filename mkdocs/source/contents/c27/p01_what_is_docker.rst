========================================
Docker
========================================

1.组成
=================

Docker组成：Docker Client 和 Docker Server

Docker组件：镜像（Image）、容器（Container）、仓库（Repository）

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






