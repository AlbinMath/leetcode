from typing import List

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            return 0 if nums1 == nums2 else -1
        pos = neg = 0
        for a, b in zip(nums1, nums2):
            d = a - b
            if d % k:
                return -1
            if d > 0:
                pos += d // k
            else:
                neg += -d // k
        return pos if pos == neg else -1
