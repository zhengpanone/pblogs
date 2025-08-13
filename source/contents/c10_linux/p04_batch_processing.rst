====================================
4. Linux批量处理任务
====================================

.. code-block:: shell
   
  for tar in *.tar.gz; 
    do 
    tar xvf $tar; 
    done

  for sh in *.sh; 
    do 
    sh $sh; 
  done

用tar命令批量解压某个文件夹下所有的tar.gz文件

.. code-block:: shell
   
  ls *.tar.gz | xargs -n1 tar xzvf

解压当前目录下的所有bz2文件，maxdepth表示搜索深度，1代表只搜索当前目录

.. code-block:: shell
  
  find -maxdepth 1 -name “*.bz2″|xargs -i tar xvjf {}

.. note:: 
   
  for i in $(ls \*.tar);do tar xvf $i;done

批量修改文件内容
=========================

.. code-block:: shell

  for i in ls *.sh;
  do
    perl -p -i -e "s/-t 4/-t 1/g" $i;
  done


在当前目录下的.c文件中把字符串"password"替换成"pwd"并以.bak扩展名备份

.. code-block:: shell
   
  perl -pi.bak -e 's/password/pwd/g' *.c

.. note::

  -a  自动分隔模式，用空格分隔$_并保存到@F中。相当于@F = split ”。分隔符可以使用-F参数指定

  -F  指定-a的分隔符，可以使用正则表达式

  -e  执行指定的脚本。

  -i<扩展名>   原地替换文件，并将旧文件用指定的扩展名备份。不指定扩展名则不备份。

  -l    对输入内容自动chomp，对输出内容自动添加换行

  -n    自动循环，相当于 while(<>) { 脚本; }

  -p    自动循环+自动输出，相当于 while(<>) { 脚本; print; }

.. code-block:: shell
   
  for i in ls *.sh;
  do
    sed -i "s/-t 4/-t 1/g" $i;
  done

.. note::

  -i 表示inplace edit，就地修改文件

  -r 表示搜索子目录

  -l 表示输出匹配的文件名

  s表示替换，d表示删除