import unittest

from tires.octoprime import Octoprime


class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_worn = [0.70, 0.7, 0.7, 0.9]
        tire_instance = Octoprime(tire_worn)
        self.assertTrue(tire_instance.needs_service())


    def test_needs_service_false(self):
        tire_worn = [0.7, 0.7, 0.7, 0.8]
        tire_instance = Octoprime(tire_worn)
        self.assertFalse(tire_instance.needs_service())