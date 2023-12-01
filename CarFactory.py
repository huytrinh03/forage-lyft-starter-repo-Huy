from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire
from car import Car


class CarFactory:
    def create_calliope(self, current_mileage, last_service_mileage, last_service_date, sensor_output):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date)
        tire = CarriganTire(sensor_output)
        return Car(engine, battery, tire)

    def create_glissade(self, current_mileage, last_service_mileage, last_service_date, sensor_output):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date)
        tire = CarriganTire(sensor_output)
        return Car(engine, battery, tire)

    def create_palindrome(self, warning_light_on, last_service_date, sensor_output):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date)
        tire = CarriganTire(sensor_output)
        return Car(engine, battery, tire)

    def create_rorschach(self, current_mileage, last_service_mileage, last_service_date, sensor_output):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date)
        tire = OctoprimeTire(sensor_output)
        return Car(engine, battery, tire)

    def create_thovex(self, current_mileage, last_service_mileage, last_service_date, sensor_output):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date)
        tire = OctoprimeTire(sensor_output)
        return Car(engine, battery, tire)
