from typing import List

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        def sum_mins(arr: List[int]) -> int:
            n = len(arr)
            stack = []
            total = 0
            for j in range(n + 1):
                while stack and (j == n or arr[stack[-1]] >= arr[j]):
                    i = stack.pop()
                    prev = stack[-1] if stack else -1
                    total += arr[i] * (i - prev) * (j - i)
                stack.append(j)
            return total

        return -sum_mins([-x for x in nums]) - sum_mins(nums)
