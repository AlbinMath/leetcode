from typing import List
from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        n = len(s)
        maxlen = max(len(w) for w in words)

        @lru_cache(maxsize=None)
        def solve(i):
            if i == n:
                return [""]
            res = []
            for j in range(i + 1, min(n, i + maxlen) + 1):
                w = s[i:j]
                if w in words:
                    for rest in solve(j):
                        res.append(w + (" " + rest if rest else ""))
            return res

        return solve(0)
