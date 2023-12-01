from abc import ABC
from datetime import datetime as dt

from battery import Battery
class NubbinBattery(Battery, ABC):
    last_service_date: dt.date
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self):
        delta_time = self.last_service_date - dt.today()
        four_years_in_days = 365 * 3 + 366
        if (delta_time.days > four_years_in_days):
            return True
        else:
            return False