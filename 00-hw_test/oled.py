#!/usr/bin/env python3
import time
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
 
#Variaveis globais
# Raspberry Pi - configuracao dos pinos:
RST = 24 #embora nao utilizado de fato, eh preciso defini-lo para a biblioteca funcionar
 
# Configura uso do display OLED de 128x64 (comunicacao I2C)
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
 
#------------------------------------------------------
#   PROGRAMA PRINCIPAL Display Oled com Raspberry Pi
#------------------------------------------------------
 
#Inicializa biblioteca de comunicacao com display e o limpa
disp.begin()
disp.clear()
disp.display()
 
#obtem altura e largura totais do display
width = disp.width
height = disp.height
 
#Carregamento das imagens.
#Importante: quanto maior a imagem, mais tempo esta conversao levara.
 
#Carrega a imagem 1 (ImagemTeste1.png) e automaticamente ja binariza e ajusta a resolucao da mesma.
image1 = Image.open('images/ImagemTeste1.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')
 
#Carrega a imagem 2 (ImagemTeste2.png) e automaticamente ja binariza e ajusta a resolucao da mesma.
image2 = Image.open('images/ImagemTeste2.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')
 
#Carrega a imagem 3 (ImagemTeste3.png) e automaticamente ja binariza e ajusta a resolucao da mesma.
image3 = Image.open('images/ImagemTeste3.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')
 
#Preparacoes necessarias para apagar tela
image = Image.new('1', (width, height)) #imagem binaria (somente 1's e 0's)
draw = ImageDraw.Draw(image)
 
#laco principal
 
while True:
    #Mostra a imagem 1 por 5 segundos
    disp.image(image1)
    disp.display()
    time.sleep(5)
     
    #desenha um retangulo preto em todo o display (para apagar "restos" de dados na 
    #area de display)
    draw.rectangle((0,0,width,height), outline=0, fill=0)
     
    #Mostra a imagem 2 por 5 segundos
    disp.image(image2)
    disp.display()
    time.sleep(5)
     
    #desenha um retangulo preto em todo o display (para apagar "restos" de dados na 
    #area de display)
    draw.rectangle((0,0,width,height), outline=0, fill=0)
     
    #Mostra a imagem 3 por 5 segundos
    disp.image(image3)
    disp.display()
    time.sleep(5)
     
    #desenha um retangulo preto em todo o display (para apagar "restos" de dados na 
    #area de display)
    draw.rectangle((0,0,width,height), outline=0, fill=0)    
