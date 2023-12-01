import unittest
from datetime import datetime

from serviceable.battery import NubbinBattery, SpindlerBattery
from serviceable.engine import CapuletEngine, SternmanEngine, WillouughbyEngine

class TestNubbinBattery(unittest.TestCase):
    def test_nubbin_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        nubbin_battery = NubbinBattery(last_service_date)
        self.assertTrue(nubbin_battery.needs_service())

    def test_nubbin_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        nubbin_battery = NubbinBattery(last_service_date)
        self.assertFalse(nubbin_battery.needs_service())

class TestSpindlerBattery(unittest.TestCase):
    def test_spindler_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        spindler_battery = SpindlerBattery(last_service_date)
        self.assertTrue(spindler_battery.needs_service())

    def test_spindler_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        spindler_battery = SpindlerBattery(last_service_date)
        self.assertTrue(spindler_battery.needs_service())

class TestCapuletEngine(unittest.TestCase):
    def test_capulet_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        capulet_engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(capulet_engine.needs_service())

    def test_capulet_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0

        capulet_engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(capulet_engine.needs_service())

class TestSternmanEngine(unittest.TestCase):
    def test_sternman_should_be_serviced(self):
        warning_light_is_on = True

        sternman_engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(sternman_engine.needs_service())

    def test_sternman_should_not_be_serviced(self):
        warning_light_is_on = False

        sternman_engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(sternman_engine.needs_service())

class TestWilloughbyEngine(unittest.TestCase):
    def test_willoughby_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        willoughby_engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(willoughby_engine.needs_service())

    def test_willoughby_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0

        willoughby_engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(willoughby_engine.needs_service())


if __name__ == '__main__':
    unittest.main()
