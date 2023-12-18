import unittest
from datetime import date

from battery.spindler_battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2021-05-12")
        last_service_date = date.fromisoformat("2016-11-22")
        battery_instance = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery_instance.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2021-05-12")
        last_service_date = date.fromisoformat("2020-11-22")
        battery_instance = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery_instance.needs_service())