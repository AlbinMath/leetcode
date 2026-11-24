from collections import Counter
from typing import List

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        cnt = Counter()
        for w in words:
            m = 0
            for ch in w:
                m |= 1 << (ord(ch) - 97)
            cnt[m] += 1

        ans = []
        for p in puzzles:
            first = 1 << (ord(p[0]) - 97)
            rest = 0
            for ch in p[1:]:
                rest |= 1 << (ord(ch) - 97)

            total = 0
            sub = rest
            while True:
                total += cnt.get(sub | first, 0)
                if sub == 0:
                    break
                sub = (sub - 1) & rest
            ans.append(total)
        return ans
