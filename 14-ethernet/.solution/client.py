import socket

s = socket.socket()
host = '192.168.10.101'
port = 1234
s.connect((host, port))
print(s.recv(1024).decode())
s.send("Here comes the temperature!".encode())

