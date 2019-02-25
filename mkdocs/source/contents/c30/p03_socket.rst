========================
30.3 socket
========================

TCP协议
============================

.. important:: 端口号只有整数，范围是0到65535 2的16次方

.. important:: - 80端口分配给HTTP服务
               - 21端口分配给FTP服务

.. note:: **netstat -an** 查看端口状态


socket
===========================

7层网络模型-OSI
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

- 基础层：物理层（Physical）、数据链路层（Datalink）、网络层（Network)
- 传输层（Transport)：TCP-UDP协议层、Socket
- 高级层：会话层（Session)、表示层（Presentation）、应用层（Application)

|image1| |image2|





socket 是进程间通信的一种方式，

创建一个tcp socket(tcp套接字)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

::

 import socket
 s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 
创建一个udp socket(udp套接字)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

::

 import socket
 s = socket.socket(socket.AF_INET,socket.SOck_DGRAM)

::

 from socket import *
 udpSocket = socket(AF_INET,SOck_DGRAM)
 udpSocket.sendto(b"haha","192.168.119.115",8080)



.. |image1| image:: ./image/19022501.webp
.. |image2| image:: ./image/19022502.webp
