=============
11.2 Urllib
=============

Python 内置的HTTP请求库

- urllib.request 请求模块
- urllib.error 异常处理模块
- urllib.parse url解析模块
- urllib.robotparser robots.txt 解析模块

GET请求

::
 
 import urllib.request
 response = urllib.request.openurl('http://www.baidu.com')
 print(response.read().decode('utf-8'))


POST请求

::

 import urllib.parse
 import urllib.request

 data = bytes(urllib.parse.urlencode({'word':'hello'}).encode('utf-8'))
 response = urllib.requset.urlopen('http://httpbin.org/post',data=data)
 print(response.read())