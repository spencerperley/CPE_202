from mimetypes import init
import unittest
from stack_nodelist import *
        
class TestLab2(unittest.TestCase):
    

    def test_node_init(self):
        node1 = Node(1, None)
        self.assertEqual(node1.value, 1)
        self.assertEqual(node1.rest, None)

        node2 = Node(2, node1)
        self.assertEqual(node2.value, 2)
        self.assertEqual(node2.rest, node1)

    def test_node_eq(self):
        node1a = Node(1, None)
        node1b = Node(1, None)
        node2a = Node(2, node1a)
        node2b = Node(2, node1b)

        self.assertEqual(node1a, node1b)
        self.assertNotEqual(node1a, node2a)
        self.assertEqual(node2a, node2b)
        node1a = Node(3, None)
        self.assertNotEqual(node1a, node1b)

    def test_node_repr(self):
        node = Node(2, Node(1, None))
        self.assertEqual(node.__repr__(), "Node(2, Node(1, None))")

    def test_stack_init(self):
        stack = Stack()
        self.assertEqual(stack.top, None)

        init_stack = Node(2, Node(1, None))
        stack = Stack(init_stack)
        self.assertEqual(stack.top, init_stack)

    def test_stack_eq(self):
        stack1 = Stack()
        stack2 = Stack()
        init_stack = Node(2, Node(1, None))
        stack4 = Stack(init_stack)
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack4)

    def test_stack_repr(self):
        init_stack = Node(2, Node(1, None))
        stack = Stack(init_stack)
        self.assertEqual(stack.__repr__(), "Stack(Node(2, Node(1, None)))")

    def test_push_and_empty(self): # same tests as array implementation as the same functionality is needed
        init_stack = Stack()
        init_stack.push(3)
        self.assertFalse(init_stack.is_empty())
        self.assertEqual(init_stack.top.value,init_stack.peek())
        self.assertEqual(init_stack.top.value,3)

    def test_pop(self):
        ints = Stack()
        ints.push(3)
        self.assertEqual(ints.top.value,ints.pop())
        ints = Stack()
        ints.push(3)
        ints.pop()
        self.assertRaises(IndexError, ints.pop)
    def testSize(self):
        ints = Stack()
        ints.push(3)
        ints.pop()
        ints.push(2974)
        ints.push(3)
        self.assertEqual(ints.size(),2)
        



# WRITE TESTS FOR STACK OPERATIONS - PUSH, POP, PEEK, etc.


if __name__ == '__main__': 
    unittest.main()
