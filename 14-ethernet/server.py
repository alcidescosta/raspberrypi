#!/usr/bin/env python3
import socket

# Cria socket para
s = socket.socket()

# Atribui IP e porta em um socket. Estas informações são necessárias
# no lado-cliente para que este possa qual IP e porta o servidor está
# escutando.
host = 'localhost'
port = 1234
s.bind((host, port))

# Socket na escuta, esperando por conexões no lado-cliente. Suporta
# até 5 conexões. Mais do isso, o servidor descarta.
s.listen(5)

# Para cada conexão, cria um novo socket, informa que a conexão foi
# bem-sucedida e recebe temperatura.
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send("Thank you for connecting".encode())
    # ----------------------------------------------------
    # Esta seção de código deve ser alterada para suportar
    # o código do data logger. Cada dado recebido deve ser
    # armazenada no pendrive
    print(c.recv(1024).decode())
    
    # ----------------------------------------------------
    c.close()
    
