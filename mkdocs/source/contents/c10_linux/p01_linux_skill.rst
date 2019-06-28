======================================
1. linux技巧
======================================


**ctrl + u ** 删除从开头到光标处的命令文本
**ctrl + k ** 删除从光标到结尾处的命令文本

cat 查看文件
===================

cat filename 从第一个字节开始正向查看文件内容
tac filename 从最后一个字节反向查看文件内容
cat -n filename 标示文件的行数
more filename 查看一个长文件
head -n 2 filename 查看一个文件的前两行
tail -n 2 filename 查看一个文件的最后两行
tail -n +1000 filename 从1000行开始显示1000行以后的内容
cat filename | head -n 3000 | tail -n +1000 显示1000到3000行
cat filename | tail -n +3000 | head -n 1000 从3000行开始显示1000行（即显示3000~3999行）

cat /etc/redhat-release # 查看操作系统版本

find 查找文件
===============================

find / -name filename 从/ 开始进入根文件系统搜索文件和目录 # #找到安装的目录 find / -name ipython 

.. note::
 
 #增加快速快捷 vim ~/.bashrc

 alias ipython3='python3 /usr/local/python37/bin/ipython'

 source ~/.bashrc

 如何配置环境变量

 vim /etc/profile

 export PATH=$PATH:/usr/local/python37/bin

 source /etc/profile

find / -user username 搜索属于用户 "username" 的文件和目录

find /usr/bin -type f -atime +100 搜索在过去100天内未被使用过的执行文件

find /usr/bin -type f -mtime -10 搜索在10天内被创建或者修改过的文件

whereis halt 显示一个二进制文件、源码或man的位置

which halt 显示一个二进制文件或可执行文件的完整路径

find /var/mail -size +50M -exec rm {} \; 删除大于50M的文件

chmod、chown、chgrp
==============================

chmod命令
>>>>>>>>>>>>>>>>>>>>

ls -lh 显示权限 
chmod ugo+rwx directory1 设置目录的所有人(u)、群组(g)以及其他人(o)以读（r，4 ）、写(w，2)和执行(x，1)的权限 

chmod go-rwx directory1  删除群组(g)与其他人(o)对目录的读写执行权限

chown命令
>>>>>>>>>>>>>>>>>>


（改变文件的所有者）
chown user1 file1 改变一个文件的所有人属性 

chown -R user1 directory1 改变一个目录的所有人属性并同时改变改目录下所有文件的属性 

chown user1:group1 file1 改变一个文件的所有人和群组属性

chgrp命令
>>>>>>>>>>>>>>>>>>>>

（改变文件所属用户组）
chgrp group1 file1 改变文件的群组