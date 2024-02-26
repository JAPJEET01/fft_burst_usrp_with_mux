import numpy as np
from gnuradio import gr
import serial

class ArduinoSerialReader(gr.sync_block):
    """Custom GNU Radio block to read data from Arduino serial output"""

    def __init__(self, port='/dev/ttyACM0', baudrate=9600):
        """Initialize the block"""
        gr.sync_block.__init__(
            self,
            name='Arduino Serial Reader',
            in_sig=None,
            out_sig=[np.uint8]  # Change the output signature if necessary
        )
        self.serial_port = serial.Serial(port, baudrate)

    def work(self, input_items, output_items):
        """Read data from serial port and emit"""
        data = self.serial_port.read(512)  # Read serial data, adjust buffer size as needed
        output_items[0][:len(data)] = np.frombuffer(data, dtype=np.uint8)
        return len(data)
