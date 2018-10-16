========================
1.1 git 基础知识
========================

1.1 名词解释

1 工作区  文件夹所在的文件夹
2 版本区  文件夹中含有.git的隐藏文件夹 通过add 添加的文件被添加到暂存区 , commit 提交后, 把暂存区的内容提交到分支上

..  image:: ../../image/git_image/Image.png
    :align: center
    :alt: git strucer

1.2 用户配置

::
 git config --global user.name 'zhengpanone'
 git config --global user.email "zhengpanone@hotmail.com"

配置级别

--local 默认，高优先级，只影响本地仓库
--global 中级优先级，只影响当前用户的git仓库 ~/.gitconfig
--system 低优先级，影响全系统的git 仓库 /etc/gitconfig

1.3 初始化仓库

第一步 使用git add <file> 或者 git add --all
第二步 使用命令 git commit -m 'git something'  ，完成

1.4 版本回退
    每次commit 作为一次快照

::
 git log // 查看历史纪录
 git log --pretty = oneline // 版本ID一行显示
 git reset --hard HEAD^ // 回退到上一版本
 git reset --hard commit_id // 回退到指定ID 版本

上一个版本是HEAD^,上上一个版本HEAD^^ ,往上100可以写成HEAD~100，有时候由于回退到之前的版本，原来的版本没有显示，可以使用 

::
 
 git reflog


1.2 linux 服务器git pull/push 时免除输入账号密码设置

1.2.1设置当前仓库
进入到当前仓库执行

::

 git config --local credential.helper store
 2、执行之后会在.git/config文件中多加[credential] helper = store

 ::

 [core]
    repositoryformatversion = 0
    filemode = true
    bare = false
    logallrefupdates = true
 [remote "origin"]
    url = https://github.com/zhengpanone/blogs.git
    fetch = +refs/heads/*:refs/remotes/origin/*
 [credential]
    helper = store

执行git pull命令，会提示输入账号密码。输完这一次以后就不再需要，并且会在家目录生成一个.git-credentials文件

::

 cat ~/.git-credentials
 >>> https://Username:Password@github.com


