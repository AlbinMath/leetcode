from typing import List

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        visited = [False] * n
        best = 0
        for i in range(n):
            if not visited[i]:
                length = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = nums[j]
                    length += 1
                best = max(best, length)
        return best
