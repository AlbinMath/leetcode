from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        NEG = float('-inf')
        dp = [0, NEG, NEG]
        for x in nums:
            new = dp[:]
            for r in range(3):
                if dp[r] != NEG:
                    nr = (r + x) % 3
                    new[nr] = max(new[nr], dp[r] + x)
            dp = new
        return dp[0]
