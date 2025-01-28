from enum import Enum
from collections import namedtuple

VARIABLES = {
    "TEST_BOOL": {
        "type": bool,
        "default": False,
        "description": "this parameter is for testing boolean values",
    },
    "TEST_INT": {
        "type": int,
        "default": 0,
    },
    "TEST_STRING": {
        "type": str,
        "default": "",
    }
}

fields = ["type", "default", "unit", "description"]

class Parameters(namedtuple('Parameters',fields), Enum):
    SEAT_PRESENCE = (
        bool,
        False,
        None,
        " The value of the seat sensor",
    )
    L_JOYSTICK = (
        int,
        0,
        None,
        "The value of the left joystick",
    )
    R_JOYSTICK = (
        int,
        0,
        None,
        "The value of the right joystick"
    )
    L_JOYSTICK_PREVIOUS = (
        int,
        0,
        None,
        "The previous value of the left joystick",
    )
    R_JOYSTICK_PREVIOUS = (
        int,
        0,
        None,
        "The previous value of the right joystick",
    )
    L_DEADMAN_SENSOR = (
        bool,
        False,
        None,
        "The value of the left deadman’s switch",
    )
    R_DEADMAN_SENSOR = (
        bool,
        False,
        None,
        "The value of the right deadman’s switch",
    )
    GEAR = (
        int,
        1,
        None,
        "The current gear of the tractor (Fast = 0, Neutral = 1, Slow = 2)"
    )
    L_MOTOR_DELAY = (
        int,
        0,
        "ms",
        "The delay for the left motor to reach the desired speed",
    )
    R_MOTOR_DELAY = (
        int,
        0,
        "ms",
        "The delay for the right motor to reach the desired speed",
    )
    
    def __str__(self) -> str:
        return str(self.value)
    
    @staticmethod
    def all_param() -> list:
        return [param for param in Parameters]

