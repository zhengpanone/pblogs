========================
22.1 jinja2基础
========================

1. 语法基础
-----------------------------------------

创建jinja_demo.py

.. code-block:: python
  :caption: jinja_demo.py

  from jinja2 import Environment,FileSystemLoader
  import os

  path = '{}/templates/'.format(os.path.dirname(__file__))

  # 创建一个加载器，jinja2会从这个目录中加载模板
  loader = FileSystemLoader(path)

  # 用加载器创建一个环境，有了它才能读取模板文件

  env = Environment(loader=loader)

  # 调用get_template()方法加载模板并返回
  template = env.get_template('demo.html')

  # 用render() 方法渲染模板
  ns = list(range(3))
  us = [{'id':1,'name':'gua'},{'id':2,'name':'瓜'}]
  template.render(name='zhengpanone',numbers=ns,users=us)



