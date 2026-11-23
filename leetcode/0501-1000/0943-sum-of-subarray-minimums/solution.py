from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        stack = []
        total = 0

        for j in range(n + 1):
            cur = arr[j] if j < n else 0   # sentinel 0 pops everything
            while stack and arr[stack[-1]] >= cur:
                i = stack.pop()
                prev = stack[-1] if stack else -1
                total += arr[i] * (i - prev) * (j - i)
            stack.append(j)

        return total % MOD
