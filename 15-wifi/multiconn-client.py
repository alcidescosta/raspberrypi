#!/usr/bin/env python3
######################################################################
# CABECALHO
# Adicione aqui as bibliotecas usadas para o desenvolvimento deste
# sistema. Dica: faca comentarios sem acentos. Isso evita erros de
# interpretacao do Python
import board
import adafruit_dht
import time
import glob, datetime

import sys
import socket
import selectors
import types

######################################################################
# INICIALIZACAO
# Adicione aqui codigo para a inicializacao dos dispositivos do siste-
# ma embarcado. Normalmente, este codigo e encontrado no fabricante do
# dispositivo. Adicione, tambem constantes e variaveis do sistema.

###########################
# Inicializacao do dht
#
#indica o pino GPIO da placa Raspberry onde a temperatura e
#a humidade devem ser lidas. Nota: em placas Raspberry Pi,
#use_pulseio=False pode ser necessario.
dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)

sel = selectors.DefaultSelector()
#messages = [b"Message 1 from client.", b"Message 2 from client."]

def start_connections(host, port, connid):
    server_addr = (host, port)
    print(f"Starting connection {connid} to {server_addr}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.connect_ex(server_addr)
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    data = types.SimpleNamespace(
        connid=connid,
        msg_total=sum(len(m) for m in messages),
        recv_total=0,
        messages=messages.copy(),
        outb=b"",
    )
    sel.register(sock, events, data=data)


def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            print(f"Received {recv_data!r} from connection {data.connid}")
            data.recv_total += len(recv_data)
        if not recv_data or data.recv_total == data.msg_total:
            print(f"Closing connection {data.connid}")
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if not data.outb and data.messages:
            data.outb = data.messages.pop(0)
        if data.outb:
            print(f"Sending {data.outb!r} to connection {data.connid}")
            sent = sock.send(data.outb)  # Should be ready to write
            data.outb = data.outb[sent:]

######################################################################
# PROGRAMA PRINCIPAL
# Adicione aqui o codigo que captura os dados dos sensores. Fa??a as
# opera????es de escrita no display e pendrive. Este c??digo deve perma-
# necer em execu????o - permanecer em loop - at?? ser abortado pelo usu-
# ??rio (ctrl+c).
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <host> <port>")
    sys.exit(1)

intervalo_da_amostra = 2.0 # segundos
host, port = sys.argv[1:3]
connid = 0

try:
    while True:
        while True:
            try:
                # este codigo esta dentro de um try. Isso quer dizer que, caso
                # houver erro na leitura do sensor, o codigo sera desviado para
                # o tratamento de excecao (ver except)
                temperature_c = dhtDevice.temperature
                temperature_f = temperature_c * (9 / 5) + 32
                humidity = dhtDevice.humidity
                # registra momento da amostragem dos dados
                dt = datetime.datetime.now()
                print(
                    "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                        temperature_f, temperature_c, humidity
                    )
                )
                # se chegou ate aqui e porque nao houve erro na leitura do dht
                # quebra o while e vai para o passo 2
                break

            except RuntimeError as error:
                # o sensor DHT pode falhar ao ler.
                # Se isso ocorrer, repita a operacao de leitura
                print(error.args[0])
                time.sleep(2.0)
                continue

            except Exception as error:
                # erro critico. Sai do programa
                dhtDevice.exit()
                raise error

        ### Passo 2 - envia temperatura e humidade para o servidor
        time.sleep(intervalo_da_amostra)
        connid += 1
        messages = [(str(temperature_c) + "," + str(humidity)).encode()]
        start_connections(host, int(port), connid)
        events = sel.select(timeout=1)
        if events:
            for key, mask in events:
                service_connection(key, mask)
        # Check for a socket being monitored to continue.
        if not sel.get_map():
            break
except KeyboardInterrupt:
    print("Caught keyboard interrupt, exiting")
finally:
    sel.close()
