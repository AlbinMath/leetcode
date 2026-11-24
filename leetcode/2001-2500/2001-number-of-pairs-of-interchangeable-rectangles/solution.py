from typing import List
from math import gcd
from collections import defaultdict

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        cnt = defaultdict(int)
        ans = 0
        for w, h in rectangles:
            g = gcd(w, h)
            key = (w // g, h // g)
            ans += cnt[key]
            cnt[key] += 1
        return ans
