from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        lo, hi = 0, nums[-1] - nums[0]

        while lo < hi:
            mid = (lo + hi) // 2

            count = 0
            i = 0
            for j in range(n):
                while nums[j] - nums[i] > mid:
                    i += 1
                count += j - i

            if count >= k:
                hi = mid
            else:
                lo = mid + 1

        return lo
