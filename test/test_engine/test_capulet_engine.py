import unittest

from engine.capulet_engine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 61256
        last_service_mileage = 31002
        engine_instance = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine_instance.needs_service())
    
    def test_needs_service_false(self):
        current_mileage = 61256
        last_service_mileage = 31256
        engine_instance = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine_instance.needs_service())
