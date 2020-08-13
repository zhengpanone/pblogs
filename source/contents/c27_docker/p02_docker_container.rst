========================================
2. Docker Container操作
========================================


启动容器
====================

基于镜像新建一个容器并启动


# 1. 后台运行一个docker

.. note::

 docker run -i-t IMAGE /bin/bash  -c "while true;do echo 正在运行; sleep 1;done"

 # -i \-\-interactive=true|fasle 默认是false 让容器的标准输入保持打开

 # -t \-\-tty=true| false 默认是false 选项让Docker分配一个伪终端（pseudo-tty）并绑定到容器的标准输入上

 # /bin/sh  指定使用centos的bash解释器

 # -c 运行一段shell命令

 # "while true;do echo 正在运行; sleep 1;done"  在linux后台，每秒中打印一次正在运行

 # 2. 启动一个bash终端,允许用户进行交互

.. note::


 docker run --name mydocker -it centos /bin/bash  

    # \-\-name  给容器定义一个名称
    # -i  让容器的标准输入保持打开
    # -t 让Docker分配一个伪终端,并绑定到容器的标准输入上
    # /bin/bash 指定docker容器，用shell解释器交互

.. note::

 docker start container_name/container_id

 docker stop container_name/container_id    # 停止容器

 docker restart container_name/container_id
 
 docker attach container_name/container_id  # 后台启动一个容器后，如果想进入到这个容器，可以使用attach命令
 
 docker ps # 检查容器进程

 docker logs -f container_id/container_name # 不间断打印容器的日志信息

 docker exec -it container_id/container_name /bin/bash  # 进入容器交互式界面

 docker container ls -a                     # 查看容器

 docker commit 059fdea031ba  zhengpanone/centos-python  # 提交这个容器，创建新的image

 docker run -d -P training/webapp python app.py
 # -P 参数会随机映射端口到容器开放的网络端口

 docker container cp anaconda-ks.cfg container_name:/root



删除容器
==========================

.. note::

 docker container rm container_id
 
 - 清理所有处于终止状态的容器
 
 docker container prune
