import socket
import glob, time, datetime

def log_temp(temperature):
#   temp_c, temp_f = read_temp()
    dt = datetime.datetime.now()
    f = open(logging_file, 'a')
    f.write('\n{:%H:%M:%S},'.format(dt))
#   f.write(str(temp_c))
    f.write(temperature)
    f.close()


# Define o intervalo de tempo em cada amostagem
log_period = 10 # seconds

# Seleciona a interface USB onde os dados serão gravados
logging_folder = glob.glob('/media/pi/*')[0]
dt = datetime.datetime.now()
file_name = "temp_log_{:%Y_%m_%d}.csv".format(dt)
logging_file = logging_folder + '/' + file_name

print("Logging to: " + logging_file)

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
    temperature = c.recv(1024).decode()
    print(temperature)
    log_temp(temperature)
    time.sleep(log_period)    
    # ----------------------------------------------------
    c.close()
    
