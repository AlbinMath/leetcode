from bisect import bisect_left, insort
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        w = sorted(nums[:k])
        res = []
        for i in range(k, len(nums) + 1):
            if k % 2:
                res.append(float(w[k // 2]))
            else:
                res.append((w[k // 2 - 1] + w[k // 2]) / 2.0)
            if i == len(nums):
                break
            del w[bisect_left(w, nums[i - k])]
            insort(w, nums[i])
        return res
