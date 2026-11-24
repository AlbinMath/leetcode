from bisect import bisect_left
from typing import List

class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        n = len(damage)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + damage[i]

        ans = 0
        for i in range(1, n + 1):                 # room i (1-indexed)
            t = requirement[i - 1] + pre[i] - hp
            k = bisect_left(pre, t, 0, i)         # smallest k in [0, i-1] with pre[k] >= t
            ans += i - k                          # k can be i (none valid) -> adds 0
        return ans
