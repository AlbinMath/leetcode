from typing import List
from collections import defaultdict

class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        dsum = 0
        l = 0
        best = float('inf')
        for r, x in enumerate(nums):
            if cnt[x] == 0:
                dsum += x
            cnt[x] += 1
            while dsum >= k:
                best = min(best, r - l + 1)
                y = nums[l]
                cnt[y] -= 1
                if cnt[y] == 0:
                    dsum -= y
                l += 1
        return -1 if best == float('inf') else best
