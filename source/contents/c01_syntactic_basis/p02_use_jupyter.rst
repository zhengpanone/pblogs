jupyter 安装和使用
========================================

安装jupyter
>>>>>>>>>>>>>>>>>>>>>>>>

>>> python -m pip install jupyter # or pip install jupyter

生成配置文件
------------------

>>> jupyter notebook --generate-config

生成密码，修改配置文件
-----------------------

>>> from notebook.auth import passwd
>>> passwd()
>>> 'sha1::f0ee0120748a:b4a02027221abc4d128dca3058ab3b0bc7a9102'

# 修改默认配置文件
----------------------- 

~/.jupyter/jupyter_notebook_config.py

.. code-block:: python
  
  c.NotebookApp.ip='0.0.0.0'  / "*"  #允许任何客户端ip访问

  c.NotebookApp.password = u'sha1:f9030dd55bce:75fd7bbaba41be6ff5ac2e811b62354ab55b1f63' 

  c.NotebookApp.open_browser = False #默认不打开浏览器
  
  c.NotebookApp.port =8888  # 客户端访问jupyter服务器的端口号

启动jupyter
-------------------

>>> jupyter notebook

魔法命令
>>>>>>>>>>>>>>>

系统与 Shell
------------------

.. code-block:: shell

  # 系统与 Shell
  !ls、!pip install pandas
  %cd ../data
  %pwd
  %env、%env MY_VAR=123
  %set_env、%set_env PATH=/usr/bin:$PATH
  %pip freeze > requirements.txt

  # 可视化
  %matplotlib inline    # matplotlib 图像直接嵌入笔记本（最常用）
  %matplotlib widget    # 交互式 matplotlib 图表（需 ipympl）

  # 文件与代码
  %run my_script.py
  %load utils.py        # 将外部文件内容加载到当前单元格
  %%writefile hello.py  # 将单元格内容写入文件
  %pycat config.yaml    # 在分页器中查看文件内容

  # 调试与探查
  %debug                # 进入上一次异常的调试器
  %pdb                  # 自动开启/关闭事后调试（on/off）
  %who                  # 列出当前命名空间中的变量
  %whos                 # 详细显示变量名、类型、值
  %reset                # 清空所有变量（会提示确认）
  ?obj / %pinfo obj     # 查看对象文档

  # 笔记本自身
  %history              # 显示命令历史
  %save                 # 将历史命令保存到文件
  %notebook             # 导出当前笔记本为 .ipynb
  %load_ext             # 加载扩展
  %reload_ext           # 重新加载扩展

.. note::

  %pip install pandas   # 装到当前内核对应的环境

  !pip install pandas   # 可能装到系统 Python，重启内核后 import 不到

远程服务器部署
>>>>>>>>>>>>>>>>>>>>>>>>

服务器跑 Jupyter，本地浏览器访问

.. code-block:: shell

  # 服务器端
  jupyter lab --no-browser --port=8888 --ip=0.0.0.0

本地用 SSH 隧道转发：

.. code-block:: shell

  ssh -N -L 8888:localhost:8888 user@server_ip

然后本地浏览器打开 http://localhost:8888，token 在服务器启动日志里。

进阶：用密码替代 token

.. code-block:: shell

  jupyter lab password   # 设置密码，之后登录不用每次复制 token

后台持久运行（防止 SSH 断开后进程被杀）

.. code-block:: shell

  # 用 tmux / screen 包裹
  tmux new -s jupyter
  jupyter lab --no-browser --port=8888
  # Ctrl+B D  detach，下次 tmux attach -t jupyter 回来



