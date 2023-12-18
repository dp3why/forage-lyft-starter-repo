import unittest

from tires.carrigan_tires import CarriganTire

class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_worn = [0.3, 0.5, 0.92, 0.9]
        tires_instance = CarriganTire(tire_worn)
        self.assertTrue(tires_instance.needs_service())
        
    def test_needs_service_false(self):
        tire_worn = [0.36, 0.899, 0.88, 0.89]
        tires_instance = CarriganTire(tire_worn)
        self.assertFalse(tires_instance.needs_service())