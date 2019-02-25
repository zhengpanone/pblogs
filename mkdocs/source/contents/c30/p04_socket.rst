========================
30.4 Socket入门
========================

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
.. |image3| image:: ./image/i9022503.webp
