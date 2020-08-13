========================
5. Docker 安装
========================

linux 安装docker
===========================

使用yum安装docker
>>>>>>>>>>>>>>>>>>>>>>>>

1. 查看内核版本

>>> uname -r 

Docker 要求 CentOS 系统的内核版本高于 3.10,如果你通过uname -r命令查出内核版本低于3.10的话,你的centos系统不支持docker

安装docker
>>>>>>>>>>>>>>>>>>>>>>>>


.. code-block:: shell
    :linenos:

    yum install docker -y 

    service docker start #启动docker
    service docker stop #停止docker
    service docker restart #重启docker
    systemctl start/status docker 

    docker version

设置docker开机启动
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

>>> systemctl enable docker 





Windows 安装Docker
=============================