from serviceable import *
from datetime import datetime as dt
class CarFactory:
    def create_calliope(self, current_mileage, last_service_mileage, last_service_date):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date)
        return Car(engine, battery)

    def create_glissade(self, current_mileage, last_service_mileage, last_service_date):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date)
        return Car(engine, battery)

    def create_palindrome(self, warning_light_on, last_service_date):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date)
        return Car(engine, battery)

    def create_rorschach(self, current_mileage, last_service_mileage, last_service_date):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date)
        return Car(engine, battery)

    def create_calliope(self, current_mileage, last_service_mileage, last_service_date):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date)
        return Car(engine, battery)