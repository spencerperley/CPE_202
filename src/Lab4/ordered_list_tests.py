import unittest
from random import randint

from ordered_list import*

class TestLab3(unittest.TestCase):
    def testAdd(self):
        a = OrderedList()
        b = []
        for i in range(0,1000):
            x = randint(0,1000)
            a.add(x)
            b.append(x)
        b.sort()
        self.assertEqual(str(a),str(b))

        c = OrderedList()
        self.assertRaises(TypeError,c.add,"a")
    
    def testRemove(self):
        a = OrderedList()
        for i in range(0,10):
            a.add(i+3)
        a.remove(5)
        a.remove(8)
        a.remove(3)
        a.remove(12)
        self.assertEqual(str(a),'[4, 6, 7, 9, 10, 11]')
        self.assertEqual(a.size(),6)

    def testSearch(self):
        a = OrderedList()
        b = []
        for i in range(0,1000):
            x = randint(0,1000)
            a.add(x)
            b.append(x)
        for i in range(0,200):
            c = randint(1,3000)
            self.assertEqual(a.search_forward(c),c in b)
            self.assertEqual(a.search_backward(c),c in b)
    
    def testPop(self):
        a = OrderedList()
        for i in range(0,10):
            a.add(i+3)

        self.assertEqual(a.pop(),12)
        self.assertEqual(a.pop(),11)
        self.assertEqual(a.pop(0),3)

        
        a = OrderedList()
        b = []
        for i in range(0,1000):
            x = randint(0,1000)
            a.add(x)
            b.append(x)
        b.sort()
        self.assertEqual(a.pop(),b[-1])
        self.assertEqual(a.pop(0),b[0])
        self.assertEqual(a.pop(100),b[101])
        self.assertEqual(a.pop(900),b[902])
        

    def testTrival(self):
        a = OrderedList()
        self.assertTrue(a.is_empty())
        self.assertEqual(a.size(),0)
        a.add(1)
        self.assertFalse(a.is_empty())
        self.assertEqual(a.size(),1)

        a.pop()
        self.assertTrue(a.is_empty())
        self.assertEqual(a.size(),0)



if __name__ == '__main__': 
    unittest.main()
