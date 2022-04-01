# CPE 202 Lab 1 Test Cases


import unittest
from lab1 import *
from random import randint

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """Tests the max list iterator function for a variety of different cases"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        
        tlist = [4,2,3,5]
        self.assertEqual(max_list_iter(tlist),5)
        
        tlist = [4,2,314,3,5]
        self.assertEqual(max_list_iter(tlist),314)

        tlist = []
        self.assertEqual(max_list_iter(tlist),None)        
        
        

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertNotEqual(reverse_rec([1,4,3]),[1,4,3])
        self.assertEqual(reverse_rec([]),[])
        
        tlist = None
        with self.assertRaises(ValueError):
            reverse_rec(tlist)

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]

        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
        self.assertEqual(bin_search(9, 0, len(list_val)-1, list_val), 7 )
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 8 )
        self.assertEqual(bin_search(10, 1, len(list_val)-1, list_val), 8 )
        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 0)
        self.assertEqual(bin_search(1, 0, len(list_val)-1, list_val), 1)
        self.assertEqual(bin_search(1, 1, len(list_val)-1, list_val), 1)
        self.assertEqual(bin_search(5, 0, len(list_val)-1, list_val), None )   
        
        list_val =[0,2,3,4,7,8,9,10]
          
        self.assertEqual(bin_search(2, 3, len(list_val)-1, list_val), None ) 
           
        tlist = None
        with self.assertRaises(ValueError):
            bin_search(2, 3, 0, tlist)
            
        
            
        
        

if __name__ == "__main__":
        unittest.main()
