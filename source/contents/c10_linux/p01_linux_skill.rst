======================================
1. linux技巧
======================================

命令行日常系快捷键
===============================

.. note::

 **ctrl + u** 剪切光标前的内容

 **ctrl + k** 剪切光标至行末的内容

 **ctrl + Y** 粘贴

 **ctrl + E** 移动光标到行末

 **ctrl + A** 移动光标到行首

 **CTRL + W**  剪切光标前一个单词

 **Alt + F** 跳向下一个空格

 **Alt + B** 跳向上一个空格

 **Alt + Backspace** 删除前一个单词

 **Shift + Insert**  向终端内粘贴文本

cat 查看文件
===================

.. note::

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

.. note::

 find / -name filename 从/ 开始进入根文件系统搜索文件和目录

 **正则查找文件**

 find . -regex ".*(.txt|.pdf)$"

 -iregex: 忽略大小写的正则

 **否定参数**

 find . ! -name  "  \*.txt " -print   查找所有非txt文本

 **指定搜索深度**
 
 find . -maxdepth 1 -type f 打印当前目录的文件深度为1

 **定制搜索**

    **按类型搜索：**
    
    find . -type d -print 
    
    -type f 文件 /l 符号链接

    **按时间搜索**

    -atime  访问时间(单位是天，分钟单位是-amin)

    -mtime  修改时间(内容被修改)

    -ctime  变化时间(元数据或权限变化)

 find . -atime 7 -type f -print 最近7天被访问的所有文件

 find /usr/bin -type f -atime +100 搜索在过去100天内未被使用过的执行文件

 find /usr/bin -type f -mtime -10 搜索在10天内被创建或者修改过的文件


 find / -user username 搜索属于用户 "username" 的文件和目录

 whereis halt 显示一个二进制文件、源码或man的位置

 which halt 显示一个二进制文件或可执行文件的完整路径

 find /var/mail -size +50M -exec rm {} \; 删除大于50M的文件

 **find . -mindepth 2 -type d | xargs du -sh -t 1G | sort -h 查找当前文件夹下的文件夹，大于1G**

 -mindepth 1 声明它包含当前路径


chmod、chown、chgrp
==============================

chmod命令
>>>>>>>>>>>>>>>>>>>>

ls -lh 显示权限  

.. note::

 chmod ugo+rwx directory1 设置目录的所有人(u)、群组(g)以及其他人(o)以读（r，4 ）、写(w，2)和执行(x，1)的权限 

 chmod go-rwx directory1  删除群组(g)与其他人(o)对目录的读写执行权限

chown命令
>>>>>>>>>>>>>>>>>>

改变文件的所有者

.. note::

 chown user1 file1 改变一个文件的所有人属性 

 chown -R user1 directory1 改变一个目录的所有人属性并同时改变改目录下所有文件的属性 

 chown user1:group1 file1 改变一个文件的所有人和群组属性

chgrp命令
>>>>>>>>>>>>>>>>>>>>

改变文件所属用户组

.. note::

 chgrp group1 file1 改变文件的群组


 #找到安装的目录 find / -name ipython 

 #增加快速快捷 vim ~/.bashrc

 alias ipython3='python3 /usr/local/python37/bin/ipython'

 source ~/.bashrc

 如何配置环境变量

 vim /etc/profile

 export PATH=$PATH:/usr/local/python37/bin

 source /etc/profile
