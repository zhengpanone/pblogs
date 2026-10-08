=======================
Docker 安装
=======================

centos安装docker
=======================

查看内核版本
>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: shell

    uname -r 

Docker 要求 CentOS 系统的内核版本高于 3.10,如果你通过uname -r命令查出内核版本低于3.10的话,你的centos系统不支持docker

安装docker
>>>>>>>>>>>>>>>>>>>>>>

yum 包更新到最新
::::::::::::::::::

.. code-block:: shell

    sudo yum update

安装需要的软件包
::::::::::::::::::

yum-util 提供yum-config-manager功能，另外两个是devicemapper驱动依赖的

.. code-block:: shell

    sudo yum install -y yum-utils device-mapper-persistent-data lvm2

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


Linux 离线安装 Docker
=====================

适用环境
>>>>>>>>>>>>>>>>>>>>>>
- 操作系统：CentOS 7 / CentOS 8
- 架构：x86_64
- 网络环境：无外网连接

前置依赖
>>>>>>>>>>>>>>>>>>>>>>
Docker 二进制运行依赖以下系统组件，请在离线服务器上提前确认或安装：

- libseccomp
- libcgroup
- iptables
- xz

可通过 CentOS 安装 ISO 或本地 yum 缓存安装：

.. code-block:: bash

    yum install -y libseccomp libcgroup iptables xz

下载与传输
>>>>>>>>>>>>>>>>>>>>>>

1. 在 **有网络的电脑** 上访问 Docker 官方二进制下载页：

   https://download.docker.com/linux/static/stable/x86_64/

2. 下载对应版本的 docker-<version>.tgz 文件（推荐使用 20.10.x 或 23.x 稳定版）。

3. 通过 U 盘或 FTP 将安装包上传至目标 CentOS 服务器。

安装步骤
>>>>>>>>>>>>>>>>>>>>>>

解压安装包
::::::::::::::::::

.. code-block:: bash

    tar -zxvf docker-*.tgz

移动可执行文件
::::::::::::::::::

将解压后的二进制文件复制到系统路径：

.. code-block:: bash

    cp docker/* /usr/bin/

创建 systemd 服务文件
:::::::::::::::::::::::::

创建并编辑 /etc/systemd/system/docker.service，写入以下内容：

.. code-block:: ini

    [Unit]
    Description=Docker Application Container Engine
    After=network-online.target firewalld.service
    Wants=network-online.target

    [Service]
    Type=notify
    ExecStart=/usr/bin/dockerd -H unix:///var/run/docker.sock
    ExecReload=/bin/kill -s HUP $MAINPID
    LimitNOFILE=infinity
    LimitNPROC=infinity
    LimitCORE=infinity
    Delegate=yes
    KillMode=process
    Restart=on-failure
    StartLimitBurst=3
    StartLimitInterval=60s

    [Install]
    WantedBy=multi-user.target

.. note::
    上述配置仅启用本地 Unix Socket，不开放远程 TCP 端口，适用于离线单机环境。
    如需远程管理 Docker，请另行配置 TLS 证书。

启动与验证
>>>>>>>>>>>>>>>>>>>>>>

赋予服务文件执行权限
:::::::::::::::::::::

.. code-block:: bash

    chmod +x /etc/systemd/system/docker.service

重载 systemd 配置
::::::::::::::::::

.. code-block:: bash

    systemctl daemon-reload

启动 Docker 并设置开机自启
:::::::::::::::::::::::::::::
.. code-block:: bash

    systemctl start docker
    systemctl enable docker

验证安装
::::::::::::::::::

检查 Docker 版本和服务状态：

.. code-block:: bash

    docker -v
    systemctl status docker

运行测试容器（可选）：

.. code-block:: bash

    docker run --rm hello-world

常见问题
>>>>>>>>>>>>>>>

- 启动失败：检查 libseccomp 和 cgroup 是否已安装。
- docker 命令无权限：将当前用户加入 docker 组：

  .. code-block:: bash

      groupadd docker
      usermod -aG docker $USER

- 容器无法联网：离线环境属正常现象，如需使用需配置内部镜像仓库。