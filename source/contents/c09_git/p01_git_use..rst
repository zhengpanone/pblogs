========================
1. git 基础知识
========================

下图是git命令对仓库的影响 |image1|




- **工作区(Working Directory)**：文件夹所在的文件夹

- **版本区**：文件夹中含有.git的隐藏文件夹 通过add 添加的文件被添加到暂存区 , commit 提交后, 把暂存区的内容提交到分支上。暂存区的内容提交到我们的本地仓库，又名版本库（respository），可将其理解成一个目录，该目录下的所有文件都会被 git 管理起来，每个文件的修改、删除、git 都能跟踪，以便随时追踪历史，和还原。.git 隐藏目录就是 git 的版本库，里面存了很多东西，最重要的就是 stage（index） 暂存区，还有第一个分支 master，以及指向 master 的 HEAD 指针。

- **暂存区(Stage/Index)**：就是每次 git add 时，文件的修改存放的地方。  git commit 时就是一次性把暂存区所有修改提交到分支。

- **本地历史仓库(Local Repository)**：

- **远程仓库(Remote Repository)**：

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




用户配置
==========

.. code-block:: shell
 
   git config --global user.name 'zhengpanone'
   git config --global user.email "zhengpanone@hotmail.com"


配置级别

1. --local 默认，高优先级，只影响本地仓库
#. --global 中级优先级，只影响当前用户的git仓库 ~/.gitconfig
#. --system 低优先级，影响全系统的git 仓库 /etc/gitconfig


把两段不相干的 分支进行强行合并

.. code-block:: shell

   git pull origin master --allow-unrelated-histories


**git pull/push 时免除输入账号密码设置**

进入到当前仓库执行

.. code-block:: shell

   git config --local credential.helper store


执行之后会在.git/config文件中多加[credential] helper = store

.. code-block:: text
   :emphasize-lines: 10
   :linenos:

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



>>> cat ~/.git-credentials
https://Username:Password@github.com


1.6 Git常用命令


创建新的仓库

.. code-block:: shell
   :linenos:

   git init  # 在当前目录新建一个Git仓库
   git init [project_name]    # 新建一个目录，并将其初始化为Git仓库
   git clone [url]    #远程下载一个仓库


配置

Git的配置文件是.gitconfig，可以放在用户的主目录（全局配置）下或项目目录下（项目配置）。

.. code-block:: shell
   :emphasize-lines: 5
   :linenos:

   
   git config --list    # 显示当前的 Git 配置
   
   git config -e [--global]      # 编辑 Git 配置
   
   git config [--global] user.name "[name]"
   git config [--global] user.email "[email address]"

添加/删除文件

.. code-block:: shell
   :emphasize-lines: 5
   :linenos:

   
   git add [file1] [file2] ...   # 将指定文件添加到暂存区中
   
   git add [dir]  # 将指定目录添加到暂存区中，包括子目录
   
   git add .   # 将当前目录中的所有文件添加到暂存区中
   
   git add -p  # 在添加每个更改之前都进行确认,对于同一个文件的多个更改，建议分开提交
   
   git rm [file1] [file2] ...    # 将指定文件从工作区删除，并将本次删除添加到暂存区
   
   git rm --cached [file]  # 停止追踪指定的文件，不会删除文件
   
   git mv [file-original] [file-renamed]  # 对指定文件进行重命名，并添加到暂存区中


代码提交相关

.. code-block:: shell
   :emphasize-lines: 5
   :linenos:

   git commit [file1] [file2] ... -m [message]  # 将指定的文件从暂存区中提交到仓库
   
   git commit -a # 将工作区的更改直接提交到仓库
   
   git commit -v  # 提交前展示所有的变动
   
   git commit --amend -m [message]  # 使用新提交代替上次提交 如果代码没有任何变动，将会用于重写上次提交的提交信息
   
   git commit --amend [file1] [file2] ...  # 重做上次的提交，并将指定的文件包含其中
 
分支相关

.. code-block:: shell
   :linenos:

   
   git branch     # 列出本地分支
   
   git branch -r  # 列出所有远程分支
   
   git branch -a  # 列出本地和远程的所有分支
   
   git branch [branch-name]   # 新建分支，并留在当前分支
   
   git checkout -b [branch]   # 新建分支，并切换到新分支
   
   git branch [branch] [commit]  # 指向某次提交新建分支
   
   git branch --track [branch] [remote-branch]  # 创建一个新分支，并与指定的远程分支建立跟踪关系
   
   git checkout [branch-name]    # 切换到指定分支，并更新工作区
   
   git checkout -    # 切换到上一个分支
   
   git branch --set-upstream [branch] [remote-branch]    # 将本地分支与指定的远程分支建立跟踪关系
   
   git merge [branch]   # 合并指定分支与当前分支
   
   git cherry-pick [commit]      # 将指定的提交合并到本地分支
   
   git branch -d [branch-name]   # 删除分支
   
   git push origin --delete [branch-name]    # 删除远程分支
   git branch -dr [remote/branch]

标签操作

.. code-block:: shell
   :linenos:

   
   git tag  # 列出所有标签
   
   git tag [tag]  # 在当前提交上创建一个新标签
   
   git tag [tag] [commit]  # 在指定提交上创建一个新标签
   
   git tag -d [tag]  # 删除本地标签
   
   git push origin :refs/tags/[tagName]   # 删除远程标签
   
   git show [tag]    # 查看标签信息
   
   git push [remote] [tag]    # 提交指定标签
   
   git push [remote] --tags   # 提交所有标签
   
   git checkout -b [branch] [tag]   # 创建一个新分支，指向特定的标签


2.7 查看信息

.. code-block:: shell
   :linenos:

   
   git log --stat    # 显示提交历史和每次提交的文件
   
   git log -S [keyword]    # 指定关键字搜索提交历史
   
   git log [tag] HEAD --pretty=format:%s     # 显示自某次提交以来的所有更改，一次提交显示一行。
   
   git log [tag] HEAD --grep feature      # 显示自某次提交以来的所有更改，其提交描述必须符合搜索条件。
   
   git log --follow [file]    # 显示指定文件的提交历史
   git whatchanged [file]
   
   git log -p [file]    # 显示与指定文件相关的每个差异
   
   git log -5 --pretty --oneline    # 显示最近 5 次提交
   
   git shortlog -sn     # 显示所有的提交用户，已提交数目多少排名
   
   git blame [file]     # 显示指定文件何时被何人修改过
   
   git diff    # 显示暂存区和工作区的文件差别
   
   git diff --cached [file]      # 显示暂存区和上一次提交的差别
   
   git diff HEAD     # 显示工作区和当前分支的最近一次提交的差别
   
   git diff [first-branch]...[second-branch]    # 显示指定两次提交的差别
   
   git diff --shortstat "@{0 day ago}"    # 显示今天提交了多少代码
   
   git show [commit]    # 显示特定提交的提交信息和更改的内容
   
   git show --name-only [commit]    # 新手某次提交改动了哪些文件
   
   git show [commit]:[filename]     # 显示某个提交的特定文件的内容
   
   git reflog           # 显示当前分支的最新提交

2.8 与远程同步

.. code-block:: shell
   :linenos:

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
 
.. code-block:: shell
   :linenos:
 
   
   git checkout [file]     # 将暂存区中的指定文件还原到工作区，保留文件变动
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
   
   git revert [commit]  # 新建新提交以撤消指定的提交
   
   git stash   # 暂存为提交的变动，并在稍后移动它们
   git stash pop

1.6.10 其他

.. code-block:: shell
   :linenos:

   
   git archive    # 生成用于发布的存档





git remote 
==============

.. code-block:: shell
   :linenos:

   git remote add <name> <url> # 创建一个与远程仓库的关联关系

   git remote rm <name> # 删除别名为<name>的远程仓库的关联关系

   git remote rename <old-name> <new-name> # 将别名<old-name>的远程仓库的关联关系重命名为<new-name>

   git remote set-url <name> <url> # 直接修改远程仓库地址

查看日志
==============


.. code-block:: shell
   :linenos:

   git log # 查看历史纪录

   git log --pretty = oneline # 版本ID一行显示

   git log --oneline --graph 

   git reset --hard HEAD^ # 回退到上一版本
   
   git reset --hard commit_id # 回退到指定ID 版本

上一个版本是HEAD^,上上一个版本HEAD^^ ,往上100可以写成HEAD~100


git log
>>>>>>>>>>>>>>>

- 根据作者过滤,支持模糊搜索。

>>> git log --author="xxx"

- 根据 commit 的内容来过滤

>>> git log --grep="xxx"

- --grep 和 --author 不一样，它是支持正则的，你可以根据正则来过滤 commit message比如这样：

>>> git log --grep="Add.*runtime"

就是过滤 commit message 里有 Add 开头、中间任意个字符然后加 runtime 的 commit：

- 根据时间来过滤

>>> git log --after="2022-01-01" --before="2022-01-31"

- 根据日期来过滤

>>> git log --until="2023-11" --since="2023-01"

- 控制打印的格式

>>> git log --format="%h %as %s %an"
   
.. admonition:: format字段含义
   :class: note

   - %h 是缩写的 commit hash，
   - %as 是日期的一种格式，
   - %s 是 commit 的主题，
   - %an 是 commit 的作者。

- 给它加上一些换行，通过 %n

>>> git log --format="hash: %h %n日期: %as %n主题: %s %n作者: %an %n"

- 文字添加颜色

>>> git log --format="hash:%Cred %h %Creset%n日期: %as %n主题:%Cblue %s %Creset%n作者: %an %n"

用 %Cred %Creset 包裹来把中间字符串变红，或者 %Cblue %Creset 包裹，把中间字符串变蓝：

- 查看某个同学上一周的 commit

>>> git log --author="zhengpanone" --after="2022-01-01" --before="2022-01-07"

- 查看在所有分支的过去一周的 commit 

  加个 ``--all`` 就好了

>>> git log --author="guang" --after="2022-01-01" --before="2022-01-07" --all

- 剔除merge 的 commit

  加个 ``--no-merges``

  >>> git log --author="guang" --after="2022-01-01" --before="2022-01-07" --all --no-merges

- merges 是只保留 merge 的 commit 

  >>> git log --author="guang" --after="2022-01-01" --before="2022-01-07" --all --merges

git shortlog
>>>>>>>>>>>>>>>

按照人来分组统计，默认是按照作者名的字母顺序来排列的，也可以按照 commit 数来倒序排列

>>> git shortlog -n

- 看某段时间内，谁提交了哪些 commit

>>> git shortlog -n --after="2022-01-01" --before="2022-01-31" --all --no-merges
>>> git shortlog -n --after="2022-01-01" --before="2022-01-31" --all --no-merges --format="%h %as %s"

git reflog
>>>>>>>>>>>>>>>

git reflog 它是记录 ref 的修改历史的。

什么 ref 前面讲过了，branch、HEAD、tag 这些都是。

比如你新增了一个 commit、新建了一个 branch、新增了一个 tag、刚 pull 下来一个分支，这些都是对 ref 的修改。

git 会把它记录在 reflog 里。

总结
>>>>>>>>>>>>>>>

git 有 3 个 log 命令：git log、git shortlog、git reflog。

git log 是查看 commit 历史的，可以指定 branch、tag、某个 commit 等来查看对应的 commit 历史。

可以通过 ``--author``、``--before``、``--after``、``--grep``、``--merges``、``--no-merges``、``--all`` 来过滤某个作者、某段时间内、某个 commit 内容、非 merge 的 commit、全部分支的 commit 等 commit。

还可以通过 ``--format`` 来指定输出的颜色和格式。

git shortlog 是 git log 的统计结果，可以按照作者来分组统计。比如查看上一周每个人提交了多少个 commit。

git reflog 记录的是 ref 的变化历史，比如分支切换、reset、新的 commit 等都会记录下来。

可以通过 git reflog 命令来查看，也可以直接在 .git/logs/refs 下查看。

git stash
================

stash 命令能够将还未 commit 的代码存起来，让你的工作目录变得干净。

.. code-block:: shell
   :linenos:

   # 保存当前未commit的代码
   git stash

   # 保存当前未commit的代码并添加备注
   git stash save "备注内容"

   # 列出stash的所有记录
   git stash list

   # 删除stash的所有记录
   git stash clear

   # 应用最近一次的stash
   git stash apply

   # 应用最近一次的stash,随后删除该记录
   git stash pop

   # 删除最近一次的stash
   git stash drop


当有多条 stash，可以指定操作stash，首先使用stash list 列出所有记录：

.. code-block:: shell
   :linenos:

   $ git stash list
   stash@{0}: WIP on ...
   stash@{1}: WIP on ...
   stash@{2}: On ...

应用第二条记录：

>>> git stash apply stash@{1}

pop，drop同理


reset --soft
==================

描述
>>>>>>>>>>

完全不接触索引文件或工作树（但会像所有模式一样，将头部重置为）。这使您的所有更改的文件更改为“要提交的更改”。

回退你已提交的 commit，并将 commit 的修改内容放回到暂存区。

一般我们在使用 reset 命令时，git reset --hard会被提及的比较多，它能让 commit 记录强制回溯到某一个节点。而git reset --soft的作用正如其名，--soft(柔软的) 除了回溯节点外，还会保留节点的修改内容。

应用场景
>>>>>>>>>>>

回溯节点，为什么要保留修改内容？

应用场景1：有时候手滑不小心把不该提交的内容 commit 了，这时想改回来，只能再 commit 一次，又多一条“黑历史”。

应用场景2：规范些的团队，一般对于 commit 的内容要求职责明确，颗粒度要细，便于后续出现问题排查。本来属于两块不同功能的修改，一起 commit 上去，这种就属于不规范。这次恰好又手滑了，一次性 commit 上去。

命令使用
>>>>>>>>>>>

学会reset --soft之后，你只需要：

.. code-block:: shell
   :linenos:

   # 恢复最近一次 commit
   git reset --soft HEAD^

reset --soft相当于后悔药，给你重新改过的机会。对于上面的场景，就可以再次修改重新提交，保持干净的 commit 记录。

以上说的是还未 push 的commit。对于已经 push 的 commit，也可以使用该命令，不过再次 push 时，由于远程分支和本地分支有差异，需要强制推送git push -f来覆盖被 reset 的 commit。

还有一点需要注意，在reset --soft指定 commit 号时，会将该 commit 到最近一次 commit 的所有修改内容全部恢复，而不是只针对该 commit。

举个例子：

commit 记录有 c、b、a。

|image2|

reset 到 a。

.. code-block:: shell
   :linenos:

   git reset --soft 1a900ac29eba73ce817bf959f82ffcb0bfa38f75

此时的 HEAD 到了 a，而 b、c 的修改内容都回到了暂存区。

|image3|

cherry-pick
=================

描述
>>>>>>>>>>>>>

给定一个或多个现有提交，应用每个提交引入的更改，为每个提交记录一个新的提交。这需要您的工作树清洁（没有从头提交的修改）。

将已经提交的 commit，复制出新的 commit 应用到分支里

应用场景
>>>>>>>>>>>>>>

commit 都提交了，为什么还要复制新的出来？

应用场景1：有时候版本的一些优化需求开发到一半，可能其中某一个开发完的需求要临时上，或者某些原因导致待开发的需求卡住了已开发完成的需求上线。这时候就需要把 commit 抽出来，单独处理。

应用场景2：有时候开发分支中的代码记录被污染了，导致开发分支合到线上分支有问题，这时就需要拉一条干净的开发分支，再从旧的开发分支中，把 commit 复制到新分支。

命令使用
>>>>>>>>>>>>>>>

复制单个
:::::::::::::


现在有一条feature分支，commit 记录如下：
|image4|

需要把 b 复制到另一个分支，首先把 commitHash 复制下来，然后切到 master 分支。
|image5|

当前 master 最新的记录是 a，使用cherry-pick把 b 应用到当前分支。
|image6|

完成后看下最新的 log，b 已经应用到 master，作为最新的 commit 了。可以看到 commitHash 和之前的不一样，但是提交时间还是保留之前的。

复制多个
:::::::::::

以上是单个 commit 的复制，下面再来看看 cherry-pick 多个 commit 要如何操作。

一次转移多个提交：

.. code-block:: shell
   :linenos:

   git cherry-pick commit1 commit2

上面的命令将 commit1 和 commit2 两个提交应用到当前分支。

多个连续的commit，也可区间复制：

.. code-block:: shell
   :linenos:

   git cherry-pick commit1^..commit2

上面的命令将 commit1 到 commit2 这个区间的 commit 都应用到当前分支（包含commit1、commit2），commit1 是最早的提交。

cherry-pick 代码冲突
:::::::::::::::::::::

在cherry-pick多个commit时，可能会遇到代码冲突，这时cherry-pick会停下来，让用户决定如何继续操作。下面看看怎么解决这种场景。
|image7|

还是 feature 分支，现在需要把 c、d、e 都复制到 master 分支上。先把起点c和终点e的 commitHash 记下来。
|image8|

切到 master 分支，使用区间的cherry-pick。可以看到 c 被成功复制，当进行到 d 时，发现代码冲突，cherry-pick中断了。这时需要解决代码冲突，重新提交到暂存区。
|image9|

然后使用cherry-pick --continue让cherry-pick继续进行下去。最后 e 也被复制进来，整个流程就完成了。

以上是完整的流程，但有时候可能需要在代码冲突后，放弃或者退出流程：

放弃 cherry-pick：

.. code-block:: shell
   :linenos:

   git cherry-pick --abort

回到操作前的样子，就像什么都没发生过。

退出 cherry-pick：

.. code-block:: shell
   :linenos:

   git cherry-pick --quit

不回到操作前的样子。即保留已经cherry-pick成功的 commit，并退出cherry-pick流程。

revert
==============

https://mp.weixin.qq.com/s/4IpF72UxPun02HcpTJl2lw





.. |image1| image:: ./image/181121.jpg
.. |image2| image:: ./image/640.png
.. |image3| image:: ./image/641.png
.. |image4| image:: ./image/642.png
.. |image5| image:: ./image/643.png
.. |image6| image:: ./image/644.png
.. |image7| image:: ./image/645.png
.. |image8| image:: ./image/646.png
.. |image9| image:: ./image/647.png