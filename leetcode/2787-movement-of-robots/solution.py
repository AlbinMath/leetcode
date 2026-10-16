from typing import List

class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        MOD = 10**9 + 7
        pos = [x + d if c == 'R' else x - d for x, c in zip(nums, s)]
        pos.sort()
        ans = 0
        prefix = 0
        for i, p in enumerate(pos):
            ans += i * p - prefix
            prefix += p
        return ans % MOD
