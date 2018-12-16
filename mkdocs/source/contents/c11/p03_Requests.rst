=============
11.3 Requests库
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

 import requests

 response = requests.get('http://httplib.org/get')
 print(response.text)

带参数GET请求
::::::::::::::

::

 import requests

 response = requests.get('http://httplib.org/get?name=germey&age=22')
 print(response.text)

::

 import requests
 data = {
    'name':'germey',
    'age':22
 }
 response = requests.get('http://httpbin.org/get',params=data)
 print(response.text)

解析json
:::::::::::::::::::::::

::

 import requests
 response = requests.get('http://httpbin.org/get')
 print(type(response,text))
 print(response.json())
 print(type(response.json()))

获取二进制数据
::::::::::::::::::::::::::::::::::

::

 import requests
 response = requests.get('https:github.com/favicon.ico')
 print(type(response),type(response.content))
 print(response.text)
 print(response.content)


::

 import requests

 response = requests.get('http://github.com/favicon.ico')
 with open('favicon.ico',wb) as f:
    f.write(response.content)
    f.close()



|image1|

.. |image1| image:: ./image/