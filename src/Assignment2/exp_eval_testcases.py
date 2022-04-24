import unittest
from exp_eval import * 

class test_expressions(unittest.TestCase):
    def test_invalid(self):
        self.assertFalse(postfix_valid(""))
        self.assertFalse(postfix_valid(" "))
        self.assertFalse(postfix_valid("2 3"))
        self.assertFalse(postfix_valid("2 /"))
        self.assertFalse(postfix_valid("/"))
        self.assertFalse(postfix_valid("2 4 3 /"))
 
    def test_valid(self):
        self.assertTrue(postfix_valid("2 3 +"))
        self.assertTrue(postfix_valid("2 3 -"))
        self.assertTrue(postfix_valid("2 3 *"))
        self.assertTrue(postfix_valid("2 3 /"))



    def test_postfixeval1(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)
        self.assertAlmostEqual(postfix_eval("5"), 5)
        self.assertAlmostEqual(postfix_eval("00.323234 2 +"), 2.323234)

    def test_inToPostBasicAssoc(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")

    def test_inToPostBasicAssoc1(self):
        self.assertEqual(infix_to_postfix("6 - 3 + 2"), "6 3 - 2 +")

    def test_inToPostBasicAssoc2(self):
        self.assertEqual(infix_to_postfix("6 ^ 3 ^ 2"), "6 3 2 ^ ^")

    def test_inToPostBasicAssoc3(self):
        self.assertEqual(infix_to_postfix("6 * ( 3 + 2 )"), "6 3 2 + *")

    def test_inToPostBasicAssoc5(self):
        self.assertEqual(infix_to_postfix("6"), "6")
        with self.assertRaises(ValueError): 
            postfix_eval("3 0 /")
    
    def testFullChain(self):
        self.assertAlmostEqual(postfix_eval(infix_to_postfix("1 + 3 * 2")), 7)
        self.assertAlmostEqual(postfix_eval(infix_to_postfix("( ( ( 1 + ( ( ( 1 + 3 * 2 ) ) ) ) ) )")), 8)
        self.assertAlmostEqual(postfix_eval(infix_to_postfix("( ( ( 1 + ( ( ( 1 + 3 * 2 ) ) + ( 2 ) ) ) ) )")), 10)
        self.assertAlmostEqual(postfix_eval(infix_to_postfix("( 1 + 3 ) ^ 2")), 16)
        self.assertAlmostEqual(postfix_eval(infix_to_postfix("( 1 + 3 ) ^ 2 ^ 3")), 65536)
        self.assertAlmostEqual(postfix_eval(infix_to_postfix("0 ^ 0 + 0 - 0 * 0 - 0")), 1)
        self.assertAlmostEqual(postfix_eval(infix_to_postfix("2")), 2)
        

if __name__ == "__main__":
    unittest.main()
