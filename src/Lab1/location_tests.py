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
    
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
