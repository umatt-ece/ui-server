from common import VARIABLES, ParameterStore
from mcu_driver import Microcontroller


if __name__ == "__main__":
    mcu = Microcontroller()
    ps = ParameterStore()
    data = {}
    for variable in VARIABLES:
        data[variable["name"]] = variable["default"]

    while True:
        try:
            for variable in VARIABLES:
                # Update from MCU
                value = mcu.get(variable["name"])
                if value != data[variable["name"]]:
                    ps.set(variable["name"], value)
                    data[variable["name"]] = value
                # Update from REDIS
                value = ps.get(variable["name"])
                if value != data[variable["name"]]:
                    mcu.set(variable["name"], value)
                    data[variable["name"]] = value
                # todo: figure out how to resolve conflicts if both change at the same time...
        except Exception as e:
            print(e)
            pass