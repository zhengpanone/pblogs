=======================
Docker 安装
=======================

centos安装docker
=======================

查看内核版本
>>>>>>>>>>>>>>>>>>>>>>

```shell
uname -r 
```

Docker 要求 CentOS 系统的内核版本高于 3.10,如果你通过uname -r命令查出内核版本低于3.10的话,你的centos系统不支持docker

安装docker
>>>>>>>>>>>>>>>>>>>>>>

yum 包更新到最新
::::::::::::::::::

```shell
sudo yum update
```

安装需要的软件包
::::::::::::::::::

yum-util 提供yum-config-manager功能，另外两个是devicemapper驱动依赖的

```shell
sudo yum install -y yum-utils device-mapper-persistent-data lvm2
```



    yum install docker -y 
    
    service docker start #启动docker
    service docker stop #停止docker
    service docker restart #重启docker
    systemctl start/status docker 
    
    docker version

设置docker开机启动
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

>>> systemctl enable docker 


ubuntu安装docker
=======================

更新ubuntu的apt源索引
>>>>>>>>>>>>>>>>>>>>>>>>>>

sudo apt-get update

安装包允许apt通过HTTPS使用仓库
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common


添加Docker官方GPG key
>>>>>>>>>>>>>>>>>>>>>>>>>>


curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

设置Docker稳定版仓库
>>>>>>>>>>>>>>>>>>>>>>>>>>

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

添加仓库后，更新apt源索引
>>>>>>>>>>>>>>>>>>>>>>>>>>

sudo apt-get update

安装最新版Docker CE（社区版）
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
.. code-block:: shell

    sudo apt-get install docker-ce

检查Docker CE是否安装正确
>>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: shell

    sudo docker run hello-world

为了避免每次命令都输入sudo，可以设置用户权限，注意执行后须注销重新登录

.. code-block:: shell

    sudo usermod -a -G docker $USER

Windows 安装Docker
=============================