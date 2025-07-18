=========================
3. git 常用命令
=========================

1. 修改上一个commit log
=================================

.. code-block:: bash

  git commit --amend
  # 修改编辑器中的log


2.该新建分支,不小心commit到master分支
=========================================

.. code-block:: bash

  # 以当前改动创建新分支
  git branch new-branch-name
  # 将之前的提交重置
  git reset HEAD~ --hard
  git checkout new-branch-name


3.不小心commit到错误的分支(没有push)
==========================================

.. code-block:: bash

  # 取消上一个commit,保留文件修改
  git reset HEAD~ --soft
  git stash
  # 进入正确的分支
  git checkout correct-branch
  git stash pop
  git add .
  git commit -m 'message'

.. code-block:: bash

  # 切换到正确的branch
  git checkout correct-branch
  # 将刚刚commit 扔到当前branch
  git cherry-pick master
  # reset 丢弃之前的改动
  git checkout master
  git reset HEAD~ --hard

4. git diff 没有反应
================================

git的diff 命令不会检查已放入staging区域的文件

.. code-block:: bash

  git diff --staged

5.git 出错,回到过去

.. code-block:: bash

  git reflog
  git reset HEAD@{index}


