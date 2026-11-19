from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        run = 0
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1] + 1:
                run += 1
            else:
                run = 1
            if i >= k - 1:
                res.append(nums[i] if run >= k else -1)
        return res
