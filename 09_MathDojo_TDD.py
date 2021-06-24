import functools
from math import sqrt
import unittest

#MathDojo class
class MathDojo:
    def __init__(self):
        self.result = 0
    
    def add(self, num, *nums):
        if len(nums)>0:
            tot_sum=functools.reduce(lambda a, b: a+b, nums)
        else:
            tot_sum = 0
        self.result += num + tot_sum
        return self
    
    def substract(self, num, *nums):
        if len(nums)>0:
            tot_subs=functools.reduce(lambda a, b: a+b, nums)
        else:
            tot_subs = 0
        self.result -= (num + tot_subs)
        return self

    def std(self, num, *nums):
        #result is a date to calculate std and insert in a array to calculate the standard desviation
        arr = [self.result, num] + list(nums)
        mean = sum(arr)/len(arr)
        arr = [(x - mean)**2 for x in arr]
        self.result = sqrt(sum(arr)/(len(arr)-1))
        return self

    def __str__(self):
        return f"the result is {self.result}"

tst01 = MathDojo()
tst02 = MathDojo()
tst03 = MathDojo()
tst04 = MathDojo()
tst05 = MathDojo()
tst06 = MathDojo()
    
class MathDojoTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(tst01.add(2,3,6).result, 11)
    def testTwo(self):
        self.assertEqual(tst01.substract(7).result, 9) #The second one
    def testThree(self):
        self.assertEqual(tst01.add(4,1).result, 16) #this test is next to testOne
    def testFour(self):
        self.assertEqual(tst02.substract(4,-1).result, -3)
    def testFive(self):
        self.assertEqual(tst03.add(4).add(2).add(-1).substract(-5).result, 10)
    def testSix(self):
        self.assertEqual(tst04.std(2).result, sqrt(2))
    def testSeven(self):
        self.assertEqual(tst05.std(1,2,3,4).result, sqrt(5/2))
    def testEight(self):
        self.assertEqual(tst06.add(4).add(2).add(-1).std(4,3).result, 1)

    def setUp(self):
        print("running test to add, substract and std to numbers")

    def tearDown(self):
        print("End of tests")

if __name__ == '__main__':
    unittest.main()

