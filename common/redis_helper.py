

class ParameterStore:
    def __init__(self):
        pass

    def get(self, parameter):
        return "test"

    def set(self, parameter, value):
        print(f"{parameter} is now {value}")
