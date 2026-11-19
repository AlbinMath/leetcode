from typing import List

class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        n = len(nums)
        S = sum(nums)
        full = (target // S) * n
        rem = target % S
        if rem == 0:
            return full

        arr = nums + nums
        best = float('inf')
        l = 0
        cur = 0
        for r, x in enumerate(arr):
            cur += x
            while cur > rem:
                cur -= arr[l]
                l += 1
            if cur == rem:
                best = min(best, r - l + 1)

        return -1 if best == float('inf') else full + best
