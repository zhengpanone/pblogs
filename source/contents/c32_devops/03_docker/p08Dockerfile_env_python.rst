====================================
定义python开发环境的Dockerfile
====================================

Dockerfile
=====================

.. literalinclude:: ./command/08.Dockerfile
    :encoding: utf-8
    :language: shell
    

构建python环境下的Docker镜像
==================================

>>> docker build -t docker-ssh:v1 $PWD

构建容器
======================================================================================

构建容器并挂载本地持久化文件目录到Docker容器中，中并指定Docker映射端口

>>> docker run -d -p 3306:3306 -p 32005:80 -p 3206:22 --name dev -v $PWD/data:/opt/data dev:v1 

