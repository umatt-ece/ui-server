from common import VARIABLES, ParameterStore
from mcu_driver import Microcontroller

if __name__ == "__main__":
    mcu = Microcontroller('can0', 
                 250000, 
                 'virtual')
    ps = ParameterStore()
    data = {}
    for variable_name, variable_data in VARIABLES.items():
        data[variable_name] = variable_data["default"]

    while True:
        try:
            for variable_name, variable_data in VARIABLES.items():
                # Update from MCU
                value = mcu.get(variable_name)
                if value != data[variable_name]:
                    ps.set(variable_name, value)
                    data[variable_name] = value
                # Update from REDIS
                value = ps.get(variable_name)
                if value != data[variable_name]:
                    mcu.set(variable_name, value)
                    data[variable_name] = value
                # todo: figure out how to resolve conflicts if both change at the same time...
        except Exception as e:
            print(e)
            pass
        
    mcu.close()