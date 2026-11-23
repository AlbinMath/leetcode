from typing import List

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        def solve(a: int, b: int, base: int) -> int:
            cost = base
            for i in range(n - 1):
                x, y = nums1[i], nums2[i]
                if x <= a and y <= b:
                    continue
                if y <= a and x <= b:
                    cost += 1
                else:
                    return float('inf')
            return cost

        res = min(solve(nums1[-1], nums2[-1], 0),
                  solve(nums2[-1], nums1[-1], 1))
        return -1 if res == float('inf') else res
