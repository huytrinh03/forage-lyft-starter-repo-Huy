from abc import ABC
from datetime import datetime as dt

from battery import Battery
class SpindlerBattery(Battery, ABC):
    last_service_date: dt.date
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self):
        delta_time = self.last_service_date - dt.today()
        two_years_in_days = 365 * 2
        if (delta_time.days > two_years_in_days):
            return True
        else:
            return False