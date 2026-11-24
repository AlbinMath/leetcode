from typing import List
from math import gcd
from collections import defaultdict

class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = defaultdict(int)
        ans = 0

        for r in range(4, n - 2):
            q = r - 2
            for p in range(q - 1):          # p <= q - 2
                g = gcd(nums[p], nums[q])
                cnt[(nums[p] // g, nums[q] // g)] += 1
            for s in range(r + 2, n):
                g = gcd(nums[s], nums[r])
                ans += cnt.get((nums[s] // g, nums[r] // g), 0)

        return ans
