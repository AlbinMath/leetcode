from typing import List
from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        best = -1
        for a, b, c, d in permutations(arr):
            h = a * 10 + b
            m = c * 10 + d
            if h < 24 and m < 60:
                best = max(best, h * 60 + m)
        if best < 0:
            return ""
        return f"{best // 60:02d}:{best % 60:02d}"
