=============
11.2 Requests库
=============

Requests 是使用Python 语言编写，基于urllib,采用Apache2 Licensed 开源协议的HTTP库

实例引入
===========

:: 

 import requests 
 response = requests.get('https://www.baidu.com')
 print(type(response))
 print(response.status_code)
 print(type(response.text))
 print(response.txt)
 print(response.cookies)

各种请求方式
============

::

 import requests
 requests.post('http://www.baidu.com/post')
 requests.put('http://httpbin.org/put')
 requests.delete('http://httpbin.org/delete')
 requests.head('http://httpbin.org/get')
 requests.options('http://httpbin.org/get')

请求
=======

基本GET请求
>>>>>>>>>>>>>>>>

基本写法
::::::::::::

::

 


|image1|

.. |image1| image:: ./image/