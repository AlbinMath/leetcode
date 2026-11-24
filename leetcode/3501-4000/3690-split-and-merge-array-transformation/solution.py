from collections import deque
from typing import List

class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        start, target = tuple(nums1), tuple(nums2)
        if start == target:
            return 0
        n = len(start)
        seen = {start}
        q = deque([(start, 0)])
        while q:
            s, d = q.popleft()
            for L in range(n):
                for R in range(L, n):
                    block = s[L:R + 1]
                    rest = s[:L] + s[R + 1:]
                    for p in range(len(rest) + 1):
                        t = rest[:p] + block + rest[p:]
                        if t == target:
                            return d + 1
                        if t not in seen:
                            seen.add(t)
                            q.append((t, d + 1))
        return -1
