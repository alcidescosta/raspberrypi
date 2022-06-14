#!/usr/bin/env python3
import socket

s = socket.socket()
host = 'localhost'
port = 1234
s.connect((host, port))
print(s.recv(1024).decode())
s.send("Here comes the temperature!".encode())

