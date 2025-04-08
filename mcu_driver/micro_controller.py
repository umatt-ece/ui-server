# mcu_driver.py
import can
import struct
from typing import Any, Dict, Optional
import time

class J1939MessageParser:
    def extract_bits(data: bytes, start_bit: int, bit_length: int) -> int:
        full_value = int.from_bytes(data, byteorder='little')
        
        # Create mask
        mask = (1 << bit_length) - 1
        
        # Shift and mask
        extracted_value = (full_value >> start_bit) & mask
        return extracted_value

class Microcontroller:
    def __init__(self, 
                 interface='can0', 
                 bitrate=250000, 
                 bustype='socketcan'):
        self.bus = can.interface.Bus(
            channel=interface, 
            bustype=bustype, 
            bitrate=bitrate
        )
        
        self.parameter_mapping = {
            "SEAT_PRESENCE": {
                "pgn": 0xFEF1, 
                "start_bit": 0,
                "bit_length": 1,
                "type": bool
            },
            "L_JOYSTICK": {
                "pgn": 0xFEF2,  
                "start_bit": 8,
                "bit_length": 16,
                "type": int
            },
            # Add mappings for other parameters
        }
    
    def get(self, parameter: str) -> Optional[Any]:
        """
        Get a specific parameter from CAN messages
        
        Args:
            parameter (str): Parameter name
        
        Returns:
            Optional value of the parameter
        """
        try:
            msg = self.bus.recv(timeout=1.0)
            
            if msg is None:
                return None
            
            param_spec = self.parameter_mapping.get(parameter)
            if not param_spec:
                return None
            
            raw_value = J1939MessageParser.extract_bits(
                msg.data, 
                param_spec['start_bit'], 
                param_spec['bit_length']
            )
            
            return param_spec['type'](raw_value)
        
        except can.CanError as e:
            print(f"CAN Error: {e}")
            return None
    
    def set(self, parameter: str, value: Any):
        try:
            param_spec = self.parameter_mapping.get(parameter)
            if not param_spec:
                raise ValueError(f"Unknown parameter: {parameter}")

            msg = can.Message(
                arbitration_id=param_spec['pgn'],
                data=value,
                is_extended_id=True
            )
            
            self.bus.send(msg)
        
        except Exception as e:
            print(f"Error setting parameter {parameter}: {e}")
    
    def _encode_value(self, value: Any, param_spec: Dict) -> bytes:

        # Implement value encoding logic
        return 0
    
    def close(self):
        """Close CAN bus connection"""
        self.bus.shutdown()