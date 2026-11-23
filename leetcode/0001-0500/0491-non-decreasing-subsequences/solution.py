from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def dfs(start: int) -> None:
            if len(path) >= 2:
                res.append(path[:])
            used = set()
            for i in range(start, len(nums)):
                x = nums[i]
                if x in used:
                    continue  # same value already tried at this level
                if path and x < path[-1]:
                    continue  # would break non-decreasing order
                used.add(x)
                path.append(x)
                dfs(i + 1)
                path.pop()

        dfs(0)
        return res
