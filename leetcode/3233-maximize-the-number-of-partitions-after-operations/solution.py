import sys
from functools import lru_cache

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        sys.setrecursionlimit(30000)
        n = len(s)

        @lru_cache(maxsize=None)
        def dfs(i: int, mask: int, can_change: bool) -> int:
            if i == n:
                return 1

            bit = 1 << (ord(s[i]) - 97)
            nm = mask | bit
            if nm.bit_count() > k:
                res = dfs(i + 1, bit, can_change) + 1
            else:
                res = dfs(i + 1, nm, can_change)

            if can_change:
                for j in range(26):
                    b = 1 << j
                    nm = mask | b
                    if nm.bit_count() > k:
                        res = max(res, dfs(i + 1, b, False) + 1)
                    else:
                        res = max(res, dfs(i + 1, nm, False))
            return res

        return dfs(0, 0, True)
