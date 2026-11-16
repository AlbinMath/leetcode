from typing import List
from math import gcd

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            l = 1
            for j in range(i, n):
                x = nums[j]
                if k % x:
                    break  # x doesn't divide k, so the LCM can never equal k
                l = l * x // gcd(l, x)
                if l == k:
                    ans += 1
                elif l > k:
                    break
        return ans
