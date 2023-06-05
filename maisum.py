import spidev
import signal
import time

#Função para finalizar o acesso à GPIO do Raspberry Pi
def end_read(signal,frame):
    global continue_reading
    print ("Ctrl+C captured, ending read.")
    continue_reading = False
    spi.close()

#Handler do sinal
signal.signal(signal.SIGINT, end_read)

#Variável para controlar o loop principal
continue_reading = True

#Cria o objeto spi
spi = spidev.SpiDev()
#Abre a conexão SPI (0 é o canal do chip enable)
spi.open(0,0)
#Configura a velocidade máxima do clock (em Hz)
spi.max_speed_hz = 1000000

#Função para ler os dados do sensor RFID
def readRFID():
    #Envia um comando para iniciar a leitura
    spi.xfer([128])
    #Lê 16 bytes do buffer
    data = spi.readbytes(16)
    #Retorna os dados lidos
    return data

#Loop principal
while continue_reading:
    #Lê os dados do sensor RFID
    data = readRFID()
    #Imprime os dados na tela
    print (data)
    #Aguarda 0.5 segundos
    time.sleep(0.5)

