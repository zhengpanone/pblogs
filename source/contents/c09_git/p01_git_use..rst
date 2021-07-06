========================
1. git 基础知识
========================

下图是git命令对仓库的影响 |image1|




- **工作区(Working Directory)**  文件夹所在的文件夹

- 版本区  文件夹中含有.git的隐藏文件夹 通过add 添加的文件被添加到暂存区 , commit 提交后, 把暂存区的内容提交到分支上。暂存区的内容提交到我们的本地仓库，又名版本库（respository），可将其理解成一个目录，该目录下的所有文件都会被 git 管理起来，每个文件的修改、删除、git 都能跟踪，以便随时追踪历史，和还原。.git 隐藏目录就是 git 的版本库，里面存了很多东西，最重要的就是 stage（index） 暂存区，还有第一个分支 master，以及指向 master 的 HEAD 指针。

   - **暂存区(Stage/Index)** 就是每次 git add 时，文件的修改存放的地方。 git commit 时就是一次性把暂存区所有修改提交到分支。

   - **本地历史仓库(Local Repository)**

   - **远程仓库(Remote Repository)**


用户配置
==========

.. code-block:: shell
 
   git config --global user.name 'zhengpanone'
   git config --global user.email "zhengpanone@hotmail.com"


配置级别

1. --local 默认，高优先级，只影响本地仓库
#. --global 中级优先级，只影响当前用户的git仓库 ~/.gitconfig
#. --system 低优先级，影响全系统的git 仓库 /etc/gitconfig


1.3 查看版本

.. code-block:: shell

   git log // 查看历史纪录
   git log --pretty = oneline // 版本ID一行显示
   git log --oneline --graph 
   git reset --hard HEAD^ // 回退到上一版本
   git reset --hard commit_id // 回退到指定ID 版本


上一个版本是HEAD^,上上一个版本HEAD^^ ,往上100可以写成HEAD~100，有时候由于回退到之前的版本，原来的版本没有显示，可以使用 

::
 
 git reflog

把两段不相干的 分支进行强行合并

.. code-block:: shell

   git pull origin master --allow-unrelated-histories

1.4 其他重要概念

- HEAD

   HEAD   就是当前活跃分支的游标，你现在在哪儿，HEAD 就指向哪儿。
   HEAD 是一个指针，总是指向当前分支。仓库版本的回退和追踪都是通过操作 HEAD 指针来完成。
   不过 HEAD 并非只能指向分支的最顶端（时间节点距今最近的那个），实际上它可以指向任何一个节点，它就是 Git 内部用来追踪当前位置的东东。

- 标签

   因为 commit id 不好找，tag 是有意义的名字，它与 commit 绑在一起。

- 其他要点

   1、每一次 git commit，都会生成一个 commit id 记录该次提交，Git 都会将它们串成一条时间线，这条时间线就是一个分支。

   2、因为创建、合并、删除分支都很快，所以 git 鼓励你使用分支完成某个任务，合并后再删除分支。过程比直接在 master 分支工作更安全，且效果一样。
   
   3、分支策略：master 分支应该是非常稳定的，仅用来发布新版本，平时不能在上面干活，干活都在 dev 分支，dev 是不稳定的，到 1.0 发布时，再将 dev 合并到 master 上，由 master 发布新版本。

linux 服务器git pull/push 时免除输入账号密码设置


进入到当前仓库执行

.. code-block:: shell

   git config --local credential.helper store

执行之后会在.git/config文件中多加[credential] helper = store

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


1.6 Git常用命令


创建新的仓库

::

 git init  # 在当前目录新建一个Git仓库
 git init [project_name]    # 新建一个目录，并将其初始化为Git仓库
 git clone [url]    #远程下载一个仓库


配置

Git的配置文件是.gitconfig，可以放在用户的主目录（全局配置）下或项目目录下（项目配置）。

::

 # 显示当前的 Git 配置
 git config --list
 # 编辑 Git 配置
 git config -e [--global]
 # 设置用来提交代码的用户信息
 git config [--global] user.name "[name]"
 git config [--global] user.email "[email address]"

添加/删除文件

::

 # 将指定文件添加到暂存区中
 git add [file1] [file2] ...
 # 将指定目录添加到暂存区中，包括子目录
 git add [dir]
 # 将当前目录中的所有文件添加到暂存区中
 git add .
 # 在添加每个更改之前都进行确认
 # 对于同一个文件的多个更改，建议分开提交
 git add -p
 # 将指定文件从工作区删除，并将本次删除添加到暂存区
 git rm [file1] [file2] ...
 # 停止追踪指定的文件，不会删除文件
 git rm --cached [file]
 # 对指定文件进行重命名，并添加到暂存区中
 git mv [file-original] [file-renamed]


代码提交相关

::

 # 将暂存区中的文件提交到代码仓库
 git commit -m [message]
 # 将指定的文件从暂存区中提交到仓库
 git commit [file1] [file2] ... -m [message]
 # 将工作区的更改直接提交到仓库
 git commit -a
 # 提交前展示所有的变动
 git commit -v
 # 使用新提交代替上次提交
 # 如果代码没有任何变动，将会用于重写上次提交的提交信息
 git commit --amend -m [message]
 # 重做上次的提交，并将指定的文件包含其中
 git commit --amend [file1] [file2] ...

分支相关

::

 # 列出本地分支
  git branch
 # 列出所有远程分支
 git branch -r
 # 列出本地和远程的所有分支
 git branch -a
 # 新建分支，并留在当前分支
 git branch [branch-name]
 # 新建分支，并切换到新分支
 git checkout -b [branch]
 # 指向某次提交新建分支
 git branch [branch] [commit]
 # 创建一个新分支，并与指定的远程分支建立跟踪关系
 git branch --track [branch] [remote-branch]
 # 切换到指定分支，并更新工作区
 git checkout [branch-name]
 # 切换到上一个分支
 git checkout -
 # 将本地分支与指定的远程分支建立跟踪关系
 git branch --set-upstream [branch] [remote-branch]
 # 合并指定分支与当前分支
 git merge [branch]
 # 将指定的提交合并到本地分支
 git cherry-pick [commit]
 # 删除分支
 git branch -d [branch-name]
 # 删除远程分支
 git push origin --delete [branch-name]
 git branch -dr [remote/branch]

标签操作

::

 # 列出所有标签
 git tag
 # 在当前提交上创建一个新标签
 git tag [tag]
 # 在指定提交上创建一个新标签
 git tag [tag] [commit]
 # 删除本地标签
 git tag -d [tag]
 # 删除远程标签
 git push origin :refs/tags/[tagName]
 # 查看标签信息
 git show [tag]
 # 提交指定标签
 git push [remote] [tag]
 # 提交所有标签
 git push [remote] --tags
 # 创建一个新分支，指向特定的标签
 git checkout -b [branch] [tag]


2.7 查看信息

::

 # 显示提交历史和每次提交的文件
  git log --stat
 # 指定关键字搜索提交历史
  git log -S [keyword]
 # 显示自某次提交以来的所有更改，一次提交显示一行。
  git log [tag] HEAD --pretty=format:%s
 # 显示自某次提交以来的所有更改，其提交描述必须符合搜索条件。
  git log [tag] HEAD --grep feature
 # 显示指定文件的提交历史
  git log --follow [file]
  git whatchanged [file]
 # 显示与指定文件相关的每个差异
  git log -p [file]
 # 显示最近 5 次提交
  git log -5 --pretty --oneline
 # 显示所有的提交用户，已提交数目多少排名
  git shortlog -sn
 # 显示指定文件何时被何人修改过
  git blame [file]
 # 显示暂存区和工作区的文件差别
  git diff
 # 显示暂存区和上一次提交的差别
  git diff --cached [file]
 # 显示工作区和当前分支的最近一次提交的差别
  git diff HEAD
 # 显示指定两次提交的差别
  git diff [first-branch]...[second-branch]
 # 显示今天提交了多少代码
  git diff --shortstat "@{0 day ago}"
 # 显示特定提交的提交信息和更改的内容
  git show [commit]
 # 新手某次提交改动了哪些文件
  git show --name-only [commit]
 # 显示某个提交的特定文件的内容
  git show [commit]:[filename]
 # 显示当前分支的最新提交
  git reflog

2.8 与远程同步

::

 # 从远程分支下载所有变动
 git fetch [remote]
 # 显示某个远程参考的信息
  git remote show [remote]
 # 新建一个远程仓库，并命名
  git remote add [shortname] [url]
 # 检索远程存储库的更改，并与本地分支合并
 git pull [remote] [branch]
 # 将本地分支提交到远程仓库
 git push [remote] [branch]
 # 将当前分支强制提交到远程仓库，即使有冲突存在
 git push [remote] --force
 # 将所有分支提交到远程仓库
 git push [remote] --all

2.9 撤销操作
 
::
 
 # 将暂存区中的指定文件还原到工作区，保留文件变动
 git checkout [file]
 # 将指定文件从某个提交还原到暂存区和工作区
 git checkout [commit] [file]
 # 将暂存区中的所有文件还原到工作区
 git checkout .
 # 重置暂存区中的指定文件，与先前的提交保持一致，但保持工作空间的变动不变
 git reset [file]
 # 重置暂存区和工作区中的指定文件，并与最近一次提交保持一致，工作空间文件变动不会保留
 git reset --hard
 # 重置暂存区，指向指定的某次提交，工作区的内容不会被覆盖
 git reset [commit]
 # 重置暂存区和工作区中的指定文件，并与指定的某次提交保持一致，工作区的内容会被覆盖
 git reset --hard [commit]
 # 将 HEAD 重置为指定的某次提交，保持暂存区和工作区的内容不变
 git reset --keep [commit]
 # 新建新提交以撤消指定的提交
 git revert [commit]
 # 暂存为提交的变动，并在稍后移动它们
 git stash
 git stash pop

1.6.10 其他

::

 # 生成用于发布的存档
 git archive


.. |image1| image:: ./image/181121.jpg
