
import socket

ms=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ainfo=socket.getaddrinfo(None,1234)
 
 ainfo
# OUTPUT WAS---> [(10, 1, 6, '', ('::1', 1234, 0, 0)), (10, 2, 17, '', ('::1', 1234, 0, 0)), (10, 3, 0, '', ('::1', 1234, 0, 0)), (2, 1, 6, '', ('127.0.0.1', 1234)), (2, 2, 17, '', ('127.0.0.1', 1234)), (2, 3, 0, '', ('127.0.0.1', 1234))]
 
 ainfo[5][4]
# OUTPUT WAS---> ('127.0.0.1', 1234)
ms.bind(ainfo[5][4])


ms.listen(5)

conn,addr=ms.accept()

data=conn.recv(1000)

print(data)

#OUTPUT WAS---> Got a Request!

conn.close()
ms.close()

