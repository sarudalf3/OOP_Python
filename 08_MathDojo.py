import functools
from math import sqrt

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

md = MathDojo()
md.add(5)
md.add(5,3)
print(md.add(5,3,2))
print(md.substract(5,3,25))

md2 = MathDojo()
x = md2.add(2).add(2,5,1).substract(3,8).result
print(x)

md3 = MathDojo()
print(md3.std(1,2,3,4))

md4 = MathDojo()
md4.add(2,3,6)
md4.add(2,5)
print(md4.result)