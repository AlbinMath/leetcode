from typing import List

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        cnt = [0] * value
        for x in nums:
            cnt[x % value] += 1
        m = 0
        while True:
            r = m % value
            if cnt[r] == 0:
                return m
            cnt[r] -= 1
            m += 1
