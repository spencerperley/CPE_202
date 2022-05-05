import unittest
from random import randint

from binary_search_tree import*

class TestLab3(unittest.TestCase):
    # def testinsrt(self):
    #     a = BinarySearchTree(0)
    #     b = [0]
    #     for i in range(1000):
    #         val = randint(-50,50)
    #         a.insert(val)
    #         b.append(val)
    #     c=[i.key for i in a.root.inorder()]
    #     self.assertEqual(c,sorted(b))

    #     a = BinarySearchTree(10)
    #     b = [10]
    #     for i in range(1000):
    #         val = randint(-50,50)
    #         a.insert(val)
    #         b.append(val)
    #     c=[i.key for i in a.root.inorder()]
    #     self.assertEqual(c,sorted(b))

        
    #     a = BinarySearchTree(-15)
    #     b = [-15]
    #     for i in range(1000):
    #         val = randint(-50,50)
    #         a.insert(val)
    #         b.append(val)

    #     for i in range(-51,51):
    #         self.assertEqual(a.find(i),i in b)

    def testremove(self):
        a = BinarySearchTree(6)
        b = [1,2,5,8,4,9,3]
        for i in b:
            a.insert(i)
        b.append(6)
        a.delete(5)
        b.remove(5)

        c=[i.key for i in a.root.inorder()]
        self.assertEqual(c,sorted(b))

        a.delete(6)
        b.remove(6)
        c=[i.key for i in a.root.inorder()]
        self.assertEqual(c,sorted(b))

        a = BinarySearchTree(6)
        b = [6]
        for i in range(1000):
            val = randint(-50,50)
            a.insert(val)
            b.append(val)
        for i in range(500):
            val = b[randint(0,1000-i)]
            a.delete(val)
            b.remove(val)
            c=[i.key for i in a.root.inorder()]
            self.assertEqual(c,sorted(b))
            

        



if __name__ == '__main__': 
    unittest.main()
