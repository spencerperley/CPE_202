from collections import deque
import unittest
from heap_lab import *

class TestLab7(unittest.TestCase):

    def testBuild(self):
        a=MaxHeap(10)
        self.assertTrue(a.build_heap([6,4,3,10,3,9,2]))


        g = MaxHeap(10)
        g.build_heap([6,4,3,10,3,9,2])
        self.assertEqual(g.popEnd(),2)
        self.assertEqual(g.dequeue(),10)
        self.assertEqual(g.peek(),9)
        
        
        b = MaxHeap(3)
        self.assertTrue(b.is_empty())
        self.assertTrue(b.build_heap([1,2,3]))
        self.assertFalse(b.build_heap([6,8,9,5]))
        self.assertEqual(b.peek(),3)
        self.assertEqual(b.size(),3)
        self.assertTrue(b.is_full())

        d = MaxHeap(10)
        
        # print(d.heap_sort_ascending([6,4,3,10,3,9,2]))

        e = MaxHeap(10)
        self.assertRaises(IndexError, e.dequeue)
        self.assertFalse(e.is_full())
        self.assertEqual(e.size(),0)
        self.assertEqual(e.build_heap([]),True)
        

        





if __name__ == '__main__':
    unittest.main()
    
