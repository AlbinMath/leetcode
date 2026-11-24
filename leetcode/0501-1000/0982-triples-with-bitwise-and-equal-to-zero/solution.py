from typing import List
from collections import Counter

class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        freq = Counter(nums)
        items = list(freq.items())

        # cnt[v] = number of ordered pairs (i, j) with nums[i] & nums[j] == v
        cnt = Counter()
        for a, fa in items:
            for b, fb in items:
                cnt[a & b] += fa * fb

        ans = 0
        for v, c in cnt.items():
            for x, fx in items:
                if v & x == 0:
                    ans += c * fx
        return ans
