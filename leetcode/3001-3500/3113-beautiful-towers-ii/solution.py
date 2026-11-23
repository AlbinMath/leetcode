from typing import List

class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)

        def build(arr):
            res = [0] * n
            stack = []  # indices with strictly increasing values
            for i, x in enumerate(arr):
                while stack and arr[stack[-1]] >= x:
                    stack.pop()
                if stack:
                    j = stack[-1]
                    res[i] = res[j] + x * (i - j)
                else:
                    res[i] = x * (i + 1)
                stack.append(i)
            return res

        left = build(maxHeights)
        right = build(maxHeights[::-1])[::-1]
        return max(left[i] + right[i] - maxHeights[i] for i in range(n))
