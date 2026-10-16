from typing import List

class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        m = max(nums)
        p = list(range(m + 1))
        def f(x):
            while p[x] != x:
                p[x] = p[p[x]]
                x = p[x]
            return x
        for x in nums:
            y, d = x, 2
            while d * d <= y:
                if y % d == 0:
                    p[f(x)] = f(d)
                    while y % d == 0: y //= d
                d += 1
            if y > 1: p[f(x)] = f(y)
        for a, b in zip(nums, sorted(nums)):
            if f(a) != f(b): return False
        return True
