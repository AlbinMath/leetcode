from math import gcd
class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        g = gcd(*numsDivide)
        for i, x in enumerate(sorted(nums)):
            if g % x == 0: return i
        return -1
