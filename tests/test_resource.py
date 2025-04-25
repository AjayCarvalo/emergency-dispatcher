import unittest
from resources import Resource

class TestResource(unittest.TestCase):
    def test_marking_resource(self):
        res = Resource("ambulance", "Main Street")
        self.assertTrue(res.available)
        res.mark_assigned("Incident A")
        self.assertFalse(res.available)
        res.mark_available()
        self.assertTrue(res.available)
