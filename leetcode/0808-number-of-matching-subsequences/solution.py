from collections import defaultdict
from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = defaultdict(list)
        for w in words:
            waiting[w[0]].append((w, 0))

        count = 0
        for ch in s:
            bucket = waiting.pop(ch, [])
            for w, i in bucket:
                i += 1
                if i == len(w):
                    count += 1
                else:
                    waiting[w[i]].append((w, i))
        return count
