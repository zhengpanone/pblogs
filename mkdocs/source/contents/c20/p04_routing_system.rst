========================
20.4 路由系统
========================

1. 可传入参数
-----------------------------

::
 
 @app.route('/user/<username>')     # 常用的   不加参数时默认字符串形式
 @app.route('/post/<int：post_id>')     # 常用的    指定int 说明是整型
 @app.route('/post/<float:post_id>')
 @app.route('/post/<path:path>')
 @app.route('/login', methods=['GET', 'POST'])


::

 DEFAULT_CONVERTERS = {
    'default':          UnicodeConverter,
    'string':           UnicodeConverter,
    'any':              AnyConverter,
    'path':             PathConverter,
    'int':              IntegerConverter,
    'float':            FloatConverter,
    'uuid':             UUIDConverter,
 }

2. 反向生成URL:url_for
-------------------------------

endpoint("name")   #别名，相当于django中的name

::

 from flask import Flask,url_for

 @app.route('/index', endpoint='xxx')   # endpoint是别名