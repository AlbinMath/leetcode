from typing import List

class Solution:
    def maxArea(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    if i and j:
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    else:
                        dp[i][j] = 1

        def ok(k: int) -> bool:
            INF = float('inf')
            min_bot_r, max_top_r = INF, -INF
            min_bot_c, max_top_c = INF, -INF
            for i in range(k - 1, m):
                row = dp[i]
                for j in range(k - 1, n):
                    if row[j] >= k:
                        min_bot_r = min(min_bot_r, i)
                        max_top_r = max(max_top_r, i - k + 1)
                        min_bot_c = min(min_bot_c, j)
                        max_top_c = max(max_top_c, j - k + 1)
            return min_bot_r < max_top_r or min_bot_c < max_top_c

        lo, hi = 0, min(m, n)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if ok(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo * lo
