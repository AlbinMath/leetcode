from functools import lru_cache

class Solution:
    def strangePrinter(self, s: str) -> int:
        t = ''.join(c for i, c in enumerate(s) if i == 0 or c != s[i-1])
        n = len(t)

        @lru_cache(None)
        def dp(i, j):
            if i > j:
                return 0
            ans = 1 + dp(i + 1, j)
            for k in range(i + 1, j + 1):
                if t[k] == t[i]:
                    ans = min(ans, dp(i + 1, k - 1) + dp(k, j))
            return ans

        return dp(0, n - 1)
