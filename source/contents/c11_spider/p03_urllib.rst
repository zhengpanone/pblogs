=============
3. Urllib
=============

Python 内置的HTTP请求库

- urllib.request 请求模块
- urllib.error 异常处理模块
- urllib.parse url解析模块
- urllib.robotparser robots.txt 解析模块


urlopen 请求
===============

GET请求
>>>>>>>>

.. code-block:: python
 
  import urllib.request
  response = urllib.request.urlopen('http://www.baidu.com')
  print(response.read().decode('utf-8'))


POST请求
>>>>>>>>>

.. code-block:: python

  import urllib.parse
  import urllib.request

  data = bytes(urllib.parse.urlencode({'word':'hello'}).encode('utf-8'))
  response = urllib.requset.urlopen('http://httpbin.org/post',data=data)
  print(response.read())

超时设置
>>>>>>>>>

.. code-block:: python

  import urllib.request
  response = urllib.request.urlopen('http://httpbin.org/get',timeout=1)
  print(response.read())


.. code-block:: python

  import socket
  import urllib.request
  import urllib.error

  try:
      response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
  except urllib.error.URLError as e:
      if isinstance(e.reason.socket.timeout):
          print('TIME OUT')


urlopen 响应
============

响应类型
>>>>>>>>>>

.. code-block:: python

  import urllib.request
  response = urllib.request.urlopen('https://www.python.org')
  print(type(response))

状态码、响应头
>>>>>>>>>>>>>>>>>>>

.. code-block:: python

  import urllib.request
  response=urllib.request.urlopen('https://www.python.org')
  print('状态码', response.status)
  print('响应头',response.getheaders())
  print('Server',response.getheader('Server'))
  print('响应体',response.read().decode('utf-8')) # 字节流byte类型，通过decode转码

Request
===========

.. code-block:: python

  import urllib.request
  request = urllib.request.Request('https://python.org') # 定义Request对象
  response = urllib.request.urlopen(request)
  print(request.read().decode('utf-8'))

.. code-block:: python

  from urllib import request,parse
  url = "http://httpbin.org/post"    # 构造post请求
  headers = {        # 添加headers 信息
      'User-Agent':'Mozilla/4.0 (compatible;MSIE 5.5;Windows NT)',
      'Host':'httpbin.org'
  }
  dict = {
      'name':'Gemey'
  }
  data = bytes(parse.urlencode(dict),encoding='utf-8') # 添加formdata
  req = request.Request(url=url,data=data,headers=headers,method='POST') # 构造Request
  response = request.urlopen(req)
  print(response.read().decode('utf-8'))

.. code-block:: python

  from urllib import request,parse
  url = "http://httpbin.org/post"
  dict = {
      'name':'Gemey'
  }
  data = bytes(parse.urlencode(dict),encoding='utf-8')
  req = request.Request(url=url,data=data,method='POST')
  req.add_header('User-Agent','Mozilla/4.0(compatible;MSIE 5.5;Windows NT)')
  response = request.urlopen(req)
  print(response.read().decode('utf-8'))

Handler
========

代理
>>>>>>

.. code-block:: python

  import urllib.request
  proxy_hander=urllib.request.Proxy_Handler({ 
      'http':'http://127.0.0.1:9743',
      'https':'https://127.0.0.1:9743'
  })
  opener = urllib.request.build_opener(proxy_hander)
  response = opener.open('http://www.baidu.com')
  print(response.read())


Cookie
>>>>>>>>

用来维持登陆状态

查看cookie内容
:::::::::::::::::::

.. code-block:: python

  import http.cookie,urllib.request
  cookie = http.cookiejar.CookieJar()
  handler = urllib.request.HTTPCookieProcesson(cookie)
  opener = urllib.request.build_opener(handler)
  response = opener.open('http://www.baidu.com')
  for item im cookie:
      print(item.name+"="+item.value)

存Cookie
::::::::::::::

.. code-block:: python

  import http.cookiejar,urllib.request
  filename = 'cookie.txt'
  cookie = http.cookiejar.MozillaCookieJar(filename)
  handler = urllib.request.HTTPCookieProcesson(cookie)
  opener = urllib.request.build_opener(handler)
  response = opener.open('http://www.baidu.com')
  cookie.save(ignore_discard=True,ignore_expires=True)

.. code-block:: python

  import http.cookiejar,urllib.request
  filename = 'cookie.txt'
  cookie = http.cookiejar.LWPCookieJar(filename)
  handler = urllib.request.HTTPCookieProcesson(cookie)
  opener = urllib.request.build_opener(handler)
  response = opener.open("http://www.baidu.com")
  cookie.save(ignore_discard=True,ignore_expires=True)

读Cookie
::::::::::::::::

::

 improt http.cookiejar,urllib.request
 cookie = http.cookiejar.LWPCookieJar()
 cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)
 handler = urllib.request.HTTPCookieProcesson(cookie)
 opener = urllib.request.build_opener(handler)
 response = opener.open('http://www.baidu.com')
 print(response.read().decode('utf-8'))

异常处理
========

.. code-block:: python

  from urllib import request,error
  try:
    response = request.urlopen("http://cuiqingcai.com/index.html")
  except error.URLError as e:
    print(e.reason)

.. code-block:: python

  from urllib import request,error
  
  try:
    response = request.urlopen("http://cuiqingcai.com/index.html")
  except error.HTTPError as e:
    print(e.reason,e.code,e.headers,sep='\n')
  except error.URLError as e:
    print(e.reason)
  else:
    print('Request Successfully')
 
.. code-block:: python

  import socket
  import urllib.request
  import urllib.error

  try:
    response = urllib.request.urlopen('https://www.baidu.com')
  except urllib.error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT')

URL解析
=========

urlparse
>>>>>>>>>

>>> urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True)

.. code-block:: python

  from urllib.parse import urlparse

  result = urlparse("http://www.baidu.com/index.html;user?id=5#comment")
  print(type(result),result)

|image1|

.. code-block:: python

  from urllib.parse import urlparse
  result = urlparse('www.baidu.com/index;user?id=5#comment',scheme='https')
  print(result)

|image2|

.. code-block:: python

  from urllib.parse improt urlparse
  result = urlparse('http://www.baidu.com/index.html;user?id=5#comment',scheme='https')
  print(result)


|image3|

.. code-block:: python

  from urllib.parse import urlparse
  result = urlparse('http://www.baidu.com/index.html;user?id=5#comment',allow_fragments=False)
  print(result)

|image4|

.. code-block:: python

  from urllib.parse import urlparse
  result = urlparse('http://www.baidu.com/index.html#comment',allow_fragments=False)
  print(result)
 
|image5|

urlunparse
>>>>>>>>>>>>>>>>

.. code-block:: python

  from urllib.parse import urlunparse
  data = ['http','www.baidu.com','index.html','user','a=6','comment']
  print(urlunparse(data))

|image6|

urljoin
>>>>>>>>

.. code-block:: python

  from urllib.parse import urljoin
  print(urljoin('http://www.baidu.com','FAQ.html'))

|image7|

urlencode
>>>>>>>>>>>>>

将字典对象转换为GET请求

.. code-block:: python

  from urllib.parse import urlencode
  params ={
      'name':'germey',
      'age':'22'
  }
  base_url = 'http://www.baidu.com?'
  url = base_url+urlencode(params)
  print(url)


.. |image1| image:: ./image/20181215195732.png
.. |image2| image:: ./image/20181215200151.png
.. |image3| image:: ./image/20181215200311.png
.. |image4| image:: ./image/20181215200619.png
.. |image5| image:: ./image/20181215200813.png
.. |image6| image:: ./image/20181215201233.png
.. |image7| image:: ./image/20181215201853.png