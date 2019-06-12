========================================
2. Docker Container操作
========================================

1. docker容器基本操作
===================================

启动容器

.. note::

 docker run -i-t IMAGE /bin/bash

  -i --interactive=true|fasle 默认是false
  -t --tty=true| false 默认是false
 
.. note::

 docker start container_name/container_id
 docker stop container_name/container_id
 docker restart container_name/container_id
 docker attach container_name/container_id  # 后台启动一个容器后，如果想进入到这个容器，可以使用attach命令

