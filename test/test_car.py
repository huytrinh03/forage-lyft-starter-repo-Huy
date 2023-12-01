import unittest
from datetime import datetime

from serviceable.battery import nubbin_battery.NubbinBattery, spindler_battery.SpindlerBattery
from serviceable.engine import capulet_engine.CapuletEngine, sternman_engine.SternmanEngine, willoughby_engine.WillouughbyEngine
from serviceable.tire import carrigan_tire.CarriganTire, octoprime_tire.OctoprimeTire

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
        last_service_date = today.replace(year=today.year - 2)
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
        self.assertFalse(spindler_battery.needs_service())

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

class TestCarriganTire(unittest.TestCase):
    def test_carrigan_should_be_serviced(self):
        sensor_output = [0.1, 0.1, 0.1, 0.9]

        carrigan_tire = CarriganTire(sensor_output)
        self.assertTrue(carrigan_tire.needs_service())

    def test_willoughby_should_not_be_serviced(self):
        sensor_output = [0.1, 0.1, 0.1, 0.8]

        carrigan_tire = CarriganTire(sensor_output)
        self.assertFalse(carrigan_tire.needs_service())

class TestOctoprimeTire(unittest.TestCase):
    def test_octoprime_should_be_serviced(self):
        sensor_output = [0.6, 0.7, 0.8, 0.9]

        octoprime_tire = OctoprimeTire(sensor_output)
        self.assertTrue(octoprime_tire.needs_service())

    def test_octoprime_should_not_be_serviced(self):
        sensor_output = [0.6, 0.7, 0.8, 0.8]

        octoprime_tire = OctoprimeTire(sensor_output)
        self.assertFalse(octoprime_tire.needs_service())

if __name__ == '__main__':
    unittest.main()
