from typing import List

class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n, m = len(nums), len(changeIndices)

        def can(T: int) -> bool:
            last = {}
            for s in range(T):
                last[changeIndices[s]] = s
            if len(last) < n:
                return False

            free = 0
            for s in range(T):
                i = changeIndices[s]
                if last[i] == s:
                    if free < nums[i - 1]:
                        return False
                    free -= nums[i - 1]
                else:
                    free += 1
            return True

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
