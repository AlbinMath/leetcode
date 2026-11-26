from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def is_arithmetic(sub: List[int]) -> bool:
            k = len(sub)
            min_val = min(sub)
            max_val = max(sub)
            if (max_val - min_val) % (k - 1) != 0:
                return False
                
            step = (max_val - min_val) // (k - 1)
            if step == 0:
                return True
                
            seen = set(sub)
            return all((min_val + i * step) in seen for i in range(k))

        return [is_arithmetic(nums[left : right + 1]) for left, right in zip(l, r)]
