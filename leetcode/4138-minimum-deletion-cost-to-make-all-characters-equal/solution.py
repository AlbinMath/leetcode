from typing import List

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        per = [0] * 26
        for ch, c in zip(s, cost):
            per[ord(ch) - 97] += c
        return sum(cost) - max(per)
