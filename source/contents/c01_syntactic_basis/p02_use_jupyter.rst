========================================
2. jupyter 安装和使用
========================================

安装jupyter
-------------------

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

.. code-block:: text
  :linenos:

  c.NotebookApp.ip='0.0.0.0'  / "*"  #允许任何客户端ip访问

  c.NotebookApp.password = u'sha1:f9030dd55bce:75fd7bbaba41be6ff5ac2e811b62354ab55b1f63' 

  c.NotebookApp.open_browser = False #默认不打开浏览器
  
  c.NotebookApp.port =8888  # 客户端访问jupyter服务器的端口号

启动jupyter
-------------------

>>> jupyter notebook






