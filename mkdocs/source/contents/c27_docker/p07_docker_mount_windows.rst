===========================================================
7. windows下安装的docker挂载window目录到docker容器
===========================================================

docker run -v f:/docker_test:/data  --privileged -itd -p 8888:22 --name centos-ssh centos:latest /usr/sbin/init

- -v 挂载本地文件夹到docker容器中f:/docker_test 表示windows下的F盘docker_test文件夹 /data 表示容器中的文件夹绝对路径