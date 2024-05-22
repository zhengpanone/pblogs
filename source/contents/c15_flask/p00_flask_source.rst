========================
Flask源码学习
========================

flask_source.py源码：

.. literalinclude:: ./code/p00_flask_source/flask_source.py
    :encoding: utf-8
    :language: python
    :emphasize-lines: 5
    :linenos:


WSGI
--------

WSGI，全称Web Server Gateway Interface，或者Python Web Server Gateway Interface，是基于Python 定义的Web服务器和Web应用程序或框架之间的一种简单而通用的接口。WSGI接口的作用是确保HTTP请求能够转化成python应用的一个功能调用，这就是Gateway的意义所在，网关的作用就是在协议之前进行转换

WSGI接口中有一个非常明确的标准，每个Python Web应用必须是可调用callbale对象且返回一个iterator，并且实现了app(environ，start_response) 的接口，server会调用application，并传给它两个参数：environ包含了请求的所有信息，start_response是application处理完之后需要调用的函数，参数是状态码、响应头部还有错误信息。引用代码示例：

.. literalinclude:: ./code/p00_flask_source/wsgi_server.py
    :encoding: utf-8
    :language: python
    :emphasize-lines: 5
    :linenos:

.. figure::|image1|
   :width: 100%
   :alt: image1

如上图所示，Flask框架包含了与WSGI Server通信部分和Application本身。Flask Server本身也包含了一个简单的WSGI Server（这也是为什么运行flask_source.py可以在浏览器访问的原因）用以开发测试使用。在实际的生产部署中，我们将使用apache、nginx+Gunicorn等方式进行部署，以适应性能要求。



.. |image1| image:: ./image/181104.webp
