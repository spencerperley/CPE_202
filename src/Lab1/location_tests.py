# CPE 202 Location Class Test Cases, Lab 1

import unittest
from location import *

class TestLocation(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        loc = Location(None, None, None)
        self.assertNotEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    def test_equals(self):
        loc = Location("SLO", 35.3, -120.7)
        loc1 = Location("SLO", 35.3, -120.7)
        self.assertTrue(loc == loc1)
        loc1 = Location("SLO", 35.2, -120.7)
        self.assertFalse(loc == loc1)
    
    def test_init(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc.name,"SLO")
        
    


if __name__ == "__main__":
        unittest.main()

