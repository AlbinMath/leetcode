from typing import List

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows = {}
        for i, row in enumerate(grid):
            for v in row:
                rows.setdefault(v, set()).add(i)

        dp = [-1] * (1 << n)
        dp[0] = 0
        for v, rs in rows.items():
            new = dp[:]
            for mask in range(1 << n):
                if dp[mask] < 0:
                    continue
                for r in rs:
                    if not mask >> r & 1:
                        nm = mask | (1 << r)
                        if dp[mask] + v > new[nm]:
                            new[nm] = dp[mask] + v
            dp = new
        return max(dp)
