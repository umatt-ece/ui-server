# ===========================================================
# parameters.py - Definition of system parameters and metadata
#
# This file defines two dictionaries, `VARIABLES` and `VARIABLES_TEST`,
# which represent configuration and telemetry parameters used in the
# system. Each parameter includes metadata such as its type, default
# value, and optionally a description and unit.
#
# These parameter definitions are typically referenced throughout the
# system (e.g., API server, microcontroller sync, and UI) to validate,
# initialize, and document control values stored in Redis.
# ===========================================================

from enum import Enum
from collections import namedtuple

# ===========================================================
# Dictionary: VARIABLES_TEST
#
# Purpose:
#   A small test set of parameters used for development or
#   diagnostic purposes. Useful when running in a test mode
#   or unit testing without full hardware.
#
# Structure:
#   {
#     "PARAM_NAME": {
#         "type": <Python type>,
#         "default": <default value>,
#         "description": <optional string>
#     }
#   }
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
# Dictionary: VARIABLES
#
# Purpose:
#   Master list of control and sensor parameters for the
#   tractor system. Each parameter includes its type,
#   default value, and a description (and optionally a unit).
#
# Typical usage:
#   - Validation for API input
#   - Default value population
#   - Metadata for UI/UX or documentation
#
# Example Entry:
#   "SEAT_PRESENCE": {
#       "type": bool,
#       "default": False,
#       "description": "The value of the seat sensor"
#   }
# ===========================================================
VARIABLES = {
    "SEAT_PRESENCE": {
        "type": bool,
        "default": False,
        "description": "The value of the seat sensor",
    },
    "L_JOYSTICK": {
        "type": int,
        "default": 0,
        "description": "The value of the left joystick",
    },
    "R_JOYSTICK": {
        "type": int,
        "default": 0,
        "description": "The value of the right joystick",
    },
    "L_JOYSTICK_PREVIOUS": {
        "type": int,
        "default": 0,
        "description": "The previous value of the left joystick",
    },
    "R_JOYSTICK_PREVIOUS": {
        "type": int,
        "default": 0,
        "description": "The previous value of the right joystick",
    },
    "L_DEADMAN_SENSOR": {
        "type": bool,
        "default": False,
        "description": "The value of the left deadman's switch",
    },
    "R_DEADMAN_SENSOR": {
        "type": bool,
        "default": False,
        "description": "The value of the right deadman's switch",
    },
    "GEAR": {
        "type": int,
        "default": 1,
        "description": "The current gear of the tractor (Fast = 0, Neutral = 1, Slow = 2)",
    },
    "L_MOTOR_DELAY": {
        "type": int,
        "default": 0,
        "unit": "ms",
        "description": "The delay for the left motor to reach the desired speed",
    },
    "R_MOTOR_DELAY": {
        "type": int,
        "default": 0,
        "unit": "ms",
        "description": "The delay for the right motor to reach the desired speed",
    },
}
