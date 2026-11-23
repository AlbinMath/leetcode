from typing import List
from math import gcd
from functools import reduce

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        if 1 in nums: return False
        p = list(range(max(nums) + 1))
        def f(x):
            if p[x] != x: p[x] = f(p[x])
            return p[x]
        for x in nums:
            for i in range(2, int(x**0.5) + 1):
                if x % i == 0:
                    p[f(x)] = f(i)
                    p[f(x)] = f(x // i)
        for x in nums:
            for i in range(2, int(x**0.5) + 1):
                if x % i == 0:
                    p[f(x)] = f(i)
                    p[f(x)] = f(x // i)
        return len({f(x) for x in nums}) == 1
