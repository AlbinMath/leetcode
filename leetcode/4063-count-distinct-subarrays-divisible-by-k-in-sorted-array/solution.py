from math import gcd
from collections import defaultdict
from typing import List

class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1
        pre = 0
        total = 0
        for v in nums:
            pre = (pre + v) % k
            total += cnt[pre]
            cnt[pre] += 1

        n = len(nums)
        i = 0
        while i < n:
            j = i
            while j < n and nums[j] == nums[i]:
                j += 1
            L = j - i
            s = k // gcd(nums[i] % k, k)   # gcd(0, k) = k, so s = 1
            m = L // s
            total -= m * (L + 1) - s * m * (m + 1) // 2
            total += m
            i = j
        return total
