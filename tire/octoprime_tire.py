from abc import ABC

from tire import Tire
class OctoprimeTire(Tire, ABC):
    sensor_output: list
    def __init__(self, sensor_output):
        self.sensor_output = sensor_output

    def needs_service(self):
        sum = 0
        for worn_index in self.sensor_output:
            sum += worn_index
        if sum >= 3:
            return True
        else:
            return False