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

 ADD

 COPY

 VOLUME

 WORKDIR

 ENV

 USER

 ONBUILD



