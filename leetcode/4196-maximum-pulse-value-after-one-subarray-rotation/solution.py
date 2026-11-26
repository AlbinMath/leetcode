from typing import List

class Solution:
    def maxValue(self, nums: List[int]) -> int:
        n = len(nums)
        P = [0] * (n + 1)
        for i, v in enumerate(nums):
            P[i + 1] = P[i] + (v if i % 2 == 0 else -v)
        base = P[n]

        best_gain = 0
        NEG = float('-inf')
        mx = [NEG, NEG]  # max P[l] per index parity, over l <= e - 2
        for e in range(2, n + 1):
            l = e - 2
            mx[l % 2] = max(mx[l % 2], P[l])
            if mx[e % 2] > NEG:
                best_gain = max(best_gain, 2 * (mx[e % 2] - P[e]))

        return base + best_gain
