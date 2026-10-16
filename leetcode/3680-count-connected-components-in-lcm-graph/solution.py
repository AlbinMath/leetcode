from math import gcd
from functools import reduce

class Solution:
    def countComponents(self, nums: List[int], threshold: int) -> int:
        p = list(range(threshold + 1))
        def f(x):
            while p[x] != x:
                p[x] = p[p[x]]
                x = p[x]
            return x
        for x in nums:
            if x <= threshold:
                for y in range(x, threshold + 1, x):
                    if y + x - gcd(y, x) <= threshold:
                        a, b = f(x), f(y)
                        p[a] = b
        return len(set(f(x) for x in nums if x <= threshold)) + sum(x > threshold for x in nums)
