import unittest
from incident import Incident

class TestIncident(unittest.TestCase):
    def test_priority_update(self):
        inc = Incident("fire", "Park", 3, ["fire_truck"])
        inc.update_priority(1)
        self.assertEqual(inc.priority, 1)
