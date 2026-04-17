======================================
1. linux技巧
======================================

添加系统应用图标
==================================

安装的软件需要在 GNOME/KDE 中显示图标：

创建文件：

.. code-block:: shell

   # 用户级应用菜单目录
   nano ~/.local/share/applications/android-studio.desktop
   # 系统级应用菜单目录
   sudo nano /usr/share/applications/android-studio.desktop


示例：

.. code-block:: text

   [Desktop Entry]
   Type=Application
   Name=Android Studio
   GenericName=Android IDE
   Icon=~/Applications/android-studio/bin/studio.svg
   Exec=~/Applications/android-studio/bin/studio %f
   Comment=Develop Android applications
   Categories=Development;IDE;
   Terminal=false
   StartupWMClass=jetbrains-studio

刷新桌面数据库

   GNOME/KDE 通常自动刷新，但可以手动更新：

.. code-block:: shell

   # 更新用户的应用程序数据库
   update-desktop-database ~/.local/share/applications/
   # 刷新图标主题缓存
   sudo update-icon-caches /usr/share/icons/*
   # 更新桌面应用列表
   update-desktop-database


Ubuntu 快捷键
===============================

工作区
>>>>>>>>>>>>>>>>>>>>

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - 快捷键
     - 功能
   * - **Ctrl + Alt + ↑**
     - 切换到上一个工作区
   * - **Ctrl + Alt + ↓**
     - 切换到下一个工作区
   * - **Shift + Ctrl + Alt + ↑**
     - 将窗口移动到上一个工作区
   * - **Shift + Ctrl + Alt + ↓**
     - 将窗口移动到下一个工作区


窗口管理
>>>>>>>>>>>>>>>>>>>>

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - 快捷键
     - 功能
   * - **Alt + `**
     - 在同一应用多个窗口间切换
   * - **Super + ↑**
     - 最大化窗口
   * - **Super + H**
     - 最小化窗口
   * - **Super + ↓**
     - 还原窗口
   * - **Super + A**
     - 打开应用搜索（App Launcher）
   * - **Super + Tab**
     - 切换应用
   * - **Super + D**
     - 显示桌面
   * - **Alt + F2**
     - 打开运行对话框


终端（Terminal）
>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - 快捷键
     - 功能
   * - **Ctrl + Alt + T**
     - 打开终端
   * - **Ctrl + Shift + T**
     - 新建标签页
   * - **Ctrl + Shift + W**
     - 关闭标签页
   * - **Ctrl + PageUp/PageDown**
     - 多标签切换
   * - **Ctrl + Shift + F**
     - 搜索终端内容
   * - **F11**
     - 全屏终端

文件管理器（Nautilus）
>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - 快捷键
     - 功能
   * - **Super + E**
     - 打开文件管理器（Ubuntu 有时需要自定义）
   * - **Ctrl + N**
     - 新建窗口
   * - **Ctrl + T**
     - 新建标签页
   * - **Ctrl + Tab / Ctrl + Shift + Tab**
     - 标签页切换
   * - **Alt + ← / Alt + →**
     - 返回/前进
   * - **Ctrl + H**
     - 显示隐藏文件
   * - **Ctrl + Shift + H**
     - 隐藏当前文件夹
   * - **Ctrl + Shift + N**
     - 新建文件夹
   * - **命令行执行 nautilus ~**
     - 打开当前用户的主目录

终端启动器
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

.. code-block:: bash
  
  gtk-launch jd-gui # 终端启动jd-gui


linux 使用光盘
>>>>>>>>>>>>>>>>>>>>>>>>>>>

在Ubuntu中将DVD+RW格式化为类似U盘的“数据包写入”（Packet Writing）模式，使Linux和Windows通用，需将其格式化为UDF文件系统。关键步骤是使用 dvd+rw-tools 工具进行空白化和挂载。
核心步骤

- 安装工具：打开终端，运行 sudo apt install dvd+rw-tools。
- 空白化光盘：使用命令 dvd+rw-format -force /dev/sr0（假设光驱是 /dev/sr0）清空DVD+RW。
- 格式化为UDF：使用 mkudffs 命令将光盘格式化为UDF文件系统，使其具备可读写特性。
- 挂载使用：挂载后，该光盘即可像U盘一样拖拽文件。 

详细操作指南

1. 准备工作

  确保您有空白的DVD+RW光盘和安装有 dvd+rw-tools 的Ubuntu环境。

2. 彻底抹除（空白化）DVD+RW
   
  为了确保在Windows和Linux下均能正常识别为“可写”状态，建议进行全盘格式化。

.. code-block:: bash

  # 检查设备名称，通常是 /dev/sr0
  dvd+rw-format -force /dev/sr0

3. 使用UDF格式化
  
  UDF (Universal Disk Format) 是Windows和Linux通用的文件系统，适合光盘作为“虚拟U盘”使用。

.. code-block:: bash

  # 创建UDF文件系统
  sudo mkudffs --utf8 --vid=DVD_UDF /dev/sr0 

4. 挂载并写入数据

  创建挂载点并挂载，然后即可像操作U盘一样将文件复制到该目录中。 

.. code-block:: bash

  mkdir -p /mnt/dvd
  sudo mount -t udf /dev/sr0 /mnt/dvd
  # 此时您可以将文件复制到 /mnt/dvd
  sudo umount /mnt/dvd
  sudo umount /dev/sr0 # 卸载光盘

兼容性说明

Linux：直接挂载UDF。

Windows：Windows XP及更高版本原生支持UDF格式，可直接读写。

注意事项：DVD+RW的写入速度较慢，且文件写入后如果需要再次修改，建议使用专门的封包写入软件（如Linux下的 udftools 或Windows下的Roxio/Nero）来获得更好的U盘体验。频繁读写可能会缩短光盘寿命。


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
