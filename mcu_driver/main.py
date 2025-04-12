# =======================
# Import required modules
# =======================
from common import VARIABLES, ParameterStore
from mcu_driver import Microcontroller

# ========================
# Main Execution Entry Point
# ========================
if __name__ == "__main__":
    # Initialize Microcontroller
    mcu = Microcontroller('can0', 
                 250000, 
                 'virtual')  # Interface, baud rate, mode
    
    # Initialize Parameter Store (e.g., Redis)
    ps = ParameterStore()
    
    # Initialize local cache for variables
    data = {}
    for variable_name, variable_data in VARIABLES.items():
        data[variable_name] = variable_data["default"]  # Set default values

    # ========================
    # Main Synchronization Loop
    # ========================
    while True:
        try:
            # Loop through each variable to sync MCU <-> Redis
            for variable_name, variable_data in VARIABLES.items():
                
                # Update from MCU → Redis
                value = mcu.get(variable_name)  # Read from MCU
                if value != data[variable_name]:
                    ps.set(variable_name, value)  # Write to Redis
                    data[variable_name] = value   # Update local cache
                
                # Update from Redis → MCU
                value = ps.get(variable_name)  # Read from Redis
                if value != data[variable_name]:
                    mcu.set(variable_name, value)  # Write to MCU
                    data[variable_name] = value    # Update local cache

                # TODO: resolve conflict if both sources change at once
        except Exception as e:
            print(e)  # Log any exception
            pass      # Continue loop silently
        
    # -----------------------
    # Cleanup MCU connection (unreachable due to infinite loop)
    # -----------------------
    mcu.close()
