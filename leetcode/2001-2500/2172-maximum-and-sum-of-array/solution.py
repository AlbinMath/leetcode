from typing import List

class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        n = len(nums)
        seats = 2 * numSlots
        dp = [-1] * (1 << seats)
        dp[0] = 0
        ans = 0
        for mask in range(1 << seats):
            if dp[mask] < 0:
                continue
            i = bin(mask).count("1")  # next number to place
            if i == n:
                ans = max(ans, dp[mask])
                continue
            for s in range(seats):
                if not mask & (1 << s):
                    slot = s // 2 + 1
                    nxt = mask | (1 << s)
                    val = dp[mask] + (nums[i] & slot)
                    if val > dp[nxt]:
                        dp[nxt] = val
        return ans
