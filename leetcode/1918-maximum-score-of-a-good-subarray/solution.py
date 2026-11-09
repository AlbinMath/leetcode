from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = j = k
        mn = nums[k]
        ans = mn

        while i > 0 or j < n - 1:
            left = nums[i - 1] if i > 0 else 0
            right = nums[j + 1] if j < n - 1 else 0
            if left >= right:
                i -= 1
                mn = min(mn, nums[i])
            else:
                j += 1
                mn = min(mn, nums[j])
            ans = max(ans, mn * (j - i + 1))

        return ans
