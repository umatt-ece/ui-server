# ===========================================================
# parameters_ver2.py - Alternative Enum-based parameter model
#
# ⚠️ NOTE: This version is NOT currently used in the main system.
#
# This file defines an alternative representation of parameters
# using Python's `Enum` and `namedtuple` for a more structured,
# class-based design. It encapsulates each parameter's metadata
# (type, default value, unit, and description) as named fields.
#
# While cleaner and potentially more maintainable, this structure
# is not used in the current integration with Redis or the API.
# ===========================================================

from enum import Enum
from collections import namedtuple

# ===========================================================
# Dictionary: VARIABLES_TEST
#
# Purpose:
#   A minimal test dictionary used for quick unit testing.
#   Structured like the original VARIABLES dictionary.
# ===========================================================
VARIABLES_TEST = {
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

# ===========================================================
# Parameter field definition for the namedtuple
# Fields: type, default, unit, description
# Used for building parameter definitions inside the Enum.
# ===========================================================
fields = ["type", "default", "unit", "description"]

# ===========================================================
# Enum: Parameters
#
# Purpose:
#   Structured, class-based representation of all system parameters.
#   Each enum member holds a tuple of metadata values for:
#     - type (e.g., bool, int)
#     - default (initial/default value)
#     - unit (e.g., 'ms', or None)
#     - description (human-readable explanation)
#
# ⚠️ Not used by the API or Redis logic as of now.
# ===========================================================
class Parameters(namedtuple('Parameters', fields), Enum):
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

    # =======================================================
    # String representation override
    # Purpose: Return string form of parameter's value tuple
    # =======================================================
    def __str__(self) -> str:
        return str(self.value)

    # =======================================================
    # Static Method: all_param
    # Purpose: Return a list of all enum members
    # Returns: List[Parameters]
    # =======================================================
    @staticmethod
    def all_param() -> list:
        return [param for param in Parameters]
