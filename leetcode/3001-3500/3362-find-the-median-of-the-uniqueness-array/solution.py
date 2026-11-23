from typing import List
from collections import defaultdict

class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2
        need = (total + 1) // 2

        def count_at_most(x: int) -> int:
            cnt = defaultdict(int)
            distinct = 0
            l = 0
            res = 0
            for r, v in enumerate(nums):
                if cnt[v] == 0:
                    distinct += 1
                cnt[v] += 1
                while distinct > x:
                    u = nums[l]
                    cnt[u] -= 1
                    if cnt[u] == 0:
                        distinct -= 1
                    l += 1
                res += r - l + 1
            return res

        lo, hi = 1, len(set(nums))
        while lo < hi:
            mid = (lo + hi) // 2
            if count_at_most(mid) >= need:
                hi = mid
            else:
                lo = mid + 1
        return lo
