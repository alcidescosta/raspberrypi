#!/usr/bin/env python3
import os, glob, time, datetime

# Define o intervalo de tempo em cada amostagem
log_period = 10 # seconds

# Seleciona a interface USB onde os dados serão gravados
logging_folder = glob.glob('/media/pi/*')[0]
dt = datetime.datetime.now()
file_name = "temp_log_{:%Y_%m_%d}.csv".format(dt)
logging_file = logging_folder + '/' + file_name

# Habilita driver de GPIO e sensor de temperatura
# os.system('modprobe w1-gpio')
# os.system('modprobe w1-therm')

# Mapeia sensor de temperatura para o linux
# base_dir = '/sys/bus/w1/devices/'
# device_folder = glob.glob(base_dir + '28*')[0]
# device_file = device_folder + '/w1_slave'

# Rotina de leitura da temperatura
# def read_temp_raw():
#     f = open(device_file, 'r')
#     lines = f.readlines()
#     f.close()
#     return lines

# Rotina conversao da temperatura para C/F
# def read_temp():
#     lines = read_temp_raw()
#     while lines[0].strip()[-3:] != 'YES':
#         time.sleep(0.2)
#         lines = read_temp_raw()
#     equals_pos = lines[1].find('t=')
#     if equals_pos != -1:
#         temp_string = lines[1][equals_pos+2:]
#         temp_c = float(temp_string) / 1000.0
#         temp_f = temp_c * 9.0 / 5.0 + 32.0
#         return temp_c, temp_f

def log_temp():
#   temp_c, temp_f = read_temp()
    dt = datetime.datetime.now()
    f = open(logging_file, 'a')
    f.write('\n"{:%H:%M:%S}",'.format(dt))
#   f.write(str(temp_c))
    f.write("A temperatura capturada pelo meu sensor vai aqui!!!")
    f.close()

print("Logging to: " + logging_file)
while True:
    log_temp()
    time.sleep(log_period)