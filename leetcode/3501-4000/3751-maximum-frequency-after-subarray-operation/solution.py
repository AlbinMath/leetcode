from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        total_k = nums.count(k)
        best_gain = 0

        for v in range(1, 51):
            if v == k:
                continue
            cur = 0
            for a in nums:
                if a == v:
                    cur += 1
                elif a == k:
                    cur -= 1
                if cur < 0:
                    cur = 0
                if cur > best_gain:
                    best_gain = cur

        return total_k + best_gain
