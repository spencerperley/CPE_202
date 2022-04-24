import unittest
from queue_array import *

class TestLab3(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        q.dequeue()
        q.size()

    def test_init(self):
        q1 = Queue(5)
        self.assertEqual(q1.num_items,0)
        self.assertEqual(q1.items,[None]*5)
        self.assertEqual(q1.front, 0)
        self.assertEqual(q1.rear, 0)
        q2 = Queue(5, [1,2])
        self.assertEqual(q2.num_items,2)
        self.assertEqual(q2.items,[1, 2, None, None, None])
        self.assertEqual(q2.front, 0)
        self.assertEqual(q2.rear, 2)


    def test_examples(self):
        q1 = Queue(5)
        self.assertTrue(q1.is_empty())
        self.assertFalse(q1.is_full())
        q1.enqueue(1)
        q1.enqueue(2)
        q1.enqueue(3)
        q2 = Queue(5, [1,2])
        q2.enqueue(3)
        self.assertEqual(q1, q2)


        q2 = Queue(10)
        q2.enqueue(2)
        q2.enqueue(3)
        self.assertEqual(q2.dequeue(),2)
        self.assertEqual(q2.dequeue(),3)
        self.assertRaises(IndexError,q2.dequeue)
        q2 = Queue(10)
        self.assertRaises(IndexError,q2.dequeue)
        q2.enqueue(2)
        q2.enqueue(3)
        q2.dequeue()
        q2.dequeue()
        self.assertRaises(IndexError,q2.dequeue)
        q2.enqueue(0)
        q2.enqueue(1)
        q2.enqueue(2)
        q2.enqueue(3)
        q2.enqueue(4)
        q2.enqueue(5)
        q2.enqueue(6)
        q2.enqueue(7)
        q2.enqueue(8)
        q2.enqueue(9)
        self.assertRaises(IndexError,q2.enqueue,10)
        self.assertEqual(q2.dequeue(),0)
        self.assertEqual(q2.dequeue(),1)
        self.assertEqual(q2.dequeue(),2)
        q2.enqueue(8)
        self.assertEqual(q2.dequeue(),3)

if __name__ == '__main__': 
    unittest.main()
