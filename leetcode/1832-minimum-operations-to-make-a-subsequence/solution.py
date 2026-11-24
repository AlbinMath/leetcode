from bisect import bisect_left
from typing import List

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        pos = {v: i for i, v in enumerate(target)}
        tails = []

        for v in arr:
            if v in pos:
                p = pos[v]
                k = bisect_left(tails, p)
                if k == len(tails):
                    tails.append(p)
                else:
                    tails[k] = p

        return len(target) - len(tails)
