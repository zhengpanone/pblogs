# 11. Docker Use Centos


在docker下使用centos7容器来学习linux的时候，遇到了采用yum安装好的man-pages无法使用的问题。

## 解决方法


vim /etc/yum.conf 将 tsflags=nodocs 这一行删除或注释掉。
重启docker中的centos7容器（不一定需要这一步）
运行命令yum -y install man-pages安装，此时就会发现man命令可用了

## 原因分析
根据stackoverflow上的回答，我看了下docker Hub中centos仓库的说明文件，其中有这样一段：


    By default, the CentOS containers are built using yum's nodocs option, which helps reduce the size of the image. If you install a package and discover files missing, please comment out the line tsflags=nodocs in /etc/yum.conf and reinstall your package.

意思是为了减少镜像文件的大小，所以开启了yum的nodocs选项，如果你发现文档不可用，就请注释掉/etc/yum.conf中的这个选项，并重安装包。
