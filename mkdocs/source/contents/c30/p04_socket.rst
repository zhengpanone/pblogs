========================
30.4 socket
========================

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



