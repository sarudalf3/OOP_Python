import unittest

def reverseList(array):
    return array[::-1]

class ReverseListsTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(reverseList([2,3,4]), [4,3,2])
    def testTwo(self):    
        self.assertNotEqual(reverseList([-1,2,2]), [-1,2,2])
    def testThree(self):
        test01 = reverseList([4,3,7,4]) == [4,7,3,4]
        self.assertTrue(test01)
    def testThree(self):
        test01 = reverseList([4,3,7,4]) == [4,7,3,4]
        self.assertTrue(test01)
    def testFour(self):
        test02 = reverseList([4,3,7,4]) == [4,3,7,4]
        self.assertFalse(test02)
    def setUp(self):
        print("Test reverseList begins")
    def tearDown(self):
        print("Test reverseList finishes")

def palindromo(txt):
    ret = txt[::-1]
    if txt == ret:
        return True
    else:
        return False    

class PalindromoTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(palindromo("racecar"),True)
        self.assertTrue(palindromo("racecar"))
    def testTwo(self):    
        self.assertEqual(palindromo("racb"), False)
        self.assertFalse(palindromo("racb"))
    def testThree(self):
        self.assertEqual(palindromo("kayak"),True)
        self.assertTrue(palindromo("kayak"))
    def testFour(self):
        self.assertEqual(palindromo("mountain"), False)
        self.assertFalse(palindromo("mountain"))
    def testFive(self):
        self.assertEqual(palindromo("stats"),True)
        self.assertTrue(palindromo("stats"))
    def testSix(self):
        self.assertEqual(palindromo("tent"), False)
        self.assertFalse(palindromo("tent"))
    def testSeven(self):
        self.assertEqual(palindromo("book"), False)
        self.assertFalse(palindromo("book"))
    def setUp(self):
        print("Test palindromo begins")
    def tearDown(self):
        print("Test palindromo finishes")

def coins(amount):
    quarter = amount//25
    res = amount % 25
    dime = res // 10
    res = res % 10
    nickel = res // 5
    penny = res % 5
    return [quarter, dime, nickel, penny]    

class CoinTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(coins(12), [0,1,0,2])
    def testTwo(self):    
        self.assertNotEqual(coins(17), [0,1,0,7])
    def testThree(self):
        test01 = coins(24) == [0,2,0,4]
        self.assertTrue(test01)
    def testThree(self):
        test01 = coins(32) == [1,0,1,2] 
        self.assertTrue(test01)
    def testFour(self):
        test02 = coins(99)  == [3,2,0,4]
        self.assertTrue(test02)
    def setUp(self):
        print("Test coinList begins")
    def tearDown(self):
        print("Test coinList finishes")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

class FactorialTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(factorial(5), 120)
    def testTwo(self):    
        self.assertEqual(factorial(0), 1)
    def testThree(self):
        test01 = factorial(4) == 24
        self.assertTrue(test01)
    def testFour(self):
        test01 = factorial(6) == 720 
        self.assertTrue(test01)
    def testFive(self):
        test02 = factorial(2) == 2
        self.assertTrue(test02)
    def setUp(self):
        print("Test factorial begins")
    def tearDown(self):
        print("Test factorial finishes")

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

class FibonacciTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(fibonacci(5), 3)
    def testTwo(self):    
        self.assertEqual(fibonacci(9), 21)
    def testThree(self):
        test01 = fibonacci(1) == 0
        self.assertTrue(test01)
    def testFour(self):
        test01 = fibonacci(3) == 1 
        self.assertTrue(test01)
    def testFive(self):
        test02 = fibonacci(13) == 144
        self.assertTrue(test02)
    def setUp(self):
        print("Test fibonacci begins")
    def tearDown(self):
        print("Test fibonacci finishes")

if __name__ == '__main__':
    unittest.main()
