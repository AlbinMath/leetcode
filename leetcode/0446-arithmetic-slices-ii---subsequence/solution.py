from typing import List
from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        ans = 0
        for j in range(n):
            for i in range(j):
                d = nums[j] - nums[i]
                c = dp[i].get(d, 0)
                ans += c
                dp[j][d] += c + 1
        return ans
