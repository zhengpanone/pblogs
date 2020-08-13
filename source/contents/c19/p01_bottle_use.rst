============================
19.1 bottle基本使用
============================

入门
---------------

::

 from bottle import route,run
 @route("/hello")
 def hello():
    return "Hello World!"

 run(host="0.0.0.0",port=8080,debug=True)
 
参考文档：https://blog.csdn.net/nawenqiang/article/details/79381807
