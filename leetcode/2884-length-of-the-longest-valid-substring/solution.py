from typing import List

class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        bad = set(forbidden)
        n = len(word)
        left = 0
        ans = 0
        for r in range(n):
            lo = max(left, r - 9)
            for i in range(r, lo - 1, -1):
                if word[i:r + 1] in bad:
                    left = i + 1
                    break
            ans = max(ans, r - left + 1)
        return ans
