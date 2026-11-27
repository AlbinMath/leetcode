from typing import List

class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        m = len(slices)
        n = m // 3

        def solve(a: List[int]) -> int:
            L = len(a)
            NEG = float('-inf')
            # dp[i][j]: first i slices, exactly j chosen, no two adjacent
            dp = [[NEG] * (n + 1) for _ in range(L + 1)]
            for i in range(L + 1):
                dp[i][0] = 0
            for i in range(1, L + 1):
                for j in range(1, n + 1):
                    best = dp[i - 1][j]
                    prev = dp[i - 2][j - 1] if i >= 2 else (0 if j == 1 else NEG)
                    if prev != NEG:
                        best = max(best, prev + a[i - 1])
                    dp[i][j] = best
            return dp[L][n]

        return max(solve(slices[:-1]), solve(slices[1:]))
