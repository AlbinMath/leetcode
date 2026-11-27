from typing import List

class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        limit = k
        total = k * (k + 1) // 2
        for x in sorted(set(nums)):
            if x <= limit:
                limit += 1
                total += limit - x
            else:
                break
        return total
