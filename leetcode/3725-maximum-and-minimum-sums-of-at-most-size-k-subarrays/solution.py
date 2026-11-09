from typing import List

class Solution:
    def minMaxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = k + 1

        def G(a, t):
            if t <= 1:
                return 0
            m = min(a, t - 1)
            return m * t - m * (m + 1) // 2

        def sum_mins(arr):
            prev = [-1] * n
            nxt = [n] * n
            stack = []
            for i in range(n):
                while stack and arr[stack[-1]] >= arr[i]:
                    nxt[stack.pop()] = i
                prev[i] = stack[-1] if stack else -1
                stack.append(i)

            total = 0
            for i in range(n):
                a = min(i - prev[i], k)
                b = min(nxt[i] - i, k)
                total += arr[i] * (G(a, s) - G(a, s - b))
            return total

        return sum_mins(nums) - sum_mins([-x for x in nums])
