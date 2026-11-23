from typing import List

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        answer = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            # Shorter people are visible and then blocked by the
            # first person taller than them.
            while stack and heights[stack[-1]] < heights[i]:
                stack.pop()
                answer[i] += 1

            # The first person taller than heights[i] is also visible.
            if stack:
                answer[i] += 1

            stack.append(i)

        return answer
