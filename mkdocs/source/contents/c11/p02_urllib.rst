=============
11.2 Urllib
=============

Python 内置的HTTP请求库

- urllib.request 请求模块
- urllib.error 异常处理模块
- urllib.parse url解析模块
- urllib.robotparser robots.txt 解析模块


请求
=====

GET请求
>>>>>>>>

::
 
 import urllib.request
 response = urllib.request.urlopen('http://www.baidu.com')
 print(response.read().decode('utf-8'))


POST请求
>>>>>>>>>

::

 import urllib.parse
 import urllib.request

 data = bytes(urllib.parse.urlencode({'word':'hello'}).encode('utf-8'))
 response = urllib.requset.urlopen('http://httpbin.org/post',data=data)
 print(response.read())

超时设置
>>>>>>>>>

::

 import urllib.request
 response = urllib.request.urlopen('http://httpbin.org/get',timeout=1)
 print(response.read())


::

 import socket
 import urllib.request
 import urllib.error

 try:
    response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
 except urllib.error.URLError as e:
    if isinstance(e.reason.socket.timeout):
        print('TIME OUT')


响应
============

响应类型
>>>>>>>>>>

::

 import urllib.request
 response = urllib.request.urlopen('https://www.python.org')
 print(type(response))

状态码、响应头
>>>>>>>>>>>>>>>>>>>

::

 import urllib.request
 response=urllib.request.urlopen('https://www.python.org')
 print('状态码', response.status)
 print('响应头',response.getheaders())
 print('Server',response.getheader('Server'))
 print('响应体',response.read().decode('utf-8')) # 字节流byte类型，通过decode转码