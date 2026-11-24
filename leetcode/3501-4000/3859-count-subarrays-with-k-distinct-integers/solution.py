from typing import List
from collections import defaultdict

class Solution:
    def countSubarrays(self, nums: List[int], k: int, m: int) -> int:
        cA = defaultdict(int); dA = 0; lo = 0     # smallest l with distinct <= k
        cB = defaultdict(int); dB = 0; lb = 0     # smallest l with distinct <= k-1
        c3 = defaultdict(int); good = 0; q = 0    # window [q, r], good = values with count >= m
        ans = 0

        for r, x in enumerate(nums):
            if cA[x] == 0: dA += 1
            cA[x] += 1
            while dA > k:
                y = nums[lo]
                cA[y] -= 1
                if cA[y] == 0: dA -= 1
                lo += 1

            if cB[x] == 0: dB += 1
            cB[x] += 1
            while dB > k - 1:
                y = nums[lb]
                cB[y] -= 1
                if cB[y] == 0: dB -= 1
                lb += 1
            hi = lb - 1

            c3[x] += 1
            if c3[x] == m: good += 1
            if good >= k:
                # advance q while removing nums[q] still leaves good >= k
                while True:
                    v = nums[q]
                    if c3[v] == m and good <= k:
                        break
                    if c3[v] == m:
                        good -= 1
                    c3[v] -= 1
                    q += 1
                top = min(hi, q)
                if top >= lo:
                    ans += top - lo + 1
        return ans
