from typing import List

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = {}
        ans = 1
        for x in nums:
            # use x+1 first (reads dp[x] before it is modified by this element)
            dp[x + 1] = dp.get(x, 0) + 1
            # then use x
            dp[x] = dp.get(x - 1, 0) + 1
            ans = max(ans, dp[x], dp[x + 1])
        return ans
