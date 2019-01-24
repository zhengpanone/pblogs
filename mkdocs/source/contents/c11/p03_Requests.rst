==========================
11.3 Requests库
==========================

Requests 是使用Python 语言编写，基于urllib,采用Apache2 Licensed 开源协议的HTTP库

实例引入
========================

:: 

 import requests 
 response = requests.get('https://www.baidu.com')
 print(type(response))
 print(response.status_code)
 print(type(response.text))
 print(response.txt)
 print(response.cookies)

各种请求方式
==============================

::

 import requests
 requests.post('http://www.baidu.com/post')
 requests.put('http://httpbin.org/put')
 requests.delete('http://httpbin.org/delete')
 requests.head('http://httpbin.org/get')
 requests.options('http://httpbin.org/get')

请求
==================

基本GET请求
>>>>>>>>>>>>>>>>>>>>>>>>

基本写法
:::::::::::::::::::::::::::::::::::::::::::::

::

 import requests

 response = requests.get('http://httplib.org/get')
 print(response.text)

带参数GET请求
:::::::::::::::::::::::::::::::::::::::::::::::::::

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
:::::::::::::::::::::::::::::::::::::::::::::::::::::::

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

添加headers
:::::::::::::::::::::::::::::::::::::::::::::

::

 import requests
 response = requests.get('https://www.zhihu.com/explore')
 print(response.text)

::

 import requests
 headers = {
    'User-Agent':'Mozilla/5.0(Macintosh;Inter Mac OS X 10_11_4) AppleWebkit/537.36(HHTML,like Gecko) Chrome/52.0.2743.116 Safari/537.36'
 }
 response = requests.get('https://www.zhihu.com/explore',headers = headers)
 print(response.text)

基本POST请求
==============

::

 import requests
 data = {'name':'germey','age':'22'}
 response = requests.post('http:httpbin.org/post',data =data)
 print(response.text)

::

 import requests
 datat = {'name':'germey','age':'22'}
 headers =  {
    'User-Agent':'Mozilla/5.0(Macintosh;Inter Mac OS X 10_11_4) AppleWebkit/537.36(HHTML,like Gecko) Chrome/52.0.2743.116 Safari/537.36'
 }
 response = requests.post('https://httpbin.org/post',data =data,headers=headers)
 print(response.json())

响应
===============

response属性
>>>>>>>>>>>>>>>>>>>>>>>>

::

 import requests
 response = requests.get('http://www.jianshu.com')
 print(type(response.status_code),response.status_code)
 print(type(response,headers),response.headers)
 print(type(response.cookies),response.cookies)
 print(type(response.url),response.url)
 print(type(response.history),response.history)

状态码判断
>>>>>>>>>>>>>>>>>>>>>

::

 import requests
 response = requests.get('http://wwww.jianshu.com')
 exit() if not response.status_code == requests.codes.ok else print('Requests Successfully')

|image1|

.. |image1| image:: ./image/