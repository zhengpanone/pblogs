========================
1.1 git 基础知识
========================

1.1 名词解释

1 工作区  文件夹所在的文件夹
2 版本区  文件夹中含有.git的隐藏文件夹 通过add 添加的文件被添加到暂存区 , commit 提交后, 把暂存区的内容提交到分支上

..  image:: ../../image/git_image/Image.png
    :align: center
    :alt: git strucer

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


