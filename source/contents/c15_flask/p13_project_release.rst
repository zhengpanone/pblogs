=============================================
15.13 uwsgi + ngix 发布项目
=============================================

1. uwsgi 安装
===================================

::

 pip install uwsgi

2. uwsgi 测试
==================================

创建test.py 
>>>>>>>>>>>>>>>>>>>>>>>>>>>

::

 # coding=utf-8
 from flask import Flask
 app = Flask(__name__)

 @app.route('/')
 def index():
    return "Hello World!"

 if __name__ == "__main__":
   app.run(host="0.0.0.0",port=8080,debug=True)

编写uwsgi_config.ini 文件
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

::

 [uwsgi]
 socket = 127.0.0.1:5000   # uwsgi 进行socket通信的端口
 processes = 4
 threads = 2
 master = true
 pythonpath = /opt/work/test   # 当前应用程序的项目路径
 module = test # 需要托管的主程序文件名
 callable = app   # uwsgi需要调用的应用程序,在程序中是 app = Flask(__name__)
 memory-report = true

执行命令
>>>>>>>>>>>>>>>>>>>>>>>>

::

 uwsgi --http :5000 --ini uwsgi_conf.ini -d ./uwsgi.log --pidfile=uwsgi.pid 

-  –http指定用5800端口启动http协议
-  –ini 指定上述的启动配置文件
-  -d指定uwsgi的log，方便我们调试
-  –pidfile将启动的进程号写到uwsgi.pid文件中，方便我们在需要停止服务器时kill掉


启动后查看uwsgi.log，如果一切正常，就在浏览器内访问: http://127.0.0.1:5800会输出hello world,表明此时uwsgi工作正常。

再以socket形式(默认)，启动uwsgi:

::

 uwsgi --ini uwsgi_conf.ini -d ./uwsgi.log

socket端口为配置文件中的端口:5000.在浏览器内访问: http://127.0.0.1:5000 会输出hello world。


关闭uwsgi

::

 pkill -f uwsgi -9

查看uwsgi

::

 ps aux |grep uwsgi

参考文档
======================

Flask的部署_

.. _Flask的部署: https://windard.com/project/2016/12/01/Deploy-Flask-APP

