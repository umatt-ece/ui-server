# ======================================
# SPI-based Microcontroller Communication
# ======================================

import spidev

# ======================================
# Microcontroller class using SPI protocol
# ======================================
class Microcontroller():
    def __init__(self, bus, device):
        """
        Initialize the SPI interface

        Args:
            bus (int): SPI bus number
            device (int): SPI device (chip select) number
        """
        self.spi = spidev.SpiDev()       # Create SPI object
        self.spi.open(bus, device)       # Open SPI connection to given bus and device

    # ======================================
    # Read data from SPI device
    # ======================================
    def get(self, parameter):
        """
        Read a specified number of bytes from the SPI device

        Args:
            parameter (int): Number of bytes to read

        Returns:
            list[int]: List of bytes read from the device
        """
        try:
            response = self.spi.readbytes(parameter)  # Read `parameter` number of bytes
            return response
        except IOError as e:
            print(f"Error reading from SPI device: {e}")  # Handle read error

    # ======================================
    # Write data to SPI device
    # ======================================
    def set(self, parameter, value):
        """
        Send a predefined sequence of bytes to the SPI device

        Args:
            parameter: (unused in this stub)
            value: (unused in this stub)
        """
        try:
            self.spi.xfer([0x01, 0x02, 0x03])  # Example data transfer
        except IOError as e:
            print(f"Error sending data to SPI device: {e}")  # Handle write error

    # ======================================
    # Close SPI connection
    # ======================================
    def close(self):
        """
        Close the SPI connection
        """
        self.spi.close()
