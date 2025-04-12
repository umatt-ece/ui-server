import spidev
import time

spi = spidev.SpiDev()  
spi.open(0, 0) 
spi.max_speed_hz = 50000 
spi.mode = 0  

data_to_send = [0x00]  
response = spi.xfer2(data_to_send) 

spi.close()