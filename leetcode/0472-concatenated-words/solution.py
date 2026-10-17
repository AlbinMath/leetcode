from typing import List

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        seen = set()
        res = []

        def can_form(w):
            if not seen:
                return False
            n = len(w)
            dp = [False] * (n + 1)
            dp[0] = True
            for i in range(1, n + 1):
                for j in range(i):
                    if dp[j] and w[j:i] in seen:
                        dp[i] = True
                        break
            return dp[n]

        for w in words:
            if can_form(w):
                res.append(w)
            seen.add(w)
        return res
