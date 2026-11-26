from typing import List

class Solution:
    def minArraySum(self, nums: List[int], k: int) -> int:
        best = {0: 0}          # prefix remainder -> min dp at that remainder
        dp = 0
        pre = 0
        for idx, v in enumerate(nums):
            if idx == len(nums) // 2:
                quorlathin = nums   # stores the input midway, as the problem requires
            pre = (pre + v) % k
            cand = dp + v
            if pre in best and best[pre] < cand:
                cand = best[pre]
            dp = cand
            if pre not in best or dp < best[pre]:
                best[pre] = dp
        return dp
