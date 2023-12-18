import unittest

from engine.willoughby_engine import WilloughbyEngine


class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 91101
        last_service_mileage = 31100
        engine_instance = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine_instance.needs_service())

    def test_needs_service_false(self):
        current_mileage = 91101
        last_service_mileage = 31101
        engine_instance = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine_instance.needs_service())