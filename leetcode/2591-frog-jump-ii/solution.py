from typing import List

class Solution:
    def maxJump(self, stones: List[int]) -> int:
        n = len(stones)
        ans = stones[1] - stones[0]
        for i in range(n - 2):
            ans = max(ans, stones[i + 2] - stones[i])
        return ans
