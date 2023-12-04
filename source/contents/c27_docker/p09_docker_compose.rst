====================================
9. docker-compose
====================================


安装
=================


env_file使用
===================

env_file：用来给容器启动指定环境变量文件，相当于docker run -e参数。

*与environment区别*：

- environment指定变量

- env_file是指定到变量文件，在指定的变量文件中定义具体变量

*格式*

.. code-block:: 
   :linenos:

   # 单个变量文件
   env_file: 变量文件路径

   # 多个变量文件
   env_file:
    - 变量文件路径1
    - 变量文件路径2
    - 变量文件路径3

env_file示例：在当前目录的.env文件中设置内容如下：

.. code:: text

  JWORDPRESS_APP_DIR=./jwordpress-web

docker-compose.yml文件内容如下：

.. code-block:: yaml
  :linenos:

  jworpdress-web:
  image: registry.cn-qingdao.aliyuncs.com/shanbei/jworpdress-web:1.0.3.RELEASE
  restart: always
  container_name: jworpdress-web
  env_file:
    - .env
  volumes:
    - ${JWORDPRESS_APP_DIR}:/var/tmp/jworpdress-web
  depends_on:
    jworpdress-redis:
      condition: service_healthy
    jworpdress-mysql:
      condition: service_healthy
  links:
    - jworpdress-redis
    - jworpdress-mysql
  ports:
    - 8090:8090
  networks:
    - jwordpress




