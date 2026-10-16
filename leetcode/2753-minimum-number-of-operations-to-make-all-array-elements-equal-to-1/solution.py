from math import gcd
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n, c = len(nums), nums.count(1)
        if c: return n - c
        if gcd(*nums) > 1: return -1
        m = n
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == 1: m = min(m, j - i + 1); break
        return m + n - 2
