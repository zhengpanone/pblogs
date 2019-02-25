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

SOcket基础
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

- 简单来说是IP地址与端口的结合协议（RFC793）
- 一种地址与端口的结合描述协议
- TCP/IP协议的相关API的总称；是网络Api的集合实现
- 涵盖了：Stream Socket/Datagram Socket
- 作用：

 + 在网络传输中用于唯一标示两个端点之间的链接
 + 端点：包括（IP+Port)
 + 4个要素：客户端地址、客户端端口、服务器地址、服务器端口

- TCP

 + TCP是面向连接的通信协议
 + 通过三次握手建立连接，通讯完成时要拆除连接
 + 由于TCP是面向连接的所以只能用于端到端的通讯

- UDP

 + UDP是面向无连接的通讯协议
 + UDP数据包括目的端口号和源端口号信息
 + 由于通讯不需要连接，所以可以实现广播发送，并不局限于端到端

- TCP/IP协议中，两个进程间通信的主要模式为：CS模型
- 主要目的：协同网络中的计算机资源、服务模式、进程间数据共享
- 常见的：FTP、SMTP、HTTP




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
