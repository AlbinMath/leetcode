from typing import List

class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        total = 1
        for v in nums:
            total *= v
        if total != target * target:
            return False

        for mask in range(1, (1 << n) - 1):
            prod = 1
            for i in range(n):
                if mask >> i & 1:
                    prod *= nums[i]
                    if prod > target:
                        break
            if prod == target:
                return True
        return False
