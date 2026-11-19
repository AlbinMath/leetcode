from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        best = {}  # mask -> longest word length with that mask
        for w in words:
            m = 0
            for ch in w:
                m |= 1 << (ord(ch) - 97)
            if len(w) > best.get(m, 0):
                best[m] = len(w)

        items = list(best.items())
        ans = 0
        for i in range(len(items)):
            mi, li = items[i]
            for j in range(i + 1, len(items)):
                mj, lj = items[j]
                if mi & mj == 0:
                    ans = max(ans, li * lj)
        return ans
