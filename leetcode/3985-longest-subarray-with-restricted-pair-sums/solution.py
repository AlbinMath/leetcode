from typing import List

class Solution:
    def maxSubarray(self, nums: List[int]) -> int:
        MAXV = 500
        last = [-1] * (2 * MAXV + 2)
        last2 = [-1] * (2 * MAXV + 2)
        L = -1
        best = 0
        for r, x in enumerate(nums):
            m = -1
            # r is the sum element: a + b == x
            for a in range(1, x):
                b = x - a
                if a > b:
                    break
                if a == b:
                    cand = last2[a]
                else:
                    cand = min(last[a], last[b])
                if cand >= 0 and cand > m:
                    m = cand
            # r is an addend: x + b == nums[k]
            for b in range(1, MAXV + 1):
                s = x + b
                if s > MAXV:
                    break
                j, k = last[b], last[s]
                if j >= 0 and k >= 0:
                    c = min(j, k)
                    if c > m:
                        m = c
            if m > L:
                L = m
            best = max(best, r - L)
            last2[x] = last[x]
            last[x] = r
        return best
