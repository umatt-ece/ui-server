import can

class Microcontroller():
    def __init__(self):
        self.bus = can.interface.Bus('text', interface='virtual',bitrate=500000)

    def get(self, parameter):
        try:
            msg = self.bus.recv(timeout=1)
            return msg
        except can.CanError as e:
            print(f"Error receiving message: {e}")            

    def set(self, parameter, value):
        msg = can.Message(arbitration_id=0x123, data=[1,2,3])
        try:
            self.bus.send(msg)
        except can.CanError as e:
            print(f"Error sending message: {e}")
        
    def close(self):
        self.bus.shutdown()
            
            
