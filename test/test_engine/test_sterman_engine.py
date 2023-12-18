import unittest
from engine.sternman_engine import SternmanEngine

class TestStermanEngine(unittest.TestCase):
    def test_needs_service_true(self):
        warning_light_is_on = True
        engine_instance = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine_instance.needs_service())

    def test_needs_service_false(self):
        warning_light_is_on = False
        engine_instance = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine_instance.needs_service())
