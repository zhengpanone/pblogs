========================================
3. Python虚拟环境
========================================

pip
===============

查询软件包
>>>>>>>>>>>>>>

查询当前环境安装的所有软件包

>>> pip list

查询pypi上含有某个名字的包

>>> pip search pkg 

查询当前环境中可升级的包

>>> pip list --outdated

查询一个包的详细内容

>>> pip show pkg

下载软件包
>>>>>>>>>>>>>>>>>>>>

不安装软件包的情况下载软件到本地

>>> pip download --destination-directory /local/wheels -r requirements.txt 

指定目录中安装软件包,不从pypi上安装

>>> pip install --no-index --find-links=/local/wheels -r requirements.txt 

从下载的包中,自己构建生成wheel文件

>>> pip install wheel
>>> pip wheel --wheel-dir=/local/wheels -r requirements.txt

安装软件
>>>>>>>>>>>>>>>>>

.. code-block:: shell
   :linenos: 

   # 下载非二进制的包
   pip download --no-binary=:all: pkg 

   # 安装非二进制的包
   pip install pkg --no-binary


安装用户私有软件包
>>>>>>>>>>>>>>>>>>>>

>>> pip install --user pkg


升级软件包
>>>>>>>>>>>>>

>>> pip install --upgrade pkg 


Virtualenv、Virtualenvwrapper、Pyenv、

Virtualenv 
============================

::

 virtualenv -p /usr/bin/python3/bin/python3 venv 
 source /venv/bin/active
 deactivate
 
Virtualenvwrapper 
=============================

::

 pip install virtualenvrapper 
 # 配置.barshrc 
 export WORKON_HOME=$HOME/.virtualenvs  # 指定目录
 export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python
 export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages' # 隔离系统site-packages 
 export PIP_VIRTUALENV_BASE=$WORKON_HOME
 export PIP_RESPECT_VIRTUALENV=true
 if [[ -r /usr/local/bin/virtualenvwrapper.sh ]]; then
    source /usr/local/bin/virtualenvwrapper.sh
 else
    echo "WARNING: Can't find virtualenvwrapper.sh"
 fi 

 # 创建使用虚拟环境
 mkvirtualenv your_project #创建
 rmvitualenv your_project #删除
 workon  # 列出项目
 workon your_project # 进去某个项目

Pyenv 
==============================

::

 pip install pyenv 
 pip install pyenv-virtualenv 
 pip install pyenv-virtualenvwrapper 

 # 配置.barshrc 
 # ---pyenv---
 export PATH="$HOME/.pyenv/bin:$PATH"
 eval "$(pyenv init -)"
 eval "$(pyenv virtualenv-init -)"

 # pyenv 使用方式
 pyenv install -l # 获取安装列表
 pyenv install 3.7.1 # 安装python3.7
 pyenv global 3.7.1 # 设置全局python
 pyenv virtualenv test-pyenv-venv # 创建虚拟包
 pyenv activate test-pyenv-venv # 进入虚拟环境
 pyenv deactivate  # 退出

pipenv 
===============================

安装pipenv
-------------------

::

 pip install pipenv

 pip install pipenv --user [username] 
 # -user 指定将pipenv 安装在该用户主目录下

 # 创建虚拟环境

 cd project1
 pipenv install

 # pipenv install 是安装已经提供的包并将它们加入到Pipfile中（Pipfile是python包依赖文件，列出了项目中所有包的依赖，这是pipenv相当大的创新，对应的是Pipfile.lock文件）(Pipfile和Pipfile.lock两个文件互相配合，完成虚拟环境的管理工作。)，这里同时创建了项目的虚拟环境。


pipenv install的时候有三种逻辑：

 - 如果目录下没有Pipfile和Pipfile.lock文件，表示创建一个新的虚拟环境；
 - 如果有，表示使用已有的Pipfile和Pipfile.lock文件中的配置创建一个虚拟环境；
 - 如果后面带诸如django这一类库名，表示为当前虚拟环境安装第三方库。

::

 # 激活虚拟环境
 pipenv shell
 # 退出虚拟环境
 exit
 # 安装和卸载第三方库
 pipenv install flask
 pipenv uninstall flask

管理开发环境

::

 # 通常有一些Python包只在你的开发环境中需要，而不是在生产环境中，例如单元测试包。 Pipenv使用--dev标志区分两个环境(开发和生产)。
 pipenv install --dev django
 # django库现在将只在开发虚拟环境中使用。如果要在你的生产环境中使用下面命令安装已有的项目：
 pipenv install 

 #该命令执行后项目中并不会安装django包。另外，如果开发人员将你的项目克隆到自己的开发环境中，他们可以使用--dev标志，将django也安装：
 pipenv install --dev
 # --dev参数，帮你在同一个虚拟环境中又区分出了开发和非开发环境
 
 #pipenv虚拟环境运行python命令
 pipenv run python your_script.py

pipenv 具有下列的选项：

.. code-block:: shell
   :linenos:

   pipenv
   Usage: pipenv [OPTIONS] COMMAND [ARGS]...

   Options:
   --update         更新Pipenv & pip
   --where          显示项目文件所在路径
   --venv           显示虚拟环境实际文件所在路径
   --py             显示虚拟环境Python解释器所在路径
   --envs           显示虚拟环境的选项变量
   --rm             删除虚拟环境
   --bare           最小化输出
   --completion     完整输出
   --man            显示帮助页面
   --three / --two  使用Python 3/2创建虚拟环境（注意本机已安装的Python版本）
   --python TEXT    指定某个Python版本作为虚拟环境的安装源
   --site-packages  附带安装原Python解释器中的第三方库
   --jumbotron      不知道啥玩意....
   --version        版本信息
   -h, --help       帮助信息

pipenv 可使用的命令参数：

::

 Commands:
  check      检查安全漏洞
  graph      显示当前依赖关系图信息
  install    安装虚拟环境或者第三方库
  lock       锁定并生成Pipfile.lock文件
  open       在编辑器中查看一个库
  run        在虚拟环境中运行命令
  shell      进入虚拟环境
  uninstall  卸载一个库
  update     卸载当前所有的包，并安装它们的最新版本







