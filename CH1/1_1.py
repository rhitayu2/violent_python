import socket
socket.setdefaulttimeout(100)
s = socket.socket()
s.connect(("172.217.163.110",21))
ans = s.recv(1024)
print ans
