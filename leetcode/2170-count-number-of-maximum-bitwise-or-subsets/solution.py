from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        target = 0
        for x in nums:
            target |= x

        n = len(nums)

        def dfs(i: int, cur: int) -> int:
            if i == n:
                return 1 if cur == target else 0
            return dfs(i + 1, cur | nums[i]) + dfs(i + 1, cur)

        return dfs(0, 0)
