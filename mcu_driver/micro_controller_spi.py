import spidev

class Microcontroller():
    def __init__(self, bus, device):
        self.spi = spidev.SpiDev()
        self.spi.open(bus, device)

    def get(self, parameter):
        try:
            response = self.spi.readbytes(parameter)
            return response
        except IOError as e:
            print(f"Error reading from SPI device: {e}")
        
    def set(self, parameter, value):
        try:
            self.spi.xfer([0x01, 0x02, 0x03]) 
        except IOError as e:
            print(f"Error sending data to SPI device: {e}")
        
    def close(self):
        self.spi.close()
