from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        best = 0

        for S in {nums[0] + nums[1], nums[-1] + nums[-2], nums[0] + nums[-1]}:
            # dp[i][j] for i <= j; out-of-range or i >= j gives 0
            dp = [[0] * (n + 2) for _ in range(n + 2)]
            for i in range(n - 1, -1, -1):
                for j in range(i + 1, n):
                    r = 0
                    if nums[i] + nums[i + 1] == S:
                        r = max(r, 1 + (dp[i + 2][j] if i + 2 <= j else 0))
                    if nums[j - 1] + nums[j] == S:
                        r = max(r, 1 + (dp[i][j - 2] if i <= j - 2 else 0))
                    if nums[i] + nums[j] == S:
                        r = max(r, 1 + (dp[i + 1][j - 1] if i + 1 <= j - 1 else 0))
                    dp[i][j] = r
            best = max(best, dp[0][n - 1])
        return best
