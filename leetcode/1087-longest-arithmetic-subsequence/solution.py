from typing import List

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        OFFSET = 500
        dp = [[1] * 1001 for _ in range(n)]   # dp[i][d + OFFSET], default length 1
        best = 2

        for i in range(n):
            for j in range(i):
                d = nums[i] - nums[j] + OFFSET
                dp[i][d] = dp[j][d] + 1
                best = max(best, dp[i][d])

        return best
