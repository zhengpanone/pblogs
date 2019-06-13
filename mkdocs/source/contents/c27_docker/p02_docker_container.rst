========================================
2. Docker Container操作
========================================

1. docker容器基本操作
===================================

启动容器

.. note::

 docker run -i-t IMAGE /bin/bash

 -i --interactive=true|fasle 默认是false 让容器的标准输入保持打开

 -t --tty=true| false 默认是false 选项让Docker分配一个伪终端（pseudo-tty）并绑定到容器的标准输入上
 
.. note::

 docker start container_name/container_id

 docker stop container_name/container_id

 docker restart container_name/container_id
 
 docker attach container_name/container_id  # 后台启动一个容器后，如果想进入到这个容器，可以使用attach命令

删除容器
==========================

.. note::

 docker container rm container_id
 
 - 清理所有处于终止状态的容器
 docker container prune
