from abc import ABC

from tire import Tire


class CarriganBattery(Tire, ABC):
    sensor_output: list

    def __init__(self, sensor_output):
        self.sensor_output = sensor_output

    def needs_service(self):
        for worn_index in self.sensor_output:
            if (worn_index >= 0.9):
                return True
        return False
