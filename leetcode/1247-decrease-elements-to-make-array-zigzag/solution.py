from typing import List

class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)
        INF = float('inf')

        def cost(start: int) -> int:
            # valleys are at indices start, start+2, ...
            total = 0
            for i in range(start, n, 2):
                left = nums[i - 1] if i > 0 else INF
                right = nums[i + 1] if i + 1 < n else INF
                m = min(left, right)
                if nums[i] >= m:
                    total += nums[i] - m + 1
            return total

        return min(cost(0), cost(1))
