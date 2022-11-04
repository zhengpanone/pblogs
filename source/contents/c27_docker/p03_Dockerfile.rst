===============================
3. Dockerfile指令
===============================

.. note::

 FROM <image>/FROM <image>:<tag> 已经存在的镜像,基础镜像,必须是第一条非注释指令

 MAINTAINER <name> 指定镜像的作者信息,包含镜像的所有者和联系人

 RUN 指定当前镜像构建中运行的命令
 RUN <command> (shell模式) 

   /bin/sh-c command 
   RUN echo hello

 RUN ["executable","param1","param2"] (exec模式)
 
   RUN ["/bin/bash","-c","echo hello"]

 EXPOSE <port> [<port>] 指定运行该镜像的容器使用的端口

 容器运行的默认命令,会被docker run 启动命令覆盖
 CMD  ["executable","param1","param2"] (exec模式)
 CMD command param1 param2 (shell模式)
 CMD ["param1","param2"] (作为ENTRYPOINT指令的默认参数)

 不会被docker run 启动命令覆盖
 可以使用 docker run --entrypoint覆盖ENTERYPOINT命令
 ENTERYPOINT  ["executable","param1","param2"] (exec模式)
 ENTERYPOINT command param1 param2 (shell模式)

 ADD <src>..<dest> ADD包含类似tar的解压功能,如果单纯复制文件,Docker推荐使用COPY
 
 ADD ["<src>"..."<dest>"] 适用于文件路径中有空格的情况

 COPY <src>..<dest>
 COPY ["<src>"..."<dest>"] 适用于文件路径中有空格的情况

 VOLUME ["/data"]

 WORKDIR /path/to/workdir #相当于linux的cd命令，改变目录，尽量使用绝对路径！！！不要用RUN cd

 WORKDIR /test # 如果没有就自动创建

 ENV <key><value>
 ENV <key>=<value>

 USER user:group

 ONBUILD [INSTRUCTION] 镜像触发器,当一个镜像被其他镜像作为基础镜像时执行会在构建过程中插入指令

.. code-block:: shell

   docker tag e6fasc zhengpanone/express-demo:v1.0 # 对镜像进行重命名
   docker build -t express-demo . # 指定build的image的名字为 express-demo

docker compose
============================

.. code-block:: yaml

   version: "3.8" # 指定compose版本
   services:
      express-demo-container: # 容器名称
         build: . # 容器是根据哪个镜像构建的，根据当前文件下的Dockerfile构建
         ports:
            - "3000:3000"
         volumes:
            - ./:/app:ro
            - /egg/node_module


