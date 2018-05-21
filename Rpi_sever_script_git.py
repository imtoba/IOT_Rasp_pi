pi@raspberrypi:~ $ python
Python 2.7.9 (default, Sep 17 2016, 20:26:04) 
[GCC 4.9.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import socket
>>> ms=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
>>> ainfo=socket.getaddrinfo(None,1234)
>>> ainfo
[(10, 1, 6, '', ('::1', 1234, 0, 0)), (10, 2, 17, '', ('::1', 1234, 0, 0)), (10, 3, 0, '', ('::1', 1234, 0, 0)), (2, 1, 6, '', ('127.0.0.1', 1234)), (2, 2, 17, '', ('127.0.0.1', 1234)), (2, 3, 0, '', ('127.0.0.1', 1234))]
>>> ainfo[5][4]
('127.0.0.1', 1234)
>>> ms.bind(ainfo[5][4])
>>> ms.listen(5)
>>> conn,addr=ms.accept()
>>> data=conn.recv(1000)
>>> print(data)
Got a Request!

>>> print(data)
Got a Request!

>>> data=conn.recv(1000)
>>> print(data)
Hello There Its my First RPi Assignment

>>> 
