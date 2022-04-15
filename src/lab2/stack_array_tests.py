import unittest
from stack_array import Stack
        
class TestLab2(unittest.TestCase):

    def test_init(self):
        stack = Stack(5)
        self.assertEqual(stack.items, [None]*5)
        self.assertEqual(stack.capacity, 5)

        stack = Stack(5, [1, 2])
        self.assertEqual(stack.items[0:2], [1, 2])
        self.assertEqual(stack.capacity, 5)

        with self.assertRaises(IndexError):
            Stack(5, [1, 2, 3, 4, 5, 6])
            

    def test_eq(self):
        stack1 = Stack(5)
        stack2 = Stack(5)
        stack3 = Stack(10)
        stack4 = Stack(5,[1, 2])
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack3)
        self.assertNotEqual(stack1, stack4)

    def test_repr(self):
        stack = Stack(5, [1, 2])
        self.assertEqual(stack.__repr__(), "Stack(5, [1, 2])")

# WRITE TESTS FOR STACK OPERATIONS - PUSH, POP, PEEK, etc.

    def test_push_and_empty(self):
        init_stack = Stack(10)
        init_stack.push(3)
        self.assertFalse(init_stack.is_empty())
        self.assertEqual(init_stack.peek(),3)

    def test_pop(self):
        ints = Stack(10)
        ints.push(3)
        self.assertEqual(3,ints.pop())
        ints = Stack(10)
        ints.push(3)
        ints.pop()
        self.assertRaises(IndexError, ints.pop)

    def testSize(self):
        ints = Stack(10)
        ints.push(3)
        ints.pop()
        ints.push(2974)
        ints.push(3)
        self.assertEqual(ints.size(),2)
    
    def testCapacity(self):
        ints = Stack(3)
        ints.push(3)
        ints.push(5)
        ints.push(2)
        self.assertRaises(IndexError,ints.push,2)
        ints.pop()
        ints.push(2)
        self.assertEqual(3,ints.size())
        
        

if __name__ == '__main__': 
    unittest.main()
