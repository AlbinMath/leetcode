from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for x in arr:
            if not stack or x >= stack[-1]:
                stack.append(x)
            else:
                mx = stack.pop()
                while stack and stack[-1] > x:
                    stack.pop()
                stack.append(mx)
        return len(stack)
