from typing import List
from math import gcd

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == k:
                    ans += 1
                elif g < k:
                    break  # gcd only shrinks, so it can't return to k
        return ans
