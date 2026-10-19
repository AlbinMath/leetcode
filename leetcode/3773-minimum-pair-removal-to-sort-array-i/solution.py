from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        a = nums[:]
        ops = 0
        while any(a[i] > a[i + 1] for i in range(len(a) - 1)):
            # leftmost adjacent pair with the minimum sum
            idx = min(range(len(a) - 1), key=lambda i: a[i] + a[i + 1])
            a[idx:idx + 2] = [a[idx] + a[idx + 1]]
            ops += 1
        return ops
