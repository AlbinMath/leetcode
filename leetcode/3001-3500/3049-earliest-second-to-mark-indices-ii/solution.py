import heapq
from typing import List

class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n, m = len(nums), len(changeIndices)
        base = sum(nums) + n          # cost if every index is handled "plain"

        def can(T: int) -> bool:
            first = {}
            for s in range(T):
                first.setdefault(changeIndices[s], s)

            heap = []                 # values of indices currently chosen to be zeroed
            cnt = 0                   # free seconds to the right, usable as mark seconds
            saved = 0                 # sum of (v - 1) over zeroed indices
            for s in range(T - 1, -1, -1):
                i = changeIndices[s]
                v = nums[i - 1]
                if first[i] != s or v <= 1:
                    cnt += 1
                elif cnt > 0:
                    cnt -= 1
                    heapq.heappush(heap, v)
                    saved += v - 1
                elif heap and heap[0] < v:
                    small = heapq.heapreplace(heap, v)
                    saved += v - small
                    cnt += 1          # fix: freed mark slot + freed set second - new mark slot
                else:
                    cnt += 1
            return base - saved <= T

        if not can(m):
            return -1

        lo, hi = 1, m
        while lo < hi:
            mid = (lo + hi) // 2
            if can(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
