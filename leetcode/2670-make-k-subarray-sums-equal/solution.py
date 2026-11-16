from typing import List
from math import gcd

class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        n = len(arr)
        g = gcd(n, k)
        ans = 0
        for r in range(g):
            group = sorted(arr[r::g])
            med = group[len(group) // 2]
            ans += sum(abs(x - med) for x in group)
        return ans
