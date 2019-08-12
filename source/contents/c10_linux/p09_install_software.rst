================================
9. 安装软件
================================

非root用户安装rpm包
============================

以wkhtmltopdf工具为例

1. wget 下载 rpm包 wget https://downloads.wkhtmltopdf.org/0.12/0.12.5/wkhtmltox-0.12.5-1.centos7.x86_64.rpm   yum 下载 yum downloader wkhtmltopdf

#. 解压 rpm2cpio wkhtmltox-0.12.5-1.centos7.x86_64.rpm |cpio -idvm

#. 会生成‘usr’目录，可以修改一下名字：mv usr wkhtmltopdf

#. 将可执行文件的目录加入到bashrc中：在这里插入图片描述

#. 测试 wkhtmltopdf --help